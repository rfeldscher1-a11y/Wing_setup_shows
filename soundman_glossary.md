# AI, Tech & Audio Dev Glossary
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

**API — Application Programming Interface**
(See Part 1) In app development specifically: the way your app talks to external services or hardware like the Wing Rack.

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

---

## PART 3 — Audio & OSC Protocol Terms
*(The technical side of talking to your mixers)*

**OSC — Open Sound Control**
A network protocol for controlling audio equipment. Like MIDI but over a network and much more flexible. Your Wing Rack and XR18 both use OSC.

**MIDI — Musical Instrument Digital Interface**
The original music control protocol from 1983. Still widely used. Sends simple messages like "note on", "note off", "control change". Limited compared to OSC but universal.

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
The delay between an action and its result. In audio, measured in milliseconds. Low latency = fast response = good.

**Buffer**
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

**AES50**
A digital audio networking standard used by Behringer/Midas for stage boxes. Your S32 connects to the Wing Rack via AES50.

**Dante**
A popular audio-over-IP networking standard. Many pro consoles support it via expansion cards.

**AVB — Audio Video Bridging**
An audio networking standard used by PreSonus StudioLive series. Requires AVB-compatible network switches.

**MADI**
A high channel count digital audio format. Used by DiGiCo and other high-end consoles for long cable runs.

**Snapshot**
A complete saved state of a mixer at a moment in time. Load a snapshot and all settings jump to that configuration instantly.

**Scene**
Similar to a snapshot — a saved configuration. Different brands use the terms differently.

**Preset**
A saved configuration for a specific channel or effect, not the whole mixer. More granular than a snapshot.

**VCA — Voltage Controlled Amplifier**
In digital mixing, a VCA group links multiple faders so one master fader controls them all proportionally. Essential for live mixing.

**DCA — Digitally Controlled Amplifier**
Same concept as VCA but in digital mixers. Behringer, DiGiCo etc. use DCA groups.

**Gain Structure**
Setting proper levels at every stage of the signal path so nothing clips and nothing is too quiet. Fundamental to good sound.

**Phantom Power (+48V)**
Power sent through an XLR cable to power condenser microphones. The +48V you see on mic channels.

**HPF — High Pass Filter**
Cuts low frequencies below a set point. Also called a low cut filter. Essential on every vocal mic to remove rumble.

**LPF — Low Pass Filter**
Cuts high frequencies above a set point. Also called a high cut filter.

**Compression**
Reduces the dynamic range of audio — makes loud parts quieter and/or quiet parts louder. Essential for live vocals.

**Gain Reduction**
How much a compressor is working. Measured in dB. More gain reduction = compressor working harder.

**Send / Return**
How effects are connected in a mixer. You "send" signal from a channel to an effect, and the effect "returns" processed signal back into the mix.

**Insert**
Putting an effect directly in the signal path of a channel, so all the signal goes through it. Different from a send/return.

**Bus**
A pathway that combines multiple channels into one output. Your Wing has 16 buses used for monitor mixes.

**Matrix**
An output that can receive from multiple buses. Used for complex routing like sending to delay speakers or broadcast feeds.

**DI — Direct Input**
Connecting an instrument (like a bass guitar) directly to the mixer without a microphone, using a DI box.

**PRE — Pre-fader**
A signal tap point before the fader. Monitor mixes are pre-fader so the FOH engineer moving a fader doesn't affect the performer's monitor.

**POST — Post-fader**
A signal tap point after the fader. Effects sends are often post-fader so they follow the channel level.

**FOH — Front of House**
The main speaker system the audience hears. Also refers to the mix position where the engineer sits.

**IEM — In-Ear Monitor**
Wireless earphones performers wear to hear their monitor mix on stage. You have Xvive U4 IEM systems.

**GPIO — General Purpose Input/Output**
Physical ports on the Wing Rack used to connect footswitches and other external controls. You use GPIO 1 for Leslie speed and GPIO 2 for FX kill.

---

*This glossary will grow as the Soundman project develops.*
*Last updated: May 2026*
