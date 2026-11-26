# Music / Audio Foundation Model Research Radar — 2026-11-26

> Lookback window: 2026-11-19 to 2026-11-26 · New papers: 13 · New models: 19 · relevant papers/models in window: 48/67 · raw papers/models: 158/335

Sources: arxiv=88 · semantic_scholar=70 · huggingface_models=335

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [goldhub/Ruach_Studio_Models_v2](https://huggingface.co/goldhub/Ruach_Studio_Models_v2) | 2026-11-25 | text-to-audio | 45 | 1 | 5296 | 11 | other |
| 2 | [urbanhorizons/ada-omni-tr](https://huggingface.co/urbanhorizons/ada-omni-tr) | 2026-11-25 | audio-to-audio | 32 | 1 | 0 | 1 | apache-2.0 |
| 3 | [mrinaltbi/tbi-tts](https://huggingface.co/mrinaltbi/tbi-tts) | 2026-11-25 | text-to-speech | 26 | 1 | 0 | 1 | cc-by-nc-4.0 |
| 4 | [audio-cpp/audio.cpp-gguf](https://huggingface.co/audio-cpp/audio.cpp-gguf) | 2026-11-25 | text-to-speech | 24 | 1 | 10014231 | 343 | other |
| 5 | [TheStinger/Ilaria_RVC](https://huggingface.co/TheStinger/Ilaria_RVC) | 2026-11-25 | audio-to-audio | 21 | 1 | 0 | 1 | mit |
| 6 | [fdemelo/open-supertonic2-pytorch](https://huggingface.co/fdemelo/open-supertonic2-pytorch) | 2026-11-25 | text-to-speech | 17 | 1 | 0 | 0 | openrail |
| 7 | [aungzaythant/Howard-0.6B](https://huggingface.co/aungzaythant/Howard-0.6B) | 2026-11-25 | text-to-speech | 15 | 1 | 0 | 2 | apache-2.0 |
| 8 | [NikitHamal/sakhiya-pro-v1](https://huggingface.co/NikitHamal/sakhiya-pro-v1) | 2026-11-25 | text-to-speech | 15 | 1 | 229 | 0 | other |
| 9 | [Lysandra999/Senik-Voice-Expressive-0.5B](https://huggingface.co/Lysandra999/Senik-Voice-Expressive-0.5B) | 2026-11-25 | text-to-speech | 15 | 1 | 70 | 0 | mit |
| 10 | [rassmos/egyptian-arabic-tts-GGUF](https://huggingface.co/rassmos/egyptian-arabic-tts-GGUF) | 2026-11-25 | text-to-speech | 15 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 11 | [JRufer/Reverb-TTS-GGUF](https://huggingface.co/JRufer/Reverb-TTS-GGUF) | 2026-11-25 | text-to-speech | 15 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 12 | [cuongyd196/VieNeu-TTS-v3-Turbo-d3](https://huggingface.co/cuongyd196/VieNeu-TTS-v3-Turbo-d3) | 2026-11-25 | text-to-speech | 15 | 1 | 0 | 0 | apache-2.0 |
| 13 | [jmcgomes/MOSS-Audio-8B-Thinking-MLX-4bit](https://huggingface.co/jmcgomes/MOSS-Audio-8B-Thinking-MLX-4bit) | 2026-11-25 | audio-text-to-text | 15 | 2 | 0 | 0 | apache-2.0 |
| 14 | [elnemer7/ElNeMeR-Audio-Splice-Clone-ONNX](https://huggingface.co/elnemer7/ElNeMeR-Audio-Splice-Clone-ONNX) | 2026-11-25 | audio-classification | 13 | 1 | 11 | 0 | mit |
| 15 | [TarikaHedaoo/indic-deepfake-voice-detection](https://huggingface.co/TarikaHedaoo/indic-deepfake-voice-detection) | 2026-11-25 | audio-classification | 13 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 16 | [voidful/acousticflow-tw-20261125](https://huggingface.co/voidful/acousticflow-tw-20261125) | 2026-11-25 | text-to-speech | 13 | 1 | 0 | 0 | other |
| 17 | [oddadmix/tiny-voca-arabic](https://huggingface.co/oddadmix/tiny-voca-arabic) | 2026-11-25 | text-to-speech | 12 | 1 | 182 | 21 | apache-2.0 |
| 18 | [Ranjit/gemma-4-12b-it-speech-translation-int4](https://huggingface.co/Ranjit/gemma-4-12b-it-speech-translation-int4) | 2026-11-25 | audio-text-to-text | 11 | 1 | 0 | 0 | apache-2.0 |
| 19 | [aman4014/whisper-large-v3-turbo-german-allrounder-v3](https://huggingface.co/aman4014/whisper-large-v3-turbo-german-allrounder-v3) | 2026-11-25 | automatic-speech-recognition | 10 | 2 | 0 | 0 | mit |

### Model cards

#### M1. goldhub/Ruach_Studio_Models_v2

- **Created / updated**: 2026-10-10 / 2026-11-25
- **Task / library**: text-to-audio / ggml
- **Relevance**: 45 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license other; community likes 11
- **Adoption signals**: downloads=5296 · likes=11 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2503.08638](https://arxiv.org/abs/2503.08638)
- **Datasets / base models**: unknown / m-a-p/YuE2-3B
- **Variants in family**: —

#### M2. urbanhorizons/ada-omni-tr

- **Created / updated**: 2026-11-24 / 2026-11-25
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 32 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; Audio Understanding & Reasoning: audio understanding; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unsloth/gemma-3n-E2B-it, erkamk/qwen3-0.6b-tr
- **Variants in family**: —

#### M3. mrinaltbi/tbi-tts

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: text-to-speech / unknown
- **Relevance**: 26 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech, voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M4. audio-cpp/audio.cpp-gguf

- **Created / updated**: 2026-07-14 / 2026-11-25
- **Task / library**: text-to-speech / audio.cpp
- **Relevance**: 24 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), automatic speech recognition; declares license other; community likes 343
- **Adoption signals**: downloads=10014231 · likes=343 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / kobimusic/dettato, kobimusic/dettato-evidence, kobimusic/dettato-grouper, kobimusic/dettato-drums, gradium/phonon-40m-fr
- **Variants in family**: —

#### M5. TheStinger/Ilaria_RVC

- **Created / updated**: 2026-11-01 / 2026-11-25
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: text-to-speech; Audio Understanding & Reasoning: audio-text; declares license mit
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M6. fdemelo/open-supertonic2-pytorch

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: text-to-speech / pytorch
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license openrail
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: openrail / public
- **Related papers**: [arXiv:2503.23108](https://arxiv.org/abs/2503.23108)
- **Datasets / base models**: unknown / Supertone/supertonic-2
- **Variants in family**: —

#### M7. aungzaythant/Howard-0.6B

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: text-to-speech / mlx
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3-TTS-12Hz-0.6B-Base
- **Variants in family**: —

#### M8. NikitHamal/sakhiya-pro-v1

- **Created / updated**: 2026-11-23 / 2026-11-25
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=229 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / k2-fsa/OmniVoice
- **Variants in family**: —

#### M9. Lysandra999/Senik-Voice-Expressive-0.5B

- **Created / updated**: 2026-11-22 / 2026-11-25
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license mit
- **Adoption signals**: downloads=70 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M10. rassmos/egyptian-arabic-tts-GGUF

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: text-to-speech / voxcpm
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Trelis/egyptian-arabic-tts-research
- **Variants in family**: —

#### M11. JRufer/Reverb-TTS-GGUF

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: text-to-speech / audio.cpp
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / software-mansion/Reverb-TTS
- **Variants in family**: —

#### M12. cuongyd196/VieNeu-TTS-v3-Turbo-d3

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / pnnbao-ump/VieNeu-TTS-v3-Turbo
- **Variants in family**: —

#### M13. jmcgomes/MOSS-Audio-8B-Thinking-MLX-4bit

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: audio-text-to-text / mlx
- **Relevance**: 15 pts · Audio Understanding & Reasoning: audio understanding, audio-text (pipeline tag); model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2606.01802](https://arxiv.org/abs/2606.01802)
- **Datasets / base models**: unknown / OpenMOSS-Team/MOSS-Audio-8B-Thinking
- **Variants in family**: jmcgomes/MOSS-Audio-8B-Thinking-MLX-8bit

#### M14. elnemer7/ElNeMeR-Audio-Splice-Clone-ONNX

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: audio-classification / onnx
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: voice cloning; declares license mit
- **Adoption signals**: downloads=11 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M15. TarikaHedaoo/indic-deepfake-voice-detection

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: audio-classification / pytorch
- **Relevance**: 13 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / facebook/wav2vec2-xls-r-300m
- **Variants in family**: —

#### M16. voidful/acousticflow-tw-20261125

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: text-to-speech / unknown
- **Relevance**: 13 pts · Generative Music & Audio: singing voice synthesis; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / gated
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M17. oddadmix/tiny-voca-arabic

- **Created / updated**: 2026-11-21 / 2026-11-25
- **Task / library**: text-to-speech / onnxruntime
- **Relevance**: 12 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license apache-2.0; community likes 21
- **Adoption signals**: downloads=182 · likes=21 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: oddadmix/msa-duplex-assistant-tts / unknown
- **Variants in family**: —

#### M18. Ranjit/gemma-4-12b-it-speech-translation-int4

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech translation; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / google/gemma-4-12b-it
- **Variants in family**: —

#### M19. aman4014/whisper-large-v3-turbo-german-allrounder-v3

- **Created / updated**: 2026-11-25 / 2026-11-25
- **Task / library**: automatic-speech-recognition / unknown
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / primeline/whisper-large-v3-turbo-german
- **Variants in family**: aman4014/whisper-large-v3-turbo-german-allrounder-v3-ct2

## Research signals

- Generative Music & Audio: 4 papers
- Evaluation, Alignment, Safety & Copyright: 4 papers
- Audio & Speech Language Models: 3 papers
- Speech Generation, Recognition & Dialogue: 2 papers
- Audio Understanding & Reasoning: 1 papers
- Music Foundation Models & Representations: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [Is Prosody Encoded in the Neural Audio Codec Mimi?](https://arxiv.org/abs/2611.32795) | 2026-11-24 | 22 | Audio & Speech Language Models, Generative Music & Audio, Speech Generation, Recognition & Dialogue | — |
| 2 | [Do Layer Rankings Survive Silence Trimming? The Silence Shortcut in Frozen WavLM Representations for Audio Deepfake Detection](https://arxiv.org/abs/2611.32457) | 2026-11-24 | 15 | Evaluation, Alignment, Safety & Copyright | [repo](https://github.com/Nooralabd/silence-shortcut-wavlm-layers) |
| 3 | [ClusterVAD: Threshold-Free Unsupervised Voice Activity Detection with Pre-Trained Neural Representations](https://arxiv.org/abs/2611.33059) | 2026-11-24 | 14 | Audio & Speech Language Models | — |
| 4 | [Perfect Scores, Misplaced Explanations: A Controlled Study of Explainability in Audio Deepfake Detection](https://arxiv.org/abs/2611.32593) | 2026-11-24 | 13 | Evaluation, Alignment, Safety & Copyright | — |
| 5 | [MADlibs: Analyzing the Distribution of Generative Music](https://arxiv.org/abs/2611.31462) | 2026-11-23 | 13 | Generative Music & Audio | — |
| 6 | [VividAudio: Multi-Event Reference-Conditioned Video-to-Audio Generation](https://arxiv.org/abs/2611.32458) | 2026-11-24 | 11 | Generative Music & Audio | — |
| 7 | [HEAR, SEE, SPIKE ONCE: Highly Efficient NeuroAI Temporal Neural Networks for Low-Precision Multimodal Audio-Visual Classification and Online Learning](https://arxiv.org/abs/2611.31884) | 2026-11-24 | 11 | Audio Understanding & Reasoning | — |
| 8 | [Task conditioned symmetry constraints and anticollapse temporal learning for invariant symbolic music pattern assessment](https://www.semanticscholar.org/paper/e1414ee1cc49f7f9175a20c44d2e5bb54db058a9) | 2026-11-25 | 8 | Music Foundation Models & Representations | — |
| 9 | [Phoneme-identity depth profiles do not reliably predict LoRA placement for dysarthric ASR](https://arxiv.org/abs/2611.32455) | 2026-11-24 | 8 | Audio & Speech Language Models | — |
| 10 | [Putting a Robot on a Phone Call: Layered Signaling, Bounded Occupancy and Turn Arbitration over WebRTC](https://arxiv.org/abs/2611.32308) | 2026-11-24 | 6 | Speech Generation, Recognition & Dialogue | — |
| 11 | [The crisis of digital truth: deepfakes and normative disruption in algorithmic society](https://www.semanticscholar.org/paper/267ee756ee50a3ab44d0e80edeeea698e77ddbd0) | 2026-11-23 | 6 | Evaluation, Alignment, Safety & Copyright | — |
| 12 | [Who Plays What: Same-Instrument Music Separation from Video](https://arxiv.org/abs/2611.29411) | 2026-11-22 | 6 | Evaluation, Alignment, Safety & Copyright | — |
| 13 | [PopMelodyGen: A Copyright-Aware Platform for Controllable Pop-Melody Generation](https://arxiv.org/abs/2611.28686) | 2026-11-21 | 6 | Generative Music & Audio | — |

## Paper cards

### 1. Is Prosody Encoded in the Neural Audio Codec Mimi?

- **Authors**: Nicolas Ballier, Artem Saloev, Erin Pacquetet, Taylor Arnold
- **Date / sources**: 2026-11-24 · arxiv
- **Relevance**: 22 pts · Generative Music & Audio: neural audio codec; Speech Generation, Recognition & Dialogue: speech translation, speech-to-speech; Audio & Speech Language Models: speech-language model
- **Links**: [Paper](https://arxiv.org/abs/2611.32795) · [PDF](https://arxiv.org/pdf/2611.32795v1)

Neural audio codecs (NACs) have become a fundamental infrastructure for modern speech-language models, discretizing continuous speech signals into token sequences that enable large language models to process and generate audio. Most research evaluates codec quality at the decoding phase, assessing the naturalness of reconstructed speech. However, little research investigates what phonetic information is captured…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. Do Layer Rankings Survive Silence Trimming? The Silence Shortcut in Frozen WavLM Representations for Audio Deepfake Detection

- **Authors**: Nur Elabid, Mahmud Esad Arar
- **Date / sources**: 2026-11-24 · arxiv, semantic_scholar
- **Relevance**: 15 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.32457) · [PDF](https://arxiv.org/pdf/2611.32457v1) · [Code 1](https://github.com/Nooralabd/silence-shortcut-wavlm-layers)

Layer-wise analyses of frozen self-supervised encoders are used to locate spoofing information in audio deepfake detection. On the ASVspoof 2019 logical access (LA) benchmark, bonafide recordings carry longer leading and trailing silence than spoofed ones, and detectors exploit this cue, the silence shortcut. This paper examines whether layer rankings for a frozen WavLM Base encoder survive the trimming of this…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. ClusterVAD: Threshold-Free Unsupervised Voice Activity Detection with Pre-Trained Neural Representations

- **Authors**: Karl El Hajal, Mathew Magimai. -Doss
- **Date / sources**: 2026-11-24 · arxiv, semantic_scholar
- **Relevance**: 14 pts · Audio & Speech Language Models: speech language model, speech foundation model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.33059) · [PDF](https://arxiv.org/pdf/2611.33059v1)

Voice activity detection (VAD) is one of the first steps in speech processing pipelines, from transcription and diarization to speech language models. Supervised detectors need labelled data and inherit the domain and annotation conventions of their training corpora. Existing unsupervised detectors rely on hand-crafted acoustic features which cannot benefit from data and degrade in far-field, noisy or atypical…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Perfect Scores, Misplaced Explanations: A Controlled Study of Explainability in Audio Deepfake Detection

- **Authors**: David Combei, Dan Oneata, Francesco Paissan, Cem Subakan, Horia Cucu, Adriana Stan
- **Date / sources**: 2026-11-24 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.32593) · [PDF](https://arxiv.org/pdf/2611.32593v1)

What if an explanation achieves perfect scores but it is uninterpretable? We show that this happens when explaining audio deepfake detectors. Using an optimization-based method, we explain a state-of-the-art wav2vec2-based detector. The explanations achieve optimal scores on standard explainability metrics, i.e. fidelity and faithfulness. Visual inspection, however, reveals unintuitive and uninterpretable patterns.…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. MADlibs: Analyzing the Distribution of Generative Music

- **Authors**: Matthew Keating, Noah Schaffer, Michael Casey, Nikhil Singh
- **Date / sources**: 2026-11-23 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Generative Music & Audio: text-to-music, music generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.31462) · [PDF](https://arxiv.org/pdf/2611.31462v1)

What music can a text-to-music model actually make? The answer to this question has consequences for individual creators, communities, and musical culture more broadly. We introduce MADlibs, a framework to measure the expressive support of state-of-the-art music generators: the subset of musical behaviors they will actually produce across the space of prompts. We first develop strategies for generating musical…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. VividAudio: Multi-Event Reference-Conditioned Video-to-Audio Generation

- **Authors**: You Li, Dewei Zhou, Fan Ma, Dongliang He, Yi Yang
- **Date / sources**: 2026-11-24 · arxiv, semantic_scholar
- **Relevance**: 11 pts · Generative Music & Audio: audio generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.32458) · [PDF](https://arxiv.org/pdf/2611.32458v1)

Existing video-to-audio (V2A) methods have achieved promising results in synthesizing high-quality audios. However, as V2A advances toward more flexible user-directed creation, existing methods remain notably limited in controlling the distinct acoustic identities of multiple events within a video. We therefore formulate multi-event reference-conditioned V2A (Mr-V2A), where each event is assigned a specific audio…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. HEAR, SEE, SPIKE ONCE: Highly Efficient NeuroAI Temporal Neural Networks for Low-Precision Multimodal Audio-Visual Classification and Online Learning

- **Authors**: Shanmuga Venkatachalam, Quinn Jacobson, John Paul Shen
- **Date / sources**: 2026-11-24 · arxiv, semantic_scholar
- **Relevance**: 11 pts · Audio Understanding & Reasoning: multimodal audio; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.31884) · [PDF](https://arxiv.org/pdf/2611.31884v1)

Spiking neural networks for multimodal audio-visual classification reach high accuracy by adopting deep-learning machinery: multi-stage convolutional or transformer encoders trained end-to-end with surrogate-gradient backpropagation through time. These prior works typically rely on full-precision (32-bit) parameters and do not treat hardware efficiency as a primary design objective. In this paper, we propose…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. Task conditioned symmetry constraints and anticollapse temporal learning for invariant symbolic music pattern assessment

- **Authors**: He-Yao Ma
- **Date / sources**: 2026-11-25 · semantic_scholar
- **Relevance**: 8 pts · Music Foundation Models & Representations: symbolic music
- **Links**: [Paper](https://www.semanticscholar.org/paper/e1414ee1cc49f7f9175a20c44d2e5bb54db058a9)

No abstract

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. Phoneme-identity depth profiles do not reliably predict LoRA placement for dysarthric ASR

- **Authors**: Bernard Muller, LaVonne Roberts
- **Date / sources**: 2026-11-24 · arxiv, semantic_scholar
- **Relevance**: 8 pts · Audio & Speech Language Models: speech foundation model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.32455) · [PDF](https://arxiv.org/pdf/2611.32455v1)

Parameter-efficient adaptation of a speech foundation model to dysarthric speech requires a rarely justified choice: which encoder layers to adapt. A recently proposed strategy is to probe the encoder, find where phonetic information becomes most decodable, and put the adapters there. We test that inference across two ASR models (Qwen3-ASR, Whisper-small) and two dysarthric corpora (Mandarin CDSD, English UASpeech),…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. Putting a Robot on a Phone Call: Layered Signaling, Bounded Occupancy and Turn Arbitration over WebRTC

- **Authors**: Zheyuan Zhang, Zaide Zhang
- **Date / sources**: 2026-11-24 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: speech generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.32308) · [PDF](https://arxiv.org/pdf/2611.32308v1)

We put a Thor robot on a browser voice call, with speech sent from Safari, answers played through the robot's loudspeaker and transcripts returned to the phone. We separate HTTPS signaling, relayed WebRTC media and speech generation into independently observable routes. The browser prefetches relay credentials and allows a 500 ms window after its first relay candidate. The backend starts speech and WebRTC-answer…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 11. The crisis of digital truth: deepfakes and normative disruption in algorithmic society

- **Authors**: Daniele Battista, L. Cervi
- **Date / sources**: 2026-11-23 · semantic_scholar
- **Relevance**: 6 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake
- **Links**: [Paper](https://www.semanticscholar.org/paper/267ee756ee50a3ab44d0e80edeeea698e77ddbd0) · [PDF](https://www.frontiersin.org/journals/sociology/articles/10.3389/fsoc.2026.1992186/pdf)

Generative artificial intelligence has made deepfakes a source of instability in contemporary information environments, challenging not only communication processes but also the normative arrangements through which trust, evidence, and accountability are established. This article examines their implications for digital societies and conceptualizes them as a form of normative disruption. A structured conceptual…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 12. Who Plays What: Same-Instrument Music Separation from Video

- **Authors**: Abhinaba Roy, Ambuj Mehrish, Sebastiano Vascon, Dorien Herremans
- **Date / sources**: 2026-11-22 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Evaluation, Alignment, Safety & Copyright: music benchmark; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29411) · [PDF](https://arxiv.org/pdf/2611.29411v1)

When two musicians in an ensemble play the same instrument, they sound alike and their instruments look alike. Audio-only separators, and audio-visual separators that rely on appearance, cannot tell them apart. What still differs is how each player moves, and when. We study same-instrument per-player separation: a user clicks one musician in a video and receives that musician's sound alone, even when other players…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 13. PopMelodyGen: A Copyright-Aware Platform for Controllable Pop-Melody Generation

- **Authors**: Di Lu, Xinran Zhang, Qingwen Zhou, Yan Gao, Yuan Zhang, Xiaoqing Wang, Yuming Sun, Xiaobing Li et al.
- **Date / sources**: 2026-11-21 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Generative Music & Audio: music generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.28686) · [PDF](https://arxiv.org/pdf/2611.28686v1)

Large-scale redistributable symbolic pop-melody data remain scarce due to copyright restrictions, creating a bottleneck for both practical deployment and reproducible research in music generation. We present PopMelodyGen, a copyright-aware platform for controllable pop-melody generation that combines rule-based synthesis with neural generation. Our approach first uses an expert synthesizer to produce large-scale…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
