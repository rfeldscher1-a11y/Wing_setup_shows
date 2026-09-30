#!/usr/bin/env python3
"""
Wing OSC Communication Test
============================
Tests basic OSC communication with the Behringer Wing Rack.
Sends WING? discovery packet and reads/writes basic parameters.

Requirements:
    pip install python-osc

Usage:
    python wing_osc_test.py --ip 192.168.1.100 --port 2223
"""

import argparse
import socket
import time
from pythonosc import dispatcher, osc_server, udp_client
from pythonosc.osc_message_builder import OscMessageBuilder


WING_DEFAULT_PORT = 2223
WING_DISCOVERY_MSG = b"WING?"


def discover_wing(broadcast_ip="255.255.255.255", port=WING_DEFAULT_PORT, timeout=3):
    """Send WING? discovery packet and listen for response."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(timeout)

    print(f"Sending WING? discovery to {broadcast_ip}:{port}...")
    sock.sendto(WING_DISCOVERY_MSG, (broadcast_ip, port))

    try:
        data, addr = sock.recvfrom(1024)
        print(f"Wing found at: {addr[0]}")
        print(f"Response: {data}")
        return addr[0]
    except socket.timeout:
        print("No Wing found on network.")
        return None
    finally:
        sock.close()


def mute_channel(client, channel: int, mute: bool):
    """Mute or unmute a channel."""
    path = f"/ch/{channel}/mute"
    value = "ON" if mute else "OFF"
    msg = OscMessageBuilder(address=path)
    msg.add_arg(value, arg_type="s")
    client.send(msg.build())
    print(f"Channel {channel} mute: {value}")


def set_fader(client, channel: int, level_db: float):
    """Set channel fader level in dB."""
    path = f"/ch/{channel}/fader"
    msg = OscMessageBuilder(address=path)
    msg.add_arg(level_db, arg_type="f")
    client.send(msg.build())
    print(f"Channel {channel} fader: {level_db} dB")


def set_eq_band(client, channel: int, band: int, freq: float, gain: float, q: float):
    """Set an EQ band on a channel."""
    base = f"/ch/{channel}/eq/b{band}"
    for param, val, typ in [("freq", freq, "f"), ("gain", gain, "f"), ("q", q, "f")]:
        msg = OscMessageBuilder(address=f"{base}/{param}")
        msg.add_arg(val, arg_type=typ)
        client.send(msg.build())
    print(f"Ch {channel} EQ Band {band}: freq={freq}Hz gain={gain}dB q={q}")


def apply_60hz_hum_removal(client, channel: int):
    """
    Apply 60Hz hum removal notch filters to a channel.
    Targets 60Hz fundamental and harmonics: 180, 300, 420, 540 Hz.
    Derived from Studio One Pro EQ preset analysis.
    """
    print(f"\nApplying 60Hz Hum Removal to Channel {channel}...")

    # Low cut at 29.24 Hz
    msg = OscMessageBuilder(address=f"/ch/{channel}/eq/lc/freq")
    msg.add_arg(29.24, arg_type="f")
    client.send(msg.build())

    msg = OscMessageBuilder(address=f"/ch/{channel}/eq/lc/on")
    msg.add_arg("ON", arg_type="s")
    client.send(msg.build())

    # Notch filters
    notch_freqs = [60.0, 180.0, 300.0, 420.0, 540.0]
    for i, freq in enumerate(notch_freqs, start=1):
        base = f"/ch/{channel}/eq/b{i}"
        for param, val, typ in [
            ("freq", freq, "f"),
            ("gain", -24.0, "f"),
            ("q", 24.0, "f"),
            ("type", "NOTCH", "s"),
            ("on", "ON", "s"),
        ]:
            msg = OscMessageBuilder(address=f"{base}/{param}")
            msg.add_arg(val, arg_type=typ)
            client.send(msg.build())
        print(f"  Notch filter {i}: {freq} Hz @ -24dB Q=24")

    # Enable EQ
    msg = OscMessageBuilder(address=f"/ch/{channel}/eq/on")
    msg.add_arg("ON", arg_type="s")
    client.send(msg.build())
    print("60Hz Hum Removal applied.")


def main():
    parser = argparse.ArgumentParser(description="Wing OSC Test Tool")
    parser.add_argument("--ip", default=None, help="Wing IP address (auto-discover if not set)")
    parser.add_argument("--port", type=int, default=WING_DEFAULT_PORT, help="Wing OSC port")
    parser.add_argument("--channel", type=int, default=15, help="Channel to test (default: 15 Lead Vocal)")
    args = parser.parse_args()

    # Discover or use provided IP
    wing_ip = args.ip or discover_wing()
    if not wing_ip:
        print("Could not find Wing. Exiting.")
        return

    # Create OSC client
    client = udp_client.SimpleUDPClient(wing_ip, args.port)
    print(f"\nConnected to Wing at {wing_ip}:{args.port}")

    # Test basic communication
    print(f"\nTesting channel {args.channel}...")
    set_fader(client, args.channel, 0.0)
    time.sleep(0.1)

    # Apply hum removal as demo
    apply_60hz_hum_removal(client, args.channel)

    print("\nTest complete.")


if __name__ == "__main__":
    main()
