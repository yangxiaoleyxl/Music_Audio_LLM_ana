# Music / Audio Foundation Model Research Radar — 2026-11-14

> Lookback window: 2026-11-07 to 2026-11-14 · New papers: 13 · New models: 12 · relevant papers/models in window: 70/56 · raw papers/models: 182/315

Sources: arxiv=86 · semantic_scholar=96 · huggingface_models=315

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [arpanpathak/staleynet-checkpoints](https://huggingface.co/arpanpathak/staleynet-checkpoints) | 2026-11-14 | text-to-audio | 42 | 1 | 0 | 2 | cc-by-sa-4.0 |
| 2 | [mahmoudalyosify/BA](https://huggingface.co/mahmoudalyosify/BA) | 2026-11-14 | text-to-speech | 36 | 1 | 18 | 0 | other |
| 3 | [D3rPapst/moss-music-8b-gufo](https://huggingface.co/D3rPapst/moss-music-8b-gufo) | 2026-11-13 | audio-text-to-text | 35 | 1 | 29 | 0 | apache-2.0 |
| 4 | [infosave/Haru-4B-cmf](https://huggingface.co/infosave/Haru-4B-cmf) | 2026-11-14 | audio-to-audio | 27 | 1 | 0 | 0 | apache-2.0 |
| 5 | [zhaoyx39/S3-S2ST](https://huggingface.co/zhaoyx39/S3-S2ST) | 2026-11-14 | audio-to-audio | 22 | 1 | 0 | 2 | unknown |
| 6 | [berrkkaayy/IndexTTS-2.5-Turkish-LoRA](https://huggingface.co/berrkkaayy/IndexTTS-2.5-Turkish-LoRA) | 2026-11-14 | text-to-speech | 17 | 1 | 0 | 4 | other |
| 7 | [Tree-AI-lab/tts-accent-ivoirien-noushi-franco-bete](https://huggingface.co/Tree-AI-lab/tts-accent-ivoirien-noushi-franco-bete) | 2026-11-14 | text-to-speech | 15 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 8 | [LiquidAI/d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B) | 2026-11-14 | audio-text-to-text | 14 | 1 | 4843 | 110 | other |
| 9 | [notmax123/blue-codec](https://huggingface.co/notmax123/blue-codec) | 2026-11-14 | text-to-speech | 11 | 1 | 0 | 1 | mit |
| 10 | [adwumatech-ai/nebula-st-twi-en](https://huggingface.co/adwumatech-ai/nebula-st-twi-en) | 2026-11-14 | automatic-speech-recognition | 10 | 1 | 233 | 1 | cc-by-4.0 |
| 11 | [huybik/hibiki-zero-vi-full-sft](https://huggingface.co/huybik/hibiki-zero-vi-full-sft) | 2026-11-14 | audio-to-audio | 9 | 1 | 0 | 1 | cc-by-nc-sa-4.0 |
| 12 | [lvndry/drone](https://huggingface.co/lvndry/drone) | 2026-11-14 | audio-classification | 7 | 1 | 0 | 0 | mit |

### Model cards

#### M1. arpanpathak/staleynet-checkpoints

- **Created / updated**: 2026-11-04 / 2026-11-14
- **Task / library**: text-to-audio / unknown
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license cc-by-sa-4.0
- **Adoption signals**: downloads=0 · likes=2 · trending=0.0
- **License / access**: cc-by-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M2. mahmoudalyosify/BA

- **Created / updated**: 2026-11-12 / 2026-11-14
- **Task / library**: text-to-speech / unknown
- **Relevance**: 36 pts · Speech Generation, Recognition & Dialogue: speech generation, text-to-speech (pipeline tag), voice cloning; Evaluation, Alignment, Safety & Copyright: audio watermarking; model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=18 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2509.24650](https://arxiv.org/abs/2509.24650) · [arXiv:2212.04356](https://arxiv.org/abs/2212.04356) · [arXiv:2205.12446](https://arxiv.org/abs/2205.12446)
- **Datasets / base models**: unknown / openbmb/VoxCPM2
- **Variants in family**: —

#### M3. D3rPapst/moss-music-8b-gufo

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-text-to-text / gufo
- **Relevance**: 35 pts · Audio & Speech Language Models: audio language model, audio-language model; Music Foundation Models & Representations: music understanding; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=29 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / OpenMOSS-Team/MOSS-Music-8B-Instruct
- **Variants in family**: —

#### M4. infosave/Haru-4B-cmf

- **Created / updated**: 2026-11-14 / 2026-11-14
- **Task / library**: audio-to-audio / cortiq
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / higurashi-ai/Haru-4B
- **Variants in family**: —

#### M5. zhaoyx39/S3-S2ST

- **Created / updated**: 2026-11-11 / 2026-11-14
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 22 pts · Speech Generation, Recognition & Dialogue: speech translation, speech-to-speech; model card links an arXiv paper
- **Adoption signals**: downloads=0 · likes=2 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: [arXiv:2610.36777](https://arxiv.org/abs/2610.36777)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M6. berrkkaayy/IndexTTS-2.5-Turkish-LoRA

- **Created / updated**: 2026-08-19 / 2026-11-14
- **Task / library**: text-to-speech / indextts
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=0 · likes=4 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2601.03888](https://arxiv.org/abs/2601.03888) · [arXiv:2607.09530](https://arxiv.org/abs/2607.09530)
- **Datasets / base models**: freyavoice/freya-tr-eval, cloud0day3/alania-synthetic-speech-tr / IndexTeam/IndexTTS-2.5
- **Variants in family**: —

#### M7. Tree-AI-lab/tts-accent-ivoirien-noushi-franco-bete

- **Created / updated**: 2026-11-14 / 2026-11-14
- **Task / library**: text-to-speech / coqui-tts
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / coqui/XTTS-v2
- **Variants in family**: —

#### M8. LiquidAI/d1-Omni-2B

- **Created / updated**: 2026-10-24 / 2026-11-14
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 14 pts · Audio Understanding & Reasoning: audio-text (pipeline tag), multimodal audio; declares license other; community likes 110
- **Adoption signals**: downloads=4843 · likes=110 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / LiquidAI/LFM3-Omni-2B
- **Variants in family**: —

#### M9. notmax123/blue-codec

- **Created / updated**: 2026-04-09 / 2026-11-14
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license mit
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M10. adwumatech-ai/nebula-st-twi-en

- **Created / updated**: 2026-11-09 / 2026-11-14
- **Task / library**: automatic-speech-recognition / unknown
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license cc-by-4.0
- **Adoption signals**: downloads=233 · likes=1 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M11. huybik/hibiki-zero-vi-full-sft

- **Created / updated**: 2026-07-29 / 2026-11-14
- **Task / library**: audio-to-audio / moshi
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: speech translation; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/hibiki-zero-3b-pytorch-bf16
- **Variants in family**: —

#### M12. lvndry/drone

- **Created / updated**: 2026-11-11 / 2026-11-14
- **Task / library**: audio-classification / pytorch
- **Relevance**: 7 pts · Music Foundation Models & Representations: music information retrieval; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

## Research signals

- Speech Generation, Recognition & Dialogue: 9 papers
- Generative Music & Audio: 3 papers
- Audio & Speech Language Models: 2 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [TeleSound-Codec: High-Fidelity General Audio Coding Under 1kbps via Language-Grounded Supervision and Scalable Generative Modeling](https://www.semanticscholar.org/paper/1ecabb30a343a0cae9ac293bd37ac70aa5767063) | 2026-11-09 | 13 | Audio & Speech Language Models, Generative Music & Audio | — |
| 2 | [Active Acoustic Probes for AI Voice Call Detection](https://www.semanticscholar.org/paper/84f734a317bdb7352b3542031ad311d96cf1fcbc) | 2026-11-14 | 12 | Speech Generation, Recognition & Dialogue | — |
| 3 | ["It Scams In The Family:" GenAI Voice Cloning Scams among Sighted and Families with Blind or Low Vision Members](https://www.semanticscholar.org/paper/5b5d29930194f07366c9006a31f6a8263870add1) | 2026-11-14 | 12 | Speech Generation, Recognition & Dialogue | — |
| 4 | [Beyond Known Speakers: Enhancing Spoofing Detection Generalization with VIVED](https://www.semanticscholar.org/paper/9a509cd80a08fd0abf54e3f7e8e32acfacb1a6bb) | 2026-11-14 | 10 | Speech Generation, Recognition & Dialogue | — |
| 5 | [An Interactive Desktop Application for Human Gesture-Controlled Music Generation Using Deep Learning-Based Hand Tracking](https://www.semanticscholar.org/paper/bced382b956a4cd0f507559f6554901556b8b885) | 2026-11-11 | 10 | Generative Music & Audio | — |
| 6 | [Students’ Choice of Spanish Text and Text-To-Speech on Items on a Large-Scale Mathematics Achievement Test](https://www.semanticscholar.org/paper/cb6f12a616caaa9c9667a889bf08357db11ca952) | 2026-11-10 | 10 | Speech Generation, Recognition & Dialogue | — |
| 7 | [A Language-Routed Speech-to-Action Framework for Code-Switched Indic Voice Assistants](https://www.semanticscholar.org/paper/4a59c74143dbc6975241358431c3f6e3a3ad675b) | 2026-11-11 | 8 | Speech Generation, Recognition & Dialogue | — |
| 8 | [PodEval: A Multimodal Evaluation Framework for Long-form Podcast Generation](https://www.semanticscholar.org/paper/cce9276afebc8990e67ddba628911f64aad956aa) | 2026-11-09 | 7 | Generative Music & Audio | [repo](https://github.com/yujxx/PodEval) |
| 9 | [Bat Vocalization Explorer: An Interactive, Leakage-Controlled Tool for Decoding Behavioural Context from Egyptian Fruit Bat Calls](https://www.semanticscholar.org/paper/26229bfc69d4a72773e712c8787068e0197d3ead) | 2026-11-09 | 7 | Audio & Speech Language Models | — |
| 10 | [Explaining Suspicious Speech Beyond Binary Deepfake Detection: A Five-Module Proposition-Centered Evidence Profile](https://www.semanticscholar.org/paper/16317f364146748cd12658a783d681b87aff254b) | 2026-11-14 | 6 | Speech Generation, Recognition & Dialogue | — |
| 11 | [Multi-criteria ranking of open automatic speech recognition models under alternative deployment priorities](https://www.semanticscholar.org/paper/117168fb1641f383b278b4ce3c4800f7c1b59890) | 2026-11-12 | 6 | Speech Generation, Recognition & Dialogue | — |
| 12 | [Reliability-aware tone–segment learning for weakly supervised Southern Min automatic speech recognition](https://www.semanticscholar.org/paper/a4db9d29354a68cfe5dde7e4003cfb2e3d02fe3c) | 2026-11-11 | 6 | Speech Generation, Recognition & Dialogue | — |
| 13 | [Human-Likeness and Conversational Preference Diverge for Synthesized Agent Speech in Customer-Service Calls](https://arxiv.org/abs/2611.16051) | 2026-11-11 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. TeleSound-Codec: High-Fidelity General Audio Coding Under 1kbps via Language-Grounded Supervision and Scalable Generative Modeling

- **Authors**: Hao Ma, Rui-Hao Jing, Shan-Song Liu, Cheng Gong, Chi Zhang, Xiao-Lei Zhang, Xue-Long Li
- **Date / sources**: 2026-11-09 · semantic_scholar
- **Relevance**: 13 pts · Audio & Speech Language Models: audio-language model; Generative Music & Audio: neural audio codec
- **Links**: [Paper](https://www.semanticscholar.org/paper/1ecabb30a343a0cae9ac293bd37ac70aa5767063) · [PDF](https://doi.org/10.1145/3767308.3836568)

High-fidelity general audio coding at ultra-low bitrates is crucial for applications ranging from low-bandwidth communication to audio-language modeling. However, existing neural audio codecs struggle under extreme bitrate constraints, exhibiting degraded performance: weak semantic alignment leads to semantic distortion, while limited generative capacity compromises acoustic fidelity. To address these challenges, we…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. Active Acoustic Probes for AI Voice Call Detection

- **Authors**: Lior Yasur, Yisroel Mirsky
- **Date / sources**: 2026-11-14 · semantic_scholar
- **Relevance**: 12 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech
- **Links**: [Paper](https://www.semanticscholar.org/paper/84f734a317bdb7352b3542031ad311d96cf1fcbc) · [PDF](https://doi.org/10.1145/3843205.3845633)

AI voice calls are making it increasingly practical to impersonate people during live audio conversations, whether through voice cloning, real-time conversion, or autonomous voice agents. Current defenses remain mostly passive: they inspect received audio for artifacts created by current generators, which locks defenders into an arms race structurally favoring the attacker. Active defenses invert this dynamic by…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. "It Scams In The Family:" GenAI Voice Cloning Scams among Sighted and Families with Blind or Low Vision Members

- **Authors**: Filipo Sharevski, Jennifer Vander Loop
- **Date / sources**: 2026-11-14 · semantic_scholar
- **Relevance**: 12 pts · Speech Generation, Recognition & Dialogue: voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/5b5d29930194f07366c9006a31f6a8263870add1) · [PDF](https://doi.org/10.1145/3830454.3846559)

The usual victim in phone scams is an individual at risk of being defrauded or whose identity might be stolen. But a new scamming scheme has emerged, targeting families as victims instead - an individual at risk of being defrauded through an emergency request, voiced by a clone of a related individual whose voice identity has been non-consensually sampled. As these scams are harmful both to the well-being and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Beyond Known Speakers: Enhancing Spoofing Detection Generalization with VIVED

- **Authors**: Wen-Bin Wang, Zi Xing, Mukesh Prasad, J. Lipman, Sanjay Jha
- **Date / sources**: 2026-11-14 · semantic_scholar
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: speech synthesis, voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/9a509cd80a08fd0abf54e3f7e8e32acfacb1a6bb) · [PDF](https://doi.org/10.1145/3843205.3845632)

Recent speech synthesis systems have moved beyond conventional voice cloning toward the generation of expressive, text-described virtual identities. This shift creates a generalization challenge for spoofing countermeasures trained primarily on cloned speech from a limited pool of reference speakers and relatively neutral read-speech content. We introduce Virtual Identities with Varied Emotional Dynamics (VIVED), a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. An Interactive Desktop Application for Human Gesture-Controlled Music Generation Using Deep Learning-Based Hand Tracking

- **Authors**: Marius-Valentin Drăgoi, Răzvan-Andrei Timofte, Iuliana Marin, C. Cristoiu
- **Date / sources**: 2026-11-11 · semantic_scholar
- **Relevance**: 10 pts · Generative Music & Audio: music generation
- **Links**: [Paper](https://www.semanticscholar.org/paper/bced382b956a4cd0f507559f6554901556b8b885) · [PDF](https://doi.org/10.3390/technologies14110747)

This paper presents an interactive desktop application for human gesture-controlled music generation. The system uses a standard webcam and deep learning-based hand tracking to detect both hands and convert hand features into musical control actions. The application was developed in Python and uses OpenCV, MediaPipe, FluidSynth, MIDI synthesis, and WAV stem playback. It provides three modes. Free Play lets the user…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. Students’ Choice of Spanish Text and Text-To-Speech on Items on a Large-Scale Mathematics Achievement Test

- **Authors**: H. Buzick
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: text-to-speech
- **Links**: [Paper](https://www.semanticscholar.org/paper/cb6f12a616caaa9c9667a889bf08357db11ca952)

No abstract

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. A Language-Routed Speech-to-Action Framework for Code-Switched Indic Voice Assistants

- **Authors**: Shubham Pankaj Badhe, Kabeer Ahmed Merchant, Shreyas Nishad Deshmukh, Shravani Bankar, M. Atre
- **Date / sources**: 2026-11-11 · semantic_scholar
- **Relevance**: 8 pts · Speech Generation, Recognition & Dialogue: text-to-speech, automatic speech recognition
- **Links**: [Paper](https://www.semanticscholar.org/paper/4a59c74143dbc6975241358431c3f6e3a3ad675b) · [PDF](https://doi.org/10.36548/jucct.2026.4.009)

There are 22 Scheduled Languages in India, along with code-switching, and accents in different dialects make voice the most viable medium for many users of digital public services. There have been remarkable strides in Automatic Speech Recognition (ASR) technology for Indic languages, but most assessments are still limited to word error rate (WER). Conversely, LLM agents rely on clean input text and thus conceal the…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. PodEval: A Multimodal Evaluation Framework for Long-form Podcast Generation

- **Authors**: Yu-Jia Xiao, Liu-Meng Xue, Lei He, Xin-Yi Chen, Aemon Yat Fei Chiu, Wen-Jie Tian, Shao-Fei Zhang, Qiu-Qiang Kong et al.
- **Date / sources**: 2026-11-09 · semantic_scholar
- **Relevance**: 7 pts · Generative Music & Audio: audio generation; has open-source code link
- **Links**: [Paper](https://www.semanticscholar.org/paper/cce9276afebc8990e67ddba628911f64aad956aa) · [PDF](https://doi.org/10.1145/3767308.3835931) · [Code 1](https://github.com/yujxx/PodEval)

Recently, an increasing number of multimodal (text and audio) benchmarks have emerged, primarily focusing on evaluating models' understanding capability. However, exploration into assessing generative capabilities remains limited, especially for open-ended long-form content generation. Significant challenges lie in no reference standard answer, no unified evaluation metrics and uncontrollable human judgments. In…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. Bat Vocalization Explorer: An Interactive, Leakage-Controlled Tool for Decoding Behavioural Context from Egyptian Fruit Bat Calls

- **Authors**: Orkhan Kazymov, Ilya Makarov
- **Date / sources**: 2026-11-09 · semantic_scholar
- **Relevance**: 7 pts · Audio & Speech Language Models: audio foundation model
- **Links**: [Paper](https://www.semanticscholar.org/paper/26229bfc69d4a72773e712c8787068e0197d3ead) · [PDF](https://doi.org/10.1145/3767308.3839007)

We present Bat Vocalization Explorer, an interactive system that demonstrates how discrete tokenization and a simple linear probe decode behavioural context from the vocalizations of Egyptian fruit bats ( Rousettus aegyptiacus ). The tool makes a leakage-controlled companion study tangible to a live audience through (i) a leakage-controlled evaluation---context macro-F1 across in-individual versus held-out…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. Explaining Suspicious Speech Beyond Binary Deepfake Detection: A Five-Module Proposition-Centered Evidence Profile

- **Authors**: Thien-Phuc Doan, Woongjae Lee, Inho Kim, An Thien Nguyen, Souhwan Jung
- **Date / sources**: 2026-11-14 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/16317f364146748cd12658a783d681b87aff254b) · [PDF](https://doi.org/10.1145/3843205.3845626)

Current deepfake detectors answer only one question: whether a recording sounds synthetic. This is insufficient for forensic analysis because replay, compression, degradation, or voice cloning can hide synthetic artifacts or preserve speaker identity. As a result, one authenticity score may be incomplete or misleading. We propose a proposition-centered evidence profile that examines five questions separately:…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 11. Multi-criteria ranking of open automatic speech recognition models under alternative deployment priorities

- **Authors**: O. Bafail, Adnan Miski
- **Date / sources**: 2026-11-12 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition
- **Links**: [Paper](https://www.semanticscholar.org/paper/117168fb1641f383b278b4ce3c4800f7c1b59890) · [PDF](https://www.nature.com/articles/s41598-026-78831-5_reference.pdf)

Automatic speech recognition (ASR) models differ in accuracy, throughput, and parameter count, so choosing a model involves trade-offs. This study ranks 69 license-eligible open ASR model configurations from the July 2026 open ASR leaderboard, which covers eight short-form English test sets. Criterion weights were derived with the fuzzy analytic hierarchy process (fuzzy AHP) under three illustrative scenarios, each…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 12. Reliability-aware tone–segment learning for weakly supervised Southern Min automatic speech recognition

- **Authors**: Ya-Ping Qiu, Wei-Hua Pan, Qi-Hua Pan, Peng-Hao Yao
- **Date / sources**: 2026-11-11 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition
- **Links**: [Paper](https://www.semanticscholar.org/paper/a4db9d29354a68cfe5dde7e4003cfb2e3d02fe3c) · [PDF](https://www.nature.com/articles/s41598-026-80505-1_reference.pdf)

Southern Min automatic speech recognition (ASR) is challenged by non-verbatim Mandarin subtitles, unreliable pseudo-transcripts, tone-related acoustic variation, and programme-dependent domain shift. We propose the Southern Min Reliability-Bridging Automatic Speech Recognition framework (MinBridge-ASR), organized around two core mechanisms: cross-scale reliability bridging and branch-selective tone–segment learning.…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 13. Human-Likeness and Conversational Preference Diverge for Synthesized Agent Speech in Customer-Service Calls

- **Authors**: Jeffrey M. Girard, Antony D'Avirro, Jason Z. Zheng, Jacqueline R. Vertino, Benjamin Peloquin
- **Date / sources**: 2026-11-11 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.16051) · [PDF](https://arxiv.org/pdf/2611.16051v1)

Listeners can judge an agent's speech on how human it sounds (human-likeness) and on how much they would want to talk to it (conversational preference). Listening tests rarely ask about conversational preference, so the relation between the two judgments is unclear. We compared them in paired-choice tests on 120 turns that actors improvised as customer-service representatives. On each trial, two agents spoke the…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
