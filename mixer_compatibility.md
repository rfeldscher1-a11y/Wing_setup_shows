# Digital Mixer Compatibility Reference
### Soundman App — Target Platform List
*Last updated: May 2026*

This document lists modern digital mixing consoles under $25,000, their communication protocols, remote control capabilities, and Soundman app integration difficulty.

---

## Integration Difficulty Key
- 🟢 **Easy** — Open protocol, well documented, OSC or similar
- 🟡 **Medium** — Partially documented, may require reverse engineering
- 🔴 **Hard** — Proprietary/closed protocol, limited access

---

## BEHRINGER / MIDAS (Primary Targets)

### Behringer Wing Rack (~$3,000)
| Property | Detail |
|---|---|
| Protocol | OSC over TCP/UDP |
| Remote Port | 2223 |
| Discovery | Send `WING?` UDP packet |
| Data Format | JSON-based parameter tree |
| Preset Format | `.chn` (channel), `.snap` (snapshot), `.show` (show file) |
| App | Wing Edit (iOS/Android/Desktop) |
| Integration | 🟢 Easy — fully documented, open protocol |

### Behringer X32 / X32 Rack (~$1,200–$2,500)
| Property | Detail |
|---|---|
| Protocol | OSC over UDP |
| Remote Port | 10023 |
| Keepalive | Send `/xremote` every 10 seconds |
| Data Format | Flat OSC address space |
| Preset Format | Binary blob (partially documented) |
| App | X32-Edit (iOS/Android/Desktop) |
| Integration | 🟢 Easy — massive community, excellent docs |

### Behringer XR18 / XR16 / XR12 (~$600–$900)
| Property | Detail |
|---|---|
| Protocol | OSC over UDP |
| Remote Port | 10024 |
| Keepalive | Send `/xremote` every 10 seconds |
| Data Format | Same as X32 family |
| App | X Air Edit (iOS/Android/Desktop) |
| Integration | 🟢 Easy — identical to X32 protocol family |

### Midas M32 / M32R (~$4,000–$5,500)
| Property | Detail |
|---|---|
| Protocol | OSC over UDP (same as X32) |
| Remote Port | 10023 |
| Data Format | Same as X32 family |
| App | M32-Edit (iOS/Android/Desktop) |
| Integration | 🟢 Easy — shares X32 codebase |

---

## ALLEN & HEATH

### Allen & Heath SQ5 / SQ6 / SQ7 (~$2,500–$5,500)
| Property | Detail |
|---|---|
| Protocol | MIDI over Network + proprietary TCP |
| Remote Port | Proprietary (SQ MixPad protocol) |
| Data Format | Proprietary binary |
| Preset Format | `.scn` (scene), channel presets via SQ app |
| App | SQ MixPad (iOS/Android) |
| Open API | Partial — MIDI controllable, some OSC via third party |
| Integration | 🟡 Medium — MIDI accessible, full API not public |
| Note | Class-compliant USB audio on Mac, ASIO/WDM on Windows |

### Allen & Heath dLive C1500 (~$8,000–$15,000)
| Property | Detail |
|---|---|
| Protocol | Proprietary TCP + OSC external control |
| Data Format | Proprietary |
| App | dLive Director (iOS/Android/Desktop) |
| Integration | 🟡 Medium — OSC external control available |

### Allen & Heath Avantis Solo (~$4,500)
| Property | Detail |
|---|---|
| Protocol | Proprietary TCP |
| App | Avantis Director (iOS/Android) |
| Integration | 🟡 Medium |

---

## YAMAHA

### Yamaha TF5 (~$3,799)
| Property | Detail |
|---|---|
| Protocol | Proprietary TCP/IP |
| Data Format | Proprietary |
| App | TF StageMix (iPad only) |
| MIDI | Yes — via USB |
| Integration | 🟡 Medium — no open API, MIDI controllable |

### Yamaha CL1 / CL3 / CL5 (~$10,000–$25,000)
| Property | Detail |
|---|---|
| Protocol | Yamaha Pro Audio Network (proprietary) |
| Remote Port | Proprietary |
| Data Format | Proprietary binary |
| App | StageMix (iPad), MonitorMix (iOS/Android) |
| MIDI | Yes |
| Integration | 🔴 Hard — closed proprietary protocol |

---

## PRESONUS

### PreSonus StudioLive 32S / 64S (~$3,000–$5,000)
| Property | Detail |
|---|---|
| Protocol | Proprietary over AVB network |
| Data Format | Proprietary |
| App | UC Surface (iOS/Android/Desktop) |
| OSC | Partial — reverse engineered third party tools exist |
| MIDI | No dedicated MIDI ports — network only |
| Integration | 🟡 Medium — OSC partially available via third party |
| Note | AVB networking requires AVB-compatible hardware |

---

## DIGICO

### DiGiCo SD12 (~$15,000–$20,000)
| Property | Detail |
|---|---|
| Protocol | OSC over Ethernet (External Control) |
| Remote Port | 8200 (receive) / 9111 (send) |
| Data Format | OSC |
| Preset Format | Proprietary snapshots |
| App | DiGiCo SD Remote (iPad) |
| Integration | 🟡 Medium — OSC available but setup required |
| Note | Default IP 192.168.x.x subnet, /16 mask |

### DiGiCo S21 (~$8,000–$12,000)
| Property | Detail |
|---|---|
| Protocol | OSC over Ethernet |
| Integration | 🟡 Medium — same as SD series |

---

## AVID

### Avid S1 / S3 / VENUE S6L (~$5,000–$25,000)
| Property | Detail |
|---|---|
| Protocol | Proprietary Avid EUCON + Pro Tools integration |
| Data Format | EUCON protocol |
| App | VENUE control via software |
| Integration | 🔴 Hard — EUCON is proprietary and licensed |

---

## QSC

### QSC TouchMix-8 (~$599)
| Property | Detail |
|---|---|
| Protocol | Proprietary WiFi TCP/IP |
| App | TouchMix app (iOS/Android) |
| Integration | 🟡 Medium |

### QSC TouchMix-16 (~$999)
| Property | Detail |
|---|---|
| Protocol | Proprietary WiFi TCP/IP |
| App | TouchMix app (iOS/Android) |
| Integration | 🟡 Medium |

### QSC TouchMix-30 Pro (~$1,899)
| Property | Detail |
|---|---|
| Protocol | Proprietary WiFi TCP/IP + Mackie Control Protocol (v2.0+) |
| Remote Port | Proprietary WiFi |
| App | TouchMix app (iOS/Android) |
| Control Surface | Supports third-party motorized fader surfaces via Mackie Control Protocol |
| Integration | 🟡 Medium — Mackie Control Protocol support provides a known hook |
| Note | Does NOT integrate with QSC Q-SYS platform — separate ecosystem entirely |

**Field Note:** TouchMix-30 Pro used personally — mixed Burning Vernon, a Robert Cray tribute band from Santa Cruz. Solid performer, intuitive touchscreen workflow.

---

## MACKIE

### Mackie DL32R (~$1,500)
| Property | Detail |
|---|---|
| Protocol | Proprietary WiFi |
| App | Master Fader (iOS only) |
| Integration | 🟡 Medium — iOS app only, limited API |

---

## QSC

### QSC TouchMix-30 Pro (~$1,500)
| Property | Detail |
|---|---|
| Protocol | Proprietary WiFi TCP/IP |
| App | TouchMix app (iOS/Android) |
| Integration | 🟡 Medium |

---

## SOUNDCRAFT

### Soundcraft Ui24R (~$1,200)
| Property | Detail |
|---|---|
| Protocol | WebSocket over WiFi |
| Data Format | JSON over WebSocket |
| App | Browser-based + iOS/Android |
| Integration | 🟢 Easy — WebSocket/JSON is very accessible |
| Note | Unique browser-based control is developer friendly |

---

## Summary — Integration Priority for Soundman App

| Priority | Console Family | Why |
|---|---|---|
| 1 | Behringer Wing/X32/XR18/Midas M32 | Open OSC, massive install base, your primary platform |
| 2 | Soundcraft Ui series | WebSocket/JSON — unusually developer friendly |
| 3 | DiGiCo SD/S series | OSC available, professional touring market |
| 4 | Allen & Heath SQ/dLive | MIDI + partial OSC, huge church/live market |
| 5 | PreSonus StudioLive | Large install base, partial OSC via third party |
| 6 | Yamaha TF/CL | MIDI only on TF, CL is closed — lower priority |
| 7 | Avid VENUE | EUCON is proprietary and licensed — very hard |

---

## Market Share & Sales Data
*Source: Sweetwater catalog count, market research reports — May 2026*

### Overall Market
- Digital mixer consoles dominate with **62.5% share** of total mixing console market
- North America leads globally with **35.7% of sales**
- Market valued at ~$1.8 billion in 2024, projected $3.4 billion by 2033 (8.48% CAGR)

### Brand Market Presence
*(Sweetwater SKU count used as install base proxy)*

| Rank | Brand | Sweetwater SKUs | Notes |
|---|---|---|---|
| 1 | Allen & Heath | 118 | Largest catalog, dominant in church/live |
| 2 | Behringer | 91 | Highest volume sales, most accessible protocol |
| 3 | Yamaha | 58 | Strong in education, worship, corporate |
| 4 | PreSonus | 48 | Acquired by Fender in Q2 2025 — direction uncertain |
| 5 | Midas | 37 | Premium Behringer family, touring market |
| 6 | Soundcraft | 23 | Install market, WebSocket protocol |
| 7 | DiGiCo | 21 | High-end touring, arena level |
| 8 | Mackie | 21 | Entry level, consumer market |

### Top Selling Product Families
*(Sweetwater product count by series)*

| Rank | Product Family | SKUs |
|---|---|---|
| 1 | Allen & Heath Qu | 49 |
| 2 | PreSonus StudioLive Series III | 42 |
| 3 | Behringer Wing | 32 |
| 4 | Allen & Heath SQ | 27 |
| 5 | Behringer X-Series | 23 |
| 6 | Midas M Series | 21 |
| 7 | Allen & Heath CQ | 18 |
| 8 | Yamaha MGX | 18 |
| 9 | Yamaha DM | 17 |
| 10 | Yamaha TF | 16 |

### Best Selling Models by Sales Volume
*Based on Amazon sales signals, Sweetwater reviews, and industry reporting. Note: exact unit sales figures are proprietary and not publicly disclosed by manufacturers.*

| Rank | Model | Price Range | Why It Sells |
|---|---|---|---|
| 1 | Behringer X32 / X32 Rack | $1,200–$2,500 | Undisputed volume leader, price/performance king |
| 2 | Allen & Heath SQ-5 | ~$2,500 | Top selling mid-range pro model |
| 3 | Yamaha TF series | $1,500–$4,000 | Dominant in live venues and worship |
| 4 | Midas M32 | ~$4,000–$5,500 | Strong in touring and professional installs |
| 5 | PreSonus StudioLive 32SC | ~$3,000 | Strong in worship and education |
| 6 | Soundcraft Ui16 / Ui24R | $800–$1,500 | Popular in install and portable markets |
| 7 | Behringer Wing | ~$3,000 | Growing rapidly, newer product |
| 8 | Allen & Heath Qu series | $1,500–$3,500 | Large install base in churches and venues |

**Field Note:** The Allen & Heath Qu-30 has been used personally at a local venue — solid performer, good candidate for Soundman compatibility.

### Key Market Intelligence for Soundman
- Behringer X32 Rack is a **top seller on Amazon** — huge installed base of budget-conscious engineers
- Allen & Heath leads in **church and house of worship** market — massive and underserved for preset tools
- PreSonus acquired by **Fender (Q2 2025)** — product direction may shift, worth monitoring
- Allen & Heath partnered with **Audinate/Dante (Q2 2025)** — expanding networking capabilities
- Fastest growing segment: **16-32 channel range** — exactly your target user demographic
- North America is **fastest growing region** — your home market

### Strategic Takeaway for Soundman
The Behringer/Midas family has the most accessible protocol AND the highest volume sales in your price range. Allen & Heath has the largest overall catalog presence and dominates the church market. Supporting both families in Phase 1 of Soundman covers the majority of your potential user base.
