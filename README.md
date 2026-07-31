# Wing Setup & Shows
### Behringer Wing Rack — 11th Street Disciples / Malice in Wonderland

A growing library of presets, routing configurations, show files, documentation, and app code for the Behringer Wing Rack digital mixing console.

This repository also serves as the foundation for **Soundman** — a multiplatform app for live sound engineers to manage presets and control digital mixers across multiple console brands, with a marketplace for engineer signature packs.

---

## About This Project

Built by a working live sound engineer for a 7-piece band. Everything here is real-world tested and designed for practical use at small-to-medium live venues.

**Current rig:**
- Console: Behringer Wing Rack (Firmware 3.1)
- Stage Box: Behringer S32 (AES50)
- Secondary Mixer: Behringer XR18
- Inputs: 27 channels (drums, stage, keyboard rig)
- Outputs: 8 monitor mixes (wedges + IEM)
- Capture: 64ch WING-LIVE dual SD

---

## Repository Structure

```
Wing_setup_shows/
├── presets/
│   ├── vocals/          # Lead vocal, BGV channel presets
│   ├── drums/           # Kick, snare, tom, overhead presets
│   ├── instruments/     # Keys, guitar, bass presets
│   └── hum_removal/     # 60Hz and noise reduction presets
├── routing/
│   ├── input_patch/     # Source to channel mapping
│   └── output_patch/    # Bus and monitor routing
├── snippets/            # GPIO configs, partial configurations
├── shows/               # Complete show files
├── docs/                # Reference documentation
│   ├── equipment_inventory.md
│   ├── mixer_compatibility.md
│   ├── publications_and_media.md
│   └── soundman_glossary.md
└── apps/                # OSC tools and utility scripts
    └── wing_osc_test.py
```

---

## Input Channel Map

| Channel | Source |
|---|---|
| Ch 1 | Kick In |
| Ch 2 | Kick Out |
| Ch 3 | Snare Top |
| Ch 4 | Snare Bottom |
| Ch 5 | Tom High |
| Ch 6 | Tom Mid |
| Ch 7 | Tom Floor |
| Ch 8 | Overhead L |
| Ch 9 | Overhead R |
| Ch 10 | Hi-Hat |
| Ch 11 | Bass DI |
| Ch 12 | Electric Guitar L |
| Ch 13 | Electric Guitar R |
| Ch 14 | Acoustic Guitar |
| Ch 15 | Lead Vocal |
| Ch 16 | BGV 1 |
| Ch 17 | BGV 2 |
| Ch 18 | BGV 3 / Spare |
| Ch 19-20 | Keys Synth L/R |
| Ch 21-22 | Keys Pad L/R |
| Ch 23-24 | Aux Keys L/R |
| Ch 25-26 | Keys FX L/R |
| Ch 27 | Bass/Click (Mono) |

---

## Output Map

| Bus | Destination |
|---|---|
| Bus 1 | Wedge 1 |
| Bus 2 | Wedge 2 |
| Bus 3 | Wedge 3 |
| Bus 4 | Wedge 4 |
| Bus 5-6 | Keys/Bass IEM (Stereo) |
| Bus 7-8 | Drum IEM (Stereo) |

---

## GPIO Assignments

| Port | Function | Mode |
|---|---|---|
| GPIO 1 | Leslie Speed Toggle | Toggle (N.O.) |
| GPIO 2 | FX Kill Switch | Latching |

---

## Vocal FX Chain

```
Lead Vocal → 76 Limiter Amp → VSS3 Reverb → Stereo Delay → Pitch Fix
```

---

## OSC Communication

| Mixer | Protocol | Port |
|---|---|---|
| Wing Rack | OSC over TCP/UDP | 2223 |
| XR18 | OSC over UDP | 10024 |

**Wing discovery:** Send `WING?` UDP packet to broadcast address

---

## Soundman App

This repo is the development foundation for **Soundman** — a multiplatform Flutter app for live sound engineers.

**Planned features:**
- Preset management and deployment across multiple console brands
- Real-time OSC control of Wing Rack and XR18
- Marketplace for engineer signature preset packs
- PA/Mixer split architecture with protected venue profiles
- Cross-console preset translation engine

**Target platforms:** iOS, Android, Windows, Mac, Web

---

## License

MIT License — open for personal and educational use.
Presets and show files are provided as-is for reference.
Commercial use of this repository's contents requires permission.

---

## Contact

Rob Feldscher
11th Street Disciples / Malice in Wonderland
GitHub: @rfeldscher1-a11y
