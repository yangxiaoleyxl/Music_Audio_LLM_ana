# Music / Audio Foundation Model Research Radar — 2026-11-19

> Lookback window: 2026-11-12 to 2026-11-19 · New papers: 5 · New models: 22 · relevant papers/models in window: 34/47 · raw papers/models: 139/346

Sources: arxiv=79 · semantic_scholar=60 · huggingface_models=346

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [coinnoin/YuE2-in-Google-Colab](https://huggingface.co/coinnoin/YuE2-in-Google-Colab) | 2026-11-19 | text-to-audio | 74 | 1 | 0 | 0 | other |
| 2 | [HeartMuLa/MuLaCover](https://huggingface.co/HeartMuLa/MuLaCover) | 2026-11-19 | audio-to-audio | 40 | 1 | 779 | 50 | cc-by-nc-4.0 |
| 3 | [ntc-ai/minimax-music3-particle-sliders](https://huggingface.co/ntc-ai/minimax-music3-particle-sliders) | 2026-11-19 | text-to-audio | 38 | 1 | 0 | 21 | mit |
| 4 | [JinchuanTian/LongCap-35B-A3B-FP8](https://huggingface.co/JinchuanTian/LongCap-35B-A3B-FP8) | 2026-11-19 | audio-text-to-text | 27 | 1 | 87 | 3 | apache-2.0 |
| 5 | [JinchuanTian/LongCap-35B-A3B](https://huggingface.co/JinchuanTian/LongCap-35B-A3B) | 2026-11-19 | audio-text-to-text | 27 | 1 | 100 | 1 | apache-2.0 |
| 6 | [nesoai-qa-org/higurashi-ai-Haru-4B](https://huggingface.co/nesoai-qa-org/higurashi-ai-Haru-4B) | 2026-11-19 | audio-to-audio | 27 | 1 | 0 | 0 | apache-2.0 |
| 7 | [Microguy1/Haru-4B-DUPLI](https://huggingface.co/Microguy1/Haru-4B-DUPLI) | 2026-11-19 | audio-to-audio | 27 | 1 | 0 | 0 | apache-2.0 |
| 8 | [TheStinger/Ilaria_RVC](https://huggingface.co/TheStinger/Ilaria_RVC) | 2026-11-19 | audio-to-audio | 21 | 1 | 0 | 1 | mit |
| 9 | [ntc-ai/yue2-particle-sliders](https://huggingface.co/ntc-ai/yue2-particle-sliders) | 2026-11-19 | text-to-audio | 20 | 1 | 0 | 22 | cc-by-nc-4.0 |
| 10 | [FireH2O/MrJMThaiTTS_CT](https://huggingface.co/FireH2O/MrJMThaiTTS_CT) | 2026-11-19 | text-to-speech | 17 | 1 | 0 | 0 | cc-by-sa-4.0 |
| 11 | [mehdi-hf/chatterbox-farsi](https://huggingface.co/mehdi-hf/chatterbox-farsi) | 2026-11-19 | text-to-speech | 16 | 1 | 0 | 52 | other |
| 12 | [ishiki-labs/ishiki-deepfake-0.5](https://huggingface.co/ishiki-labs/ishiki-deepfake-0.5) | 2026-11-19 | audio-classification | 15 | 1 | 17 | 1 | mit |
| 13 | [RetentionLabs/personaplex-7b-extended](https://huggingface.co/RetentionLabs/personaplex-7b-extended) | 2026-11-19 | audio-to-audio | 15 | 1 | 2 | 0 | other |
| 14 | [mimba/mimba-tune](https://huggingface.co/mimba/mimba-tune) | 2026-11-19 | text-to-audio | 14 | 1 | 0 | 0 | other |
| 15 | [neurarank/voice-ai-s2s](https://huggingface.co/neurarank/voice-ai-s2s) | 2026-11-19 | audio-to-audio | 13 | 1 | 109 | 0 | apache-2.0 |
| 16 | [hhhhaura/purplemusic-500k](https://huggingface.co/hhhhaura/purplemusic-500k) | 2026-11-19 | text-to-audio | 13 | 1 | 0 | 0 | unknown |
| 17 | [amosgyamfi/Sophon-Realtime-4B-Flash-CoreAI](https://huggingface.co/amosgyamfi/Sophon-Realtime-4B-Flash-CoreAI) | 2026-11-19 | audio-to-audio | 13 | 1 | 0 | 0 | apache-2.0 |
| 18 | [KaleComputer/kale-tts-1-nano](https://huggingface.co/KaleComputer/kale-tts-1-nano) | 2026-11-19 | text-to-speech | 11 | 1 | 129 | 0 | apache-2.0 |
| 19 | [rodbiren/kokoro_parakeet_aio_models](https://huggingface.co/rodbiren/kokoro_parakeet_aio_models) | 2026-11-19 | text-to-speech | 9 | 1 | 0 | 0 | other |
| 20 | [HeartMuLa/HeartMuLa-oss-3B](https://huggingface.co/HeartMuLa/HeartMuLa-oss-3B) | 2026-11-19 | text-to-audio | 7 | 1 | 779 | 262 | apache-2.0 |
| 21 | [HeartMuLa/HeartMuLa-oss-3B-happy-new-year](https://huggingface.co/HeartMuLa/HeartMuLa-oss-3B-happy-new-year) | 2026-11-19 | text-to-audio | 7 | 1 | 3158 | 67 | apache-2.0 |
| 22 | [litert-community/MediaPipe-AudioClassifier-YAMNet](https://huggingface.co/litert-community/MediaPipe-AudioClassifier-YAMNet) | 2026-11-19 | audio-classification | 7 | 1 | 0 | 0 | apache-2.0 |

### Model cards

#### M1. coinnoin/YuE2-in-Google-Colab

- **Created / updated**: 2026-11-19 / 2026-11-19
- **Task / library**: text-to-audio / unknown
- **Relevance**: 74 pts · Generative Music & Audio: text-to-music, text to music, music generation; Audio Understanding & Reasoning: audio understanding; Music Foundation Models & Representations: music information retrieval; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M2. HeartMuLa/MuLaCover

- **Created / updated**: 2026-09-14 / 2026-11-19
- **Task / library**: audio-to-audio / mulacover
- **Relevance**: 40 pts · Generative Music & Audio: text-to-music, text to music; Music Foundation Models & Representations: symbolic music; model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=779 · likes=50 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2601.10547](https://arxiv.org/abs/2601.10547)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M3. ntc-ai/minimax-music3-particle-sliders

- **Created / updated**: 2026-08-16 / 2026-11-19
- **Task / library**: text-to-audio / unknown
- **Relevance**: 38 pts · Generative Music & Audio: text-to-music, text to music, audio generation; declares license mit; community likes 21
- **Adoption signals**: downloads=0 · likes=21 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / MiniMaxAI/MiniMax-Music3
- **Variants in family**: —

#### M4. JinchuanTian/LongCap-35B-A3B-FP8

- **Created / updated**: 2026-10-26 / 2026-11-19
- **Task / library**: audio-text-to-text / longcap
- **Relevance**: 27 pts · Audio Understanding & Reasoning: audio captioning, sound event detection, audio-text (pipeline tag); Speech Generation, Recognition & Dialogue: automatic speech recognition; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=87 · likes=3 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2611.11125](https://arxiv.org/abs/2611.11125)
- **Datasets / base models**: unknown / JinchuanTian/LongCap-35B-A3B
- **Variants in family**: —

#### M5. JinchuanTian/LongCap-35B-A3B

- **Created / updated**: 2026-11-08 / 2026-11-19
- **Task / library**: audio-text-to-text / longcap
- **Relevance**: 27 pts · Audio Understanding & Reasoning: audio captioning, sound event detection, audio-text (pipeline tag); Speech Generation, Recognition & Dialogue: automatic speech recognition; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=100 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2611.11125](https://arxiv.org/abs/2611.11125)
- **Datasets / base models**: unknown / Qwen/Qwen3.5-35B-A3B-Base
- **Variants in family**: —

#### M6. nesoai-qa-org/higurashi-ai-Haru-4B

- **Created / updated**: 2026-11-19 / 2026-11-19
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M7. Microguy1/Haru-4B-DUPLI

- **Created / updated**: 2026-11-19 / 2026-11-19
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M8. TheStinger/Ilaria_RVC

- **Created / updated**: 2026-11-01 / 2026-11-19
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: text-to-speech; Audio Understanding & Reasoning: audio-text; declares license mit
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M9. ntc-ai/yue2-particle-sliders

- **Created / updated**: 2026-09-17 / 2026-11-19
- **Task / library**: text-to-audio / unknown
- **Relevance**: 20 pts · Generative Music & Audio: music generation, audio generation, text-to-audio (pipeline tag); declares license cc-by-nc-4.0; community likes 22
- **Adoption signals**: downloads=0 · likes=22 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / m-a-p/YuE2-3B
- **Variants in family**: —

#### M10. FireH2O/MrJMThaiTTS_CT

- **Created / updated**: 2026-11-16 / 2026-11-19
- **Task / library**: text-to-speech / pocket-tts
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license cc-by-sa-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-sa-4.0 / gated
- **Related papers**: [arXiv:2604.27607](https://arxiv.org/abs/2604.27607)
- **Datasets / base models**: pythainlp/som_tts_dataset, CMKL/Porjai-Thai-voice-dataset-central, airesearch/thai-ser / kyutai/pocket-tts
- **Variants in family**: —

#### M11. mehdi-hf/chatterbox-farsi

- **Created / updated**: 2026-11-11 / 2026-11-19
- **Task / library**: text-to-speech / chatterbox
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other; community likes 52
- **Adoption signals**: downloads=0 · likes=52 · trending=0.0
- **License / access**: other / gated
- **Related papers**: —
- **Datasets / base models**: unknown / ResembleAI/chatterbox
- **Variants in family**: —

#### M12. ishiki-labs/ishiki-deepfake-0.5

- **Created / updated**: 2026-11-18 / 2026-11-19
- **Task / library**: audio-classification / unknown
- **Relevance**: 15 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; model card links an arXiv paper; declares license mit
- **Adoption signals**: downloads=17 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: [arXiv:2202.12233](https://arxiv.org/abs/2202.12233) · [arXiv:1911.01601](https://arxiv.org/abs/1911.01601) · [arXiv:2504.05657](https://arxiv.org/abs/2504.05657) · [arXiv:2109.00537](https://arxiv.org/abs/2109.00537) · [arXiv:2209.08000](https://arxiv.org/abs/2209.08000)
- **Datasets / base models**: unknown / facebook/wav2vec2-xls-r-300m
- **Variants in family**: —

#### M13. RetentionLabs/personaplex-7b-extended

- **Created / updated**: 2026-11-16 / 2026-11-19
- **Task / library**: audio-to-audio / transformers
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=2 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2401.01325](https://arxiv.org/abs/2401.01325)
- **Datasets / base models**: unknown / nvidia/personaplex-7b-v1
- **Variants in family**: —

#### M14. mimba/mimba-tune

- **Created / updated**: 2026-11-07 / 2026-11-19
- **Task / library**: text-to-audio / peft
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / gated
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5
- **Variants in family**: —

#### M15. neurarank/voice-ai-s2s

- **Created / updated**: 2026-11-17 / 2026-11-19
- **Task / library**: audio-to-audio / transformers
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=109 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M16. hhhhaura/purplemusic-500k

- **Created / updated**: 2026-11-19 / 2026-11-19
- **Task / library**: text-to-audio / pytorch
- **Relevance**: 13 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag)
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / gated
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M17. amosgyamfi/Sophon-Realtime-4B-Flash-CoreAI

- **Created / updated**: 2026-11-19 / 2026-11-19
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / adventists-ai/Sophon-Realtime-4B-Flash
- **Variants in family**: —

#### M18. KaleComputer/kale-tts-1-nano

- **Created / updated**: 2026-11-16 / 2026-11-19
- **Task / library**: text-to-speech / onnx
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: text-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=129 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: KaleComputer/kale-tts-1-data / KaleComputer/kale-tts-1-base
- **Variants in family**: —

#### M19. rodbiren/kokoro_parakeet_aio_models

- **Created / updated**: 2026-10-02 / 2026-11-19
- **Task / library**: text-to-speech / unknown
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), automatic speech recognition; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M20. HeartMuLa/HeartMuLa-oss-3B

- **Created / updated**: 2026-01-14 / 2026-11-19
- **Task / library**: text-to-audio / unknown
- **Relevance**: 7 pts · Generative Music & Audio: text-to-audio (pipeline tag); model card links an arXiv paper; declares license apache-2.0; community likes 262
- **Adoption signals**: downloads=779 · likes=262 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2601.10547](https://arxiv.org/abs/2601.10547)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M21. HeartMuLa/HeartMuLa-oss-3B-happy-new-year

- **Created / updated**: 2026-02-13 / 2026-11-19
- **Task / library**: text-to-audio / unknown
- **Relevance**: 7 pts · Generative Music & Audio: text-to-audio (pipeline tag); model card links an arXiv paper; declares license apache-2.0; community likes 67
- **Adoption signals**: downloads=3158 · likes=67 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2601.10547](https://arxiv.org/abs/2601.10547)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M22. litert-community/MediaPipe-AudioClassifier-YAMNet

- **Created / updated**: 2026-11-18 / 2026-11-19
- **Task / library**: audio-classification / litert
- **Relevance**: 7 pts · Audio Understanding & Reasoning: sound event detection; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

## Research signals

- Speech Generation, Recognition & Dialogue: 4 papers
- Music Foundation Models & Representations: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [21Codec: Decoder-side Speaker Control for Text-to-Speech](https://arxiv.org/abs/2611.24094) | 2026-11-18 | 11 | Speech Generation, Recognition & Dialogue | — |
| 2 | [Location Matters: Layer-wise Prompt Conditioning for Voice--Style Disentanglement in Text-to-Speech](https://arxiv.org/abs/2611.24125) | 2026-11-18 | 10 | Speech Generation, Recognition & Dialogue | — |
| 3 | [Harmonic Circuit: Chord Progression Lies in a Sparse Principal Information Flow in Symbolic Music Models](https://arxiv.org/abs/2611.24453) | 2026-11-18 | 9 | Music Foundation Models & Representations | — |
| 4 | [Real-time sign language to speech translation using CNNs](https://www.semanticscholar.org/paper/34736970d1091a41439bc9daee5ae53424907b60) | 2026-11-15 | 8 | Speech Generation, Recognition & Dialogue | — |
| 5 | [Gaspard: Expressive unified speech and gesture synthesis with continuous autoregressive flow-matching and decoupled classifier-free guidance](https://arxiv.org/abs/2611.24862) | 2026-11-18 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. 21Codec: Decoder-side Speaker Control for Text-to-Speech

- **Authors**: David Lindevelt, Suzan Verberne, Joost Broekens
- **Date / sources**: 2026-11-18 · arxiv, semantic_scholar
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.24094) · [PDF](https://arxiv.org/pdf/2611.24094v1)

We propose 21Codec, a streaming codec model with reduced recoverable speaker information from the token stream and decoder-side speaker control. Existing codec models infer speaker identity from token stream. Making them streamable is not sufficiently robust to speaker drift, because each chunk re-infers the identity from the local chunk context alone. Our adversarial speaker classifier and NANSY-style formant-shift…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. Location Matters: Layer-wise Prompt Conditioning for Voice--Style Disentanglement in Text-to-Speech

- **Authors**: David Lindevelt, Suzan Verberne, Joost Broekens
- **Date / sources**: 2026-11-18 · arxiv
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: text-to-speech
- **Links**: [Paper](https://arxiv.org/abs/2611.24125) · [PDF](https://arxiv.org/pdf/2611.24125v1)

Independent control of voice and emotional style characteristics of speech is a long-standing problem in text-to-speech (TTS) systems. We investigate how the conditioning location of voice and style prompts across TTS decoder layers affects the trade-off between preservation and expressiveness for voice identity and emotional style. We introduce a layer-dependent gated fusion mechanism and systematically study which…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. Harmonic Circuit: Chord Progression Lies in a Sparse Principal Information Flow in Symbolic Music Models

- **Authors**: Ruiji Yu, Gus Xia
- **Date / sources**: 2026-11-18 · arxiv, semantic_scholar
- **Relevance**: 9 pts · Music Foundation Models & Representations: symbolic music; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.24453) · [PDF](https://arxiv.org/pdf/2611.24453v1)

Mechanistic Interpretability (MI) seeks to decode neural network computations into human-understandable logic. A core methodology in MI is circuit discovery: identifying the information flow in sub-networks that drive specific model behaviors. While circuit discovery has matured within Natural Language Processing (NLP), the interpretable circuits in music models remain largely unexplored. In this work, we identify a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Real-time sign language to speech translation using CNNs

- **Authors**: Piotr Krzysztof Gdula
- **Date / sources**: 2026-11-15 · semantic_scholar
- **Relevance**: 8 pts · Speech Generation, Recognition & Dialogue: speech translation
- **Links**: [Paper](https://www.semanticscholar.org/paper/34736970d1091a41439bc9daee5ae53424907b60) · [PDF](https://doi.org/10.5604/01.3001.0055.9904)

<p><span lang="EN-US" style="font-size:10.0pt"><span style="font-family:"Times New Roman",serif">This article presents the design, implementation, and empirical evaluation of an end-to-end software architecture for the real-time translation of the American Sign Language (ASL) alphabet into text and synthesized speech. The proposed system leverages the OpenCV library for video ingestion and the MediaPipe framework to…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Gaspard: Expressive unified speech and gesture synthesis with continuous autoregressive flow-matching and decoupled classifier-free guidance

- **Authors**: Téo Guichoux, Théodor Lemerle, Catherine Pelachaud, Nicolas Obin
- **Date / sources**: 2026-11-18 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: speech generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.24862) · [PDF](https://arxiv.org/pdf/2611.24862v1)

Human communication involves highly coordinated multimodal signals such as speech and co-speech gestures. Existing approaches for generating both modalities commonly follow a cascaded pipeline, where speech is generated first and subsequently used to drive gesture generation; speech generation is therefore independent of gestures. We introduce Gaspard, a unified speech--gesture generation model based on continuous…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
