# AI, Tech & Audio Engineering Glossary
### Plain English Definitions for Real People
*No fluff. No hype. Just what things actually mean.*

---

## PART 1 — General AI Terms
*(The stuff the Facebook influencers say)*

**AI — Artificial Intelligence**
Software that can do tasks that normally require human thinking, like recognizing speech, writing text, or making decisions. Umbrella term for everything below.

**ML — Machine Learning**
A type of AI where the computer learns from examples instead of being explicitly programmed. It figures out patterns on its own.

**LLM — Large Language Model**
The technology behind ChatGPT, Claude, Gemini, etc. A massive AI trained on huge amounts of text that can read and write human language. "Large" refers to the number of parameters (billions).

**GPT — Generative Pre-trained Transformer**
The architecture behind OpenAI's models. "Generative" = creates new content. "Pre-trained" = learned from data before you used it. "Transformer" = the underlying math structure. ChatGPT uses this.

**Claude**
Anthropic's AI assistant — that's me. Named after Claude Shannon, the father of information theory.

**Gemini**
Google's AI model family. Formerly called Bard.

**API — Application Programming Interface**
A way for two software programs to talk to each other. When your app sends an OSC message to your Wing Rack, it's using an API. When Soundman talks to an AI or another service, it uses an API.

**Prompt**
The text or instruction you give to an AI. "Write me a preset for lead vocals" is a prompt.

**Token**
How AI models measure text — roughly 3/4 of a word. AI models have a limit on how many tokens they can process at once (their "context window").

**Context Window**
How much text an AI can "remember" in a single conversation. Claude's is very large. When it fills up, older parts of the conversation get pushed out.

**Hallucination**
When an AI confidently makes something up. Not lying — it genuinely doesn't know it's wrong. Always verify important facts.

**RAG — Retrieval Augmented Generation**
A technique where AI looks up real documents before answering, instead of relying only on its training. Makes answers more accurate and current.

**Fine-tuning**
Taking an existing AI model and training it further on specific data to specialize it. Like teaching a general doctor to become a cardiologist.

**Neural Network**
The mathematical structure that powers modern AI — loosely inspired by how brain neurons connect. Layers of math that transform inputs into outputs.

**Parameters / Weights**
The numbers inside an AI model that determine how it behaves. GPT-4 has hundreds of billions of these. More parameters generally = more capable but slower and more expensive.

**Inference**
When an AI actually runs and generates a response. Training is when it learns; inference is when it works.

**Training Data**
The text/images/audio the AI learned from. Claude was trained on a large portion of the internet plus books and other sources.

**AGI — Artificial General Intelligence**
A hypothetical AI that can do anything a human can do, across any domain. Doesn't exist yet. What influencers like to scare or excite you about.

**ASI — Artificial Super Intelligence**
Hypothetical AI smarter than all humans combined. Even further away. Mostly sci-fi right now.

**OpenAI**
The company that makes ChatGPT and GPT models. Originally nonprofit, now very much a business.

**Anthropic**
The company that makes Claude. Founded by former OpenAI researchers focused on AI safety.

**Copilot**
Microsoft's AI assistant built into Windows, Office, and GitHub. Powered by OpenAI's models.

**Agent / AI Agent**
An AI that can take actions autonomously — like browsing the web, writing code, or controlling software — not just answer questions.

**MCP — Model Context Protocol**
A standard way for AI models to connect to external tools and services. What allows Claude to check your calendar or search Google Drive.

**Vector Database**
A special database that stores information in a way that AI can search by meaning rather than exact words. Used in RAG systems.

**Embeddings**
A way of converting text into numbers so AI can compare meanings mathematically. "King minus Man plus Woman equals Queen" is a classic example.

**Multimodal**
An AI that can work with multiple types of input — text, images, audio, video. Claude, GPT-4, and Gemini are all multimodal.

**Zero-shot / Few-shot**
Zero-shot: asking AI to do something with no examples. Few-shot: giving it a couple of examples first. Few-shot usually works better.

**Temperature**
A setting that controls how creative/random an AI's responses are. Low temperature = more predictable. High temperature = more creative and unpredictable.

**SaaS — Software as a Service**
Software you access over the internet on a subscription basis instead of installing it. Claude, Spotify, and Google Docs are all SaaS.

**Open Source**
Software where the code is publicly available for anyone to use, modify, or build on. The opposite of proprietary/closed source.

**Closed Source / Proprietary**
Software where the code is private and owned by a company. Most commercial AI models are closed source.

### Added October 2026

**Claude Desktop**
The Claude app you install on your Windows or Mac computer. Unlike the web version, it can connect to local tools (through MCP) like your files, GitHub, or your Wing Rack.

**Claude Code**
Anthropic's coding assistant that runs in a terminal (command line). You type what you want built or fixed, and it reads, writes, and runs code for you.

**Context Engineering**
The skill of deciding exactly what information, instructions, and tools an AI gets to see so it gives good answers. Think of it as prompt writing grown up — you're setting up the whole workspace, not just one question.

**Flowise**
A free, open-source tool for building AI apps and chatbots by dragging and connecting boxes on screen instead of writing code. Usually run locally with Docker.

**AI Avatar**
A computer-generated video version of a person that can "speak" any script you give it. Lets you make videos without appearing on camera yourself.

**Project (Claude)**
A shared workspace inside Claude that keeps documents, instructions, and memory persistent across multiple conversations. The Mixer Programming App project holds the Wing Rack and Soundman work.

**NotebookLM**
Google's AI research tool that reads documents you upload and lets you ask questions, build summaries, and generate audio overviews. Handy for turning band interviews and manuals into organized reference material.

**Proto-Soundman**
Using Claude Desktop with OSC tools as a live mixer controller before the full Soundman Flutter app exists — a working proof of concept using the same Wing Rack communication the app will use.

---

## PART 2 — App Development Terms
*(Flutter, Dart, and building Soundman)*

**Flutter**
Google's framework for building apps that run on iOS, Android, Windows, Mac, and web from a single codebase. What we're planning to build Soundman in.

**Dart**
The programming language Flutter uses. Designed by Google, beginner-friendly, fast.

**SDK — Software Development Kit**
A package of tools, libraries, and documentation for building software on a specific platform. You install the Flutter SDK to start building Flutter apps.

**IDE — Integrated Development Environment**
A fancy text editor for writing code. VS Code and Android Studio are popular for Flutter development.

**UI — User Interface**
What the user sees and interacts with. Buttons, sliders, screens, menus.

**UX — User Experience**
How the user feels using the app. Good UX = intuitive and satisfying. Bad UX = confusing and frustrating.

**Widget**
Flutter's building block for UI. Everything in a Flutter app is a widget — buttons, text, layouts, animations.

**State**
The current data/condition of your app. When a fader moves, that's a state change. Managing state well is one of the core challenges in app development.

**Native**
An app built specifically for one platform (iOS or Android) using that platform's own tools. Flutter compiles to native code even though you write it once.

**Cross-platform**
An app that runs on multiple platforms from one codebase. Flutter is cross-platform.

**REST API**
A common style of API that uses standard web requests (GET, POST, PUT, DELETE). Very common for web services.

**WebSocket**
A persistent two-way connection between an app and a server. Used by Soundcraft Ui series mixers. More efficient than REST for real-time control.

**JSON — JavaScript Object Notation**
A simple, human-readable data format. The Wing Rack's parameter tree is JSON-based. Looks like: `{"channel": 1, "fader": 0.0, "mute": false}`

**Repository / Repo**
A folder that stores your code with full version history. Your Wing_setup_shows repo on GitHub is one.

**Git**
The version control system that tracks changes to your code. GitHub is built on Git.

**Commit**
Saving a snapshot of your code at a point in time. Like a save game — you can always go back.

**Push / Pull**
Push = sending your local code changes up to GitHub. Pull = downloading changes from GitHub to your local machine.

**Branch**
A separate copy of your code where you can experiment without affecting the main version. When it works, you merge it back in.

**Debug**
Finding and fixing errors in code. Bugs are errors. Debugging is the process of hunting them down.

**Library / Package**
Pre-written code someone else made that you can use in your app. The `libwing` Dart package for Wing communication is a library.

**Pub.dev**
Flutter/Dart's official package repository — like an app store for code libraries.

**Compile**
Converting human-readable code into machine code the computer can actually run.

**Deploy**
Publishing your app so users can download and use it.

**App Store / Play Store**
Apple's (iOS) and Google's (Android) platforms for distributing apps. To sell Soundman you'd publish it here.

### Added October 2026

**Docker**
A tool that packages an app together with everything it needs to run, so it works the same on any computer. Used to run things like Flowise and the GitHub MCP server on your laptop.

**Container / Docker Image**
An image is the packaged, ready-to-go recipe for an app; a container is a running copy of that image. You "pull" an image once, then start containers from it whenever you need it.

**WSL2 — Windows Subsystem for Linux**
A built-in Windows feature that runs a real Linux system inside Windows. Docker Desktop uses it behind the scenes.

**PAT — Personal Access Token**
A long password-like code that lets an app (like Claude) access your GitHub account with only the permissions you choose. Keep it secret, and note when it expires.

**Pull Request (PR)**
A request to merge changes from one branch into another (usually into main). It lets you review exactly what changed before accepting it.

**Interface / Adapter**
An interface is a shared "contract" listing what a piece of code must be able to do (like "set fader" or "mute channel"). An adapter is the code that makes one specific mixer — Wing, XR18, StudioLive — fulfill that contract, so the app can treat all mixers the same way.

**React**
A popular JavaScript library for building web app screens out of reusable pieces. The Wing Command Center app is built with it.

**localStorage**
A small storage space inside your web browser where a web app can save data, like settings, between visits. It stays on that one browser and computer only.

**Keepalive**
A small message sent regularly just to keep a connection open. The XR18 stops sending updates unless it gets an `/xremote` keepalive every few seconds.

**Reverse Engineering**
Figuring out how a product or protocol works by watching and analyzing it, when the maker hasn't published the details. That's how the community learned PreSonus's UCNET protocol.

**Wing Command Center**
The React web app for controlling the Wing Rack from a browser over OSC.

**Marketplace**
A store inside an app where creators sell or share their work. Soundman plans a marketplace where engineers can sell signature preset packs for different console brands.

**Preset Translation Engine**
A planned Soundman feature that converts a preset made for one console (like the Wing) into the equivalent settings for another (like the XR18 or X32).

**PA/Mixer Split Architecture**
Treating the PA side (mains, subs, output EQ) and the Mixer side (inputs, effects, monitor mixes) as two separate domains. The PA side gets locked once dialed in; the Mixer side stays fluid from show to show.

---

## PART 3 — Audio Engineering & Mixing Terms

### Signal Flow & Gain Staging

**Gain Structure / Gain Staging**
Setting proper levels at every stage of the signal path — from mic preamp to output — so nothing clips and nothing is too quiet. Fundamental to good sound.

**Headroom**
The margin between the nominal operating level and the point of clipping/distortion.

**Unity Gain**
The point where output level equals input level (no boost or cut).

**Trim / Gain Knob**
Preamp control that sets the initial input level from a mic or line source.

**Fader**
Slider controlling channel or bus level after gain staging.

**Bus**
A pathway that combines multiple channels into one output. Your Wing has 16 buses used for monitor mixes.

**Matrix**
An output that can receive from multiple buses. Used for complex routing like sending to delay speakers or broadcast feeds.

**Aux Send**
A separate output from a channel, typically used for monitors or effects. "Send" = signal going out to an effect; "return" = the processed signal coming back into the mix.

**Insert**
Putting an effect directly in-line in a channel's signal path, so all the signal passes through it — different from a send/return, which is parallel.

**Pre-fader (PRE)**
A signal tap point before the fader. Monitor mixes are usually pre-fader so the FOH engineer moving a fader doesn't affect the performer's monitor.

**Post-fader (POST)**
A signal tap point after the fader. Effects sends are often post-fader so they follow the channel level.

**Clipping**
Distortion caused by a signal exceeding the maximum level a device can handle.

**Signal-to-Noise Ratio (S/N)**
The ratio between the desired signal level and background noise.

### EQ (Equalization)

**EQ**
Adjusting the balance of frequency content in a signal.

**Parametric EQ**
EQ with adjustable frequency, gain, and bandwidth (Q) per band.

**Graphic EQ**
EQ with fixed frequency bands, each with a gain slider.

**Shelf (High/Low Shelf)**
A filter that boosts or cuts all frequencies above/below a set point.

**HPF — High-Pass Filter**
Cuts low frequencies below a set point; also called a low cut. Essential on nearly every vocal mic to remove rumble.

**LPF — Low-Pass Filter**
Cuts high frequencies above a set point; also called a high cut.

**Q (Bandwidth)**
Determines how narrow or wide an EQ band's effect is around its center frequency.

**Notch Filter**
A very narrow, steep cut used to remove a specific problem frequency (e.g., feedback or 60 Hz hum). The 60 Hz Hum Remover preset uses notches at 60, 180, 300, 420, and 540 Hz.

**Subtractive EQ**
Cutting unwanted frequencies rather than boosting desired ones; generally cleaner-sounding.

**Frequency Masking**
When overlapping frequencies from different sources compete and obscure each other.

### Dynamics

**Compression**
Reduces the dynamic range of a signal — makes loud parts quieter and/or quiet parts louder relative to each other. Essential for live vocals.

**Threshold**
The level at which a compressor or gate begins acting on the signal.

**Ratio**
How much gain reduction is applied once the signal crosses the threshold (e.g., 4:1).

**Attack**
How quickly a compressor/gate responds once the threshold is crossed.

**Release**
How quickly a compressor/gate stops acting after the signal falls back below threshold.

**Knee (Soft/Hard)**
How gradually or abruptly compression is applied around the threshold.

**Makeup Gain**
Gain added after compression to restore perceived loudness.

**Gain Reduction**
How much a compressor is working, measured in dB. More gain reduction = compressor working harder.

**Limiter**
A compressor with a very high ratio, used to prevent a signal from exceeding a ceiling.

**Noise Gate**
Mutes or attenuates a signal that falls below a set threshold, used to reduce bleed/noise.

**Expander**
Increases dynamic range by further attenuating signal below threshold (gentler than a gate).

**Sidechain**
Using one signal to control the dynamics processing applied to another (e.g., ducking).

### Time-Based & Modulation Effects

**Reverb**
Simulates the reflections of a physical space; adds depth and ambience.

**Delay**
Repeats a signal after a set time interval; can be short (slapback) or long (echo).

**Pre-Delay**
The gap before reverb reflections begin, used to preserve clarity of the initial transient.

**Chorus**
Modulation effect that thickens a sound by layering slightly detuned, delayed copies.

**Flanger**
Modulation effect using a very short, sweeping delay, creating a sweeping/jet-like sound.

**Phaser**
Modulation effect using phase-shifted copies, creating a swirling sound.

**Doubling**
Layering a near-identical, slightly delayed copy of a signal for thickness.

### Mics, DI & Connectors

**Dynamic Microphone**
Rugged mic type using a moving coil; handles high SPL well (e.g., SM58).

**Condenser Microphone**
Mic type using a charged diaphragm; more sensitive and detailed, requires phantom power.

**Phantom Power (+48V)**
DC voltage sent through an XLR cable to power condenser mics.

**Polar Pattern**
A mic's directional sensitivity (cardioid, omnidirectional, figure-8, etc.).

**Proximity Effect**
Bass boost that occurs as a directional mic gets closer to the source.

**DI — Direct Input / DI Box**
Converts a high-impedance instrument signal (like a bass guitar) to balanced mic level, without a microphone.

**XLR**
3-pin balanced connector standard for mics and pro audio.

**TRS / TS**
Tip-Ring-Sleeve (balanced/stereo) vs. Tip-Sleeve (unbalanced/mono) 1/4" connectors.

**Balanced Line**
Wiring scheme that cancels induced noise over long cable runs.

**Bleed**
Unwanted pickup of one source in another source's microphone.

### Console & Live Mixing Terms

**FOH — Front of House**
The main speaker system the audience hears. Also refers to the mix position/engineer.

**Monitor Mix**
A separate mix sent to performers' stage monitors or in-ears, independent of FOH.

**IEM — In-Ear Monitor**
Wireless earphones performers wear to hear their monitor mix on stage. You use Xvive U4 IEM systems.

**Wedge**
A traditional floor-standing stage monitor speaker.

**VCA — Voltage Controlled Amplifier / DCA — Digitally Controlled Amplifier**
A control that links multiple faders together so one master fader controls them proportionally, without summing audio (unlike a group bus). Essential for live mixing. Digital consoles (Behringer, DiGiCo, etc.) call this a DCA.

**Snapshot**
A complete saved state of a mixer at a moment in time. Load one and all settings jump to that configuration instantly.

**Scene**
Similar to a snapshot — a saved configuration. Different brands use the terms differently.

**Preset**
A saved configuration for a specific channel or effect, not the whole mixer — more granular than a snapshot.

**Panning**
Positioning a signal within the stereo (or surround) field.

**Solo (PFL/AFL)**
Monitoring a single channel in isolation, pre-fader (PFL) or after-fader (AFL).

**Mute Group**
A set of channels that can be muted together with one control.

**Gain Compensation**
Automatically adjusting downstream level when input trim is changed, to keep fader position meaningful.

**GPIO — General Purpose Input/Output**
Physical ports on the Wing Rack used to connect footswitches and other external controls. You use GPIO 1 for Leslie speed and GPIO 2 for FX kill.

### Digital Audio, Protocols & Networking

**OSC — Open Sound Control**
A network protocol for controlling audio equipment. Like MIDI but over a network and much more flexible. Your Wing Rack and XR18 both use OSC.

**MIDI — Musical Instrument Digital Interface**
The original music control protocol from 1983. Still widely used. Sends simple messages like "note on," "note off," "control change." Limited compared to OSC but universal.

**UDP — User Datagram Protocol**
A fast, lightweight network protocol. Doesn't confirm delivery — just sends and hopes it arrives. XR18 uses UDP for OSC. Fast but can drop packets.

**TCP — Transmission Control Protocol**
A reliable network protocol that confirms every packet was received. Slower than UDP but nothing gets lost. Wing Rack uses TCP for OSC.

**IP Address**
A unique address for a device on a network. Like a street address. Your Wing Rack has one (e.g., 192.168.1.100).

**Port**
A numbered "channel" within a network connection. Wing uses port 2223. XR18 uses port 10024. Like different doors on the same building.

**Subnet**
A segment of a network. Devices on the same subnet can talk to each other. Your Wing, XR18, and laptop need to be on the same subnet to communicate.

**DHCP**
Automatic IP address assignment. Your router does this by default. Static IP = you set it manually and it never changes.

**Latency**
The delay between an action (or input) and its result (or output). In audio, measured in milliseconds. Low latency = fast response = good.

**Buffer / Buffer Size**
A small memory area that temporarily holds audio data. Larger buffer = more latency but more stable. Smaller buffer = less latency but more CPU strain.

**DPC Latency — Deferred Procedure Call Latency**
A Windows-specific measure of how long system interrupts take. High DPC latency = audio dropouts. The main enemy of live audio on Windows laptops.

**Sample Rate**
How many audio samples per second. 44.1kHz = CD quality. 48kHz = standard for video/live. 96kHz = high resolution. Wing Rack runs at 96kHz.

**Bit Depth**
How much information each audio sample contains. 16-bit = CD. 24-bit = professional standard. 32-bit = mastering/archival.

**DSP — Digital Signal Processing**
The math that processes audio in real time. EQ, compression, reverb, delay — all DSP.

**FPGA — Field Programmable Gate Array**
A type of chip that can be reconfigured in hardware. Allen & Heath SQ uses FPGA for their ultra-low latency processing.

**Plugin**
Software that processes or generates audio inside a DAW or digital console.

**Sample-Accurate**
Timing precision down to the individual audio sample.

**AES50**
A digital audio networking standard used by Behringer/Midas for stage boxes. Your S32 connects to the Wing Rack via AES50.

**Dante**
A popular audio-over-IP networking standard. Many pro consoles support it via expansion cards.

**AVB — Audio Video Bridging**
An audio networking standard used by PreSonus StudioLive series. Requires AVB-compatible network switches.

**MADI**
A high channel count digital audio format. Used by DiGiCo and other high-end consoles for long cable runs.

### Monitoring & PA

**PA (Public Address) System**
The full sound reinforcement system delivering audio to an audience.

**Mains**
The primary loudspeakers covering the audience.

**Subwoofer (Sub)**
A speaker dedicated to low-frequency content.

**Feedback**
An audible loop caused when a mic picks up its own amplified sound.

**Coverage Pattern**
The horizontal/vertical spread of sound from a loudspeaker.

**Line Array**
A vertically stacked speaker system designed for controlled long-throw coverage.

### Mastering & Loudness

**LUFS — Loudness Units Full Scale**
A standardized measurement of perceived loudness.

**True Peak**
The actual peak level of a signal including inter-sample peaks, used to prevent clipping after conversion.

**Dynamic Range**
The difference between the loudest and quietest parts of a signal.

**Mix Bus Compression**
Light compression applied across the entire mix to glue elements together.

### Added October 2026

**Stage Box**
A box on stage that holds the mic inputs and outputs and sends everything to the console over one digital cable. Your Behringer S32 is a stage box connected to the Wing Rack by AES50.

**Firmware**
The software built into a piece of hardware, like a mixer or stage box. Updating firmware adds features and fixes bugs — keep the console and stage box on matching versions.

**Rider**
A document listing what a band needs from the venue or sound crew — inputs, monitors, gear, power, and sometimes hospitality. It can also act as an agreement between the band and the venue.

**Stage Plot**
A simple drawing showing where each musician, amp, mic, monitor, and power drop sits on stage. Often goes with the input list in the rider.

**DAW — Digital Audio Workstation**
Software for recording, editing, and mixing audio on a computer. Studio One and Cakewalk are DAWs.

**ASIO / ASIO4ALL**
ASIO is a Windows audio driver standard that gives music software low-latency access to your audio hardware. ASIO4ALL is a free, universal ASIO driver for devices that don't come with their own.

**UCNET**
PreSonus's private network protocol for controlling StudioLive mixers from computers and tablets. It isn't publicly documented, so apps have to reverse-engineer it.

**PreSonus StudioLive (32SC, etc.)**
PreSonus's line of digital mixers. The 32SC is a compact 32-channel model, like the one on the Musik Ink practice stage.

**Leslie Speaker**
A speaker cabinet with spinning horns that gives organ sounds a swirling, moving tone. Players switch between slow and fast rotation — your GPIO 1 footswitch toggles that speed.

**Harmonizer**
An effect that adds pitch-shifted copies of a voice to create instant harmony parts. The Boss VE-2 is one.

**Boundary Microphone**
A flat mic designed to lie on a surface like a floor, table, or inside a kick drum. The surface helps it pick up a fuller sound. The Behringer BA19A is one.

**Ground Loop / Hum Eliminator**
A ground loop happens when gear is grounded through more than one path, causing a low hum or buzz. A hum eliminator (like the Morley MHE2) breaks that loop on the audio line without removing safety ground.

**Power Conditioner**
A rack unit that distributes power to your gear and filters out electrical noise and spikes. The ART PB4x4 is one.

**SSID**
The name of a Wi-Fi network — what you see in the list when you connect. Using the same SSID and password on the router and all extenders lets devices move between them automatically.

**2.4 GHz vs. 5 GHz**
The two main Wi-Fi bands. 2.4 GHz reaches farther and goes through walls better but is slower and more crowded; 5 GHz is faster but shorter range. Many sound techs put the mixer on its own dedicated band for a steadier connection.

**Wi-Fi Extender**
A device that repeats a Wi-Fi signal to cover more area. Placement matters — mount it up high and in the open, not tucked on top of a fridge.

**Roaming**
When a phone, tablet, or laptop switches automatically from one Wi-Fi access point to a stronger one as you move around. Important when you're mixing from a tablet while walking the room.

**Guest Network**
A separate Wi-Fi network for visitors that keeps them away from your main devices, like the mixer and office computers.

**Driver**
Small software that lets Windows talk to a piece of hardware like an audio interface. Old or broken drivers are a common cause of crashes, dropouts, and devices not showing up.

**Memory Integrity (Core Isolation)**
A Windows security feature that blocks untrusted drivers from running deep inside the system. Old audio drivers may need to be removed before it can be turned on.

**Pitch Correction**
An effect that nudges off-key notes toward the correct pitch. Used lightly, it's barely noticeable; used heavily, you get the robotic 'Auto-Tune' sound.

**Multitrack Recording**
Recording each input to its own separate track so you can remix the show later. The WING-LIVE card records up to 64 channels to SD cards.

**Show File**
A complete save of the entire mixer state — all channels, buses, effects, routing, and settings. Load one and the console jumps to exactly how it was for that gig.

**Channel Preset (.chn)**
A Wing-format file that saves the settings for a single channel — EQ, compression, gate, effects, name. The 60 Hz Hum Remover is a `.chn` file.

**Signature Pack**
A curated collection of presets made by a specific engineer and shared or sold under their name.

**Waves SuperRack Performer**
Waves Audio's live plugin host. Runs studio-quality plugins (including third-party VST3) on a laptop connected to your mixer, without needing a dedicated server.

**Native Mode**
Running SuperRack on the laptop's own CPU, with no SoundGrid server. Simpler and cheaper, but performance depends on the computer.

**SoundGrid**
Waves' server-based audio processing network. Plugins run on dedicated hardware instead of the laptop — a separate setup from native SuperRack.

**LiveBox D**
A Windows hardware appliance from Waves, pre-configured to run SuperRack for live shows.

**VST3**
The current standard plugin format for audio software. SuperRack Performer can load third-party VST3 plugins.

**MKL Optimization (Waves)**
A Waves utility that fixes abnormally high CPU use when running Waves plugins on AMD processors. Run it as Administrator after installing SuperRack.

**PoE — Power over Ethernet**
Delivers power through a standard network cable, so a device like a camera or access point needs only one cable. Requires a PoE switch or injector.

**PTZ Camera — Pan/Tilt/Zoom**
A camera that can be aimed and zoomed remotely. Used for venue coverage and live streaming. Some have auto-tracking that can cause unexpected movement if left on.

### Business & Training

**Fog City Audio / Fog City Sound Works**
Rob's live sound consulting business, aimed at small bar and intimate venues.

**Audio Rockstars**
Rob's audio engineering training platform — taking people with little audio knowledge and building their skills fast.

---
*This glossary grows as the Soundman and Audio Rockstars projects develop.*
*Last updated: October 29, 2026*
*Next review: November 12, 2026*
