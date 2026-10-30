# Music / Audio Foundation Model Research Radar — 2026-10-30

> Lookback window: 2026-10-23 to 2026-10-30 · New papers: 10 · New models: 0 · relevant papers/models in window: 35/81 · raw papers/models: 149/357

Sources: arxiv=93 · semantic_scholar=56 · huggingface_models=357

## Research signals

- Speech Generation, Recognition & Dialogue: 4 papers
- Generative Music & Audio: 4 papers
- Audio & Speech Language Models: 3 papers
- Audio Understanding & Reasoning: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [Do Audio LLMs HEAR Pain? Tracing Acoustic Evidence from Speech to Language Reasoning](https://arxiv.org/abs/2610.38570) | 2026-10-28 | 20 | Audio & Speech Language Models | — |
| 2 | [Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis](https://arxiv.org/abs/2610.39168) | 2026-10-29 | 17 | Speech Generation, Recognition & Dialogue | — |
| 3 | [A Tutorial on Generative Models for Music Audio](https://arxiv.org/abs/2610.38252) | 2026-10-28 | 16 | Generative Music & Audio | — |
| 4 | [Pronunciation-Supervised Text-to-Speech for Irish (Gaeilge)](https://arxiv.org/abs/2610.38384) | 2026-10-28 | 14 | Speech Generation, Recognition & Dialogue | — |
| 5 | [DRC-TTS: A Dual-Resolution Codec-Based Architecture for Lexicon-Free Malay Speech Synthesis](https://arxiv.org/abs/2610.38316) | 2026-10-28 | 14 | Generative Music & Audio, Speech Generation, Recognition & Dialogue | — |
| 6 | [MixCards: Evaluating Structured Descriptions of Multi-Source Sound Scenes](https://arxiv.org/abs/2610.38276) | 2026-10-28 | 13 | Audio & Speech Language Models, Audio Understanding & Reasoning | [repo](https://github.com/Sound-Captioning-for-Accessibility/mixcardbench) |
| 7 | [SpeakerTurn: Target-Speaker Semantic Turn Detection in Multi-Speaker Environments](https://arxiv.org/abs/2610.39828) | 2026-10-29 | 6 | Audio & Speech Language Models | — |
| 8 | [SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization](https://arxiv.org/abs/2610.40640) | 2026-10-29 | 6 | Generative Music & Audio | — |
| 9 | [Partially Edited Audio: Generation, Defense, and Open Problems](https://arxiv.org/abs/2610.37640) | 2026-10-27 | 6 | Generative Music & Audio | — |
| 10 | [ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling](https://arxiv.org/abs/2610.36126) | 2026-10-26 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. Do Audio LLMs HEAR Pain? Tracing Acoustic Evidence from Speech to Language Reasoning

- **Authors**: Wenqi Li, Xiangjue Dong, Sulaiman Vesal
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 20 pts · Audio & Speech Language Models: audio language model, audio llm
- **Links**: [Paper](https://arxiv.org/abs/2610.38570) · [PDF](https://arxiv.org/pdf/2610.38570v1)

Large audio language models (LALMs) can process speech directly, but it remains unclear how well they use the non-lexical acoustic information that speech carries. We study this question through pain, using TAME-Pain, which contains pain-neutral Harvard sentences and spoken pain ratings recorded at different self-reported pain levels. We introduce HEAR, a four-stage diagnostic framework that traces pain-related…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis

- **Authors**: Cheng Zhang
- **Date / sources**: 2026-10-29 · arxiv
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: speech synthesis, automatic speech recognition, voice cloning
- **Links**: [Paper](https://arxiv.org/abs/2610.39168) · [PDF](https://arxiv.org/pdf/2610.39168v1)

Few-shot voice cloning makes it cheap to produce daily Japanese financial commentary with several synthetic speakers, but kanji words with more than one reading, such as the word for "market" (shijo vs. ichiba) or "overall trend" (taisei vs. oze), are still misread. A common quality gate transcribes each synthesized sentence with automatic speech recognition (ASR), converts both the input and the transcript to kana,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. A Tutorial on Generative Models for Music Audio

- **Authors**: Mateusz Modrzejewski, Joanna Kurkowska, Dorien Herremans
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 16 pts · Generative Music & Audio: music generation, audio generation, neural audio codec
- **Links**: [Paper](https://arxiv.org/abs/2610.38252) · [PDF](https://arxiv.org/pdf/2610.38252v1)

Music audio generation spans instrumental clips, full songs with vocals, edits of existing recordings, and systems that play alongside a musician in real time. This monograph explains the methods behind these systems for readers familiar with neural-network training who are new to music generation. It introduces neural audio codecs and autoencoders, autoregressive and masked token models, diffusion and flow…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Pronunciation-Supervised Text-to-Speech for Irish (Gaeilge)

- **Authors**: William Lane
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 14 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech
- **Links**: [Paper](https://arxiv.org/abs/2610.38384) · [PDF](https://arxiv.org/pdf/2610.38384v1)

Speech technology for Irish must be built from very little transcribed speech, yet the language's pronunciation is thoroughly documented in dictionaries and dialect descriptions. We ask whether that documentation can supervise the adaptation of a large pretrained text-to-speech model to a language it was never trained on. We adapt Qwen3-TTS to Irish using 12.8 hours of crowdsourced Common Voice speech, correcting…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. DRC-TTS: A Dual-Resolution Codec-Based Architecture for Lexicon-Free Malay Speech Synthesis

- **Authors**: Tianhui Su, Tien-Ping Tan
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 14 pts · Speech Generation, Recognition & Dialogue: speech synthesis; Generative Music & Audio: neural audio codec
- **Links**: [Paper](https://arxiv.org/abs/2610.38316) · [PDF](https://arxiv.org/pdf/2610.38316v1)

Modern discrete neural audio codecs facilitate speech synthesis by replacing continuous acoustic representations with low-frame-rate discrete token sequences. For Malay speech synthesis, character-level input reduces reliance on pronunciation lexicons. However, combining character-level inputs with low-frame-rate discrete codecs introduces a temporal alignment challenge. When predicted character durations are…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. MixCards: Evaluating Structured Descriptions of Multi-Source Sound Scenes

- **Authors**: Sripathi Sridhar, Yujin Kim, Giovana Morais, Liang-Yuan Wu, Mehmet Atilay Kucukoglu, Prem Seetharaman, Lloyd May, Mark Cartwright et al.
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 13 pts · Audio & Speech Language Models: audio language model; Audio Understanding & Reasoning: audio captioning; has open-source code link
- **Links**: [Paper](https://arxiv.org/abs/2610.38276) · [PDF](https://arxiv.org/pdf/2610.38276v1) · [Code 1](https://github.com/Sound-Captioning-for-Accessibility/mixcardbench)

Audio captioning benchmarks typically evaluate a single unstructured free-text description of an audio scene, providing limited insight into how a model fails to understand polyphonic audio. A plausible caption may omit a source, or conflate multiple sources into one, or assign an attribute of one source to another, and conventional captioning evaluation cannot locate these errors. We introduce MixCardBench, a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. SpeakerTurn: Target-Speaker Semantic Turn Detection in Multi-Speaker Environments

- **Authors**: Nan Li, Hetao Shan, Jintao Liang, Jiahao Yan, Longbiao Wang, Tubin Huang, Min Xu
- **Date / sources**: 2026-10-29 · arxiv
- **Relevance**: 6 pts · Audio & Speech Language Models: speech language model
- **Links**: [Paper](https://arxiv.org/abs/2610.39828) · [PDF](https://arxiv.org/pdf/2610.39828v1)

Semantic completeness alone cannot determine when an assistant should respond in a multi-speaker environment: a completed utterance may belong to an interfering speaker, while the designated user is still speaking, acknowledging, or requesting time. We therefore study semantic turn inference conditioned on speaker identity. We propose SpeakerTurn, a framework that jointly predicts the target transcript and turn…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization

- **Authors**: Derong Jin, Xiyi Chen, Ming C. Lin, Ruohan Gao
- **Date / sources**: 2026-10-29 · arxiv
- **Relevance**: 6 pts · Generative Music & Audio: audio diffusion
- **Links**: [Paper](https://arxiv.org/abs/2610.40640) · [PDF](https://arxiv.org/pdf/2610.40640v1)

Recent progress in visual scene generation has extended beyond static 3D scenes toward the more challenging problem of generating dynamic 4D scenes from minimal input. However, sound, despite being intrinsically coupled with dynamic objects and events, remains largely unmodeled in prior work. We introduce Video-to-4DAVScene, a new task that turns a video into an explorable, time-varying 4D audio-visual scene, and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. Partially Edited Audio: Generation, Defense, and Open Problems

- **Authors**: Lin Zhang, You Zhang, Nicholas Evans, Xin Wang, David Harwath, Abhinav Dhall, Bowen Shi, Chengzhe Sun et al.
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Generative Music & Audio: audio generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.37640) · [PDF](https://arxiv.org/pdf/2610.37640v1)

Recent advances in generative audio models facilitate increasingly flexible and selective editing of linguistic content and paralinguistic, extralinguistic, and other attributes. This paradigm, named partially edited audio, differs from full audio generation as only portions of the real recording are edited. This technique can serve both beneficial and harmful applications. We therefore present a concise survey from…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling

- **Authors**: Kehinde Elelu, Joshua E. Siegel, Mohammadali Saffary, Tashfain Ahmed, Simeon Babatunde, Ebuka Okpala
- **Date / sources**: 2026-10-26 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.36126) · [PDF](https://arxiv.org/pdf/2610.36126v1)

Accurate prediction of human Mean Opinion Scores (MOS) is crucial for evaluating synthetic speech quality in text-to-speech (TTS) and voice conversion (VC). Most MOS predictors output only point estimates and ignore uncertainty, limiting reliability in model selection and deployment. We propose ConformalMOS, a framework that augments MOS prediction with conformal prediction to produce statistically valid prediction…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
