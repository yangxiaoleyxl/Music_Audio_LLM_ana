# Music / Audio Foundation Model Research Radar — 2026-11-21

> Lookback window: 2026-11-14 to 2026-11-21 · New papers: 2 · New models: 24 · relevant papers/models in window: 34/58 · raw papers/models: 125/355

Sources: arxiv=68 · semantic_scholar=57 · huggingface_models=355

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [moonbox-dev/MiniMax-Music3-MLX](https://huggingface.co/moonbox-dev/MiniMax-Music3-MLX) | 2026-11-20 | text-to-audio | 47 | 1 | 0 | 0 | other |
| 2 | [moonbox-dev/YuE2-3B-MLX](https://huggingface.co/moonbox-dev/YuE2-3B-MLX) | 2026-11-20 | text-to-audio | 44 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 3 | [snkii/Sori-10B-Speech](https://huggingface.co/snkii/Sori-10B-Speech) | 2026-11-21 | audio-text-to-text | 43 | 1 | 58 | 1 | cc-by-nc-sa-4.0 |
| 4 | [jjcoders/suna-v1](https://huggingface.co/jjcoders/suna-v1) | 2026-11-21 | text-to-audio | 42 | 1 | 2257 | 2 | mit |
| 5 | [touati-kamel/Hadra-TTS-xtts](https://huggingface.co/touati-kamel/Hadra-TTS-xtts) | 2026-11-21 | text-to-speech | 28 | 1 | 59 | 0 | other |
| 6 | [warten/Haru-4B](https://huggingface.co/warten/Haru-4B) | 2026-11-21 | audio-to-audio | 27 | 1 | 0 | 0 | apache-2.0 |
| 7 | [Evan-Lin/Crossfeed-Unison](https://huggingface.co/Evan-Lin/Crossfeed-Unison) | 2026-11-21 | text-to-speech | 25 | 1 | 0 | 0 | other |
| 8 | [prakharkhatri/dvitts](https://huggingface.co/prakharkhatri/dvitts) | 2026-11-21 | text-to-speech | 22 | 1 | 30 | 2 | apache-2.0 |
| 9 | [TheStinger/Ilaria_RVC](https://huggingface.co/TheStinger/Ilaria_RVC) | 2026-11-21 | audio-to-audio | 21 | 1 | 0 | 1 | mit |
| 10 | [empiriolabsai/canora-dutch](https://huggingface.co/empiriolabsai/canora-dutch) | 2026-11-21 | text-to-speech | 19 | 5 | 138 | 0 | apache-2.0 |
| 11 | [Mikhailo/mova-tts](https://huggingface.co/Mikhailo/mova-tts) | 2026-11-21 | text-to-speech | 18 | 1 | 0 | 0 | apache-2.0 |
| 12 | [TontaubeAI/TontaubeV1](https://huggingface.co/TontaubeAI/TontaubeV1) | 2026-11-21 | text-to-speech | 17 | 2 | 0 | 18 | other |
| 13 | [TontaubeAI/TontaubeV1.1-int4](https://huggingface.co/TontaubeAI/TontaubeV1.1-int4) | 2026-11-21 | text-to-speech | 16 | 1 | 0 | 24 | other |
| 14 | [hongyanaipro/Capoo-LLM-models](https://huggingface.co/hongyanaipro/Capoo-LLM-models) | 2026-11-21 | text-to-speech | 15 | 1 | 0 | 1 | apache-2.0 |
| 15 | [gabrione/pocket-tts-phonemes-multilang](https://huggingface.co/gabrione/pocket-tts-phonemes-multilang) | 2026-11-21 | text-to-speech | 15 | 2 | 0 | 0 | cc-by-4.0 |
| 16 | [Maximilian228/Geode-YuE2](https://huggingface.co/Maximilian228/Geode-YuE2) | 2026-11-21 | text-to-audio | 14 | 1 | 0 | 1 | cc-by-nc-4.0 |
| 17 | [Maximilian228/Geode-ACE-Step-1.5-turbo](https://huggingface.co/Maximilian228/Geode-ACE-Step-1.5-turbo) | 2026-11-21 | text-to-audio | 14 | 1 | 0 | 0 | mit |
| 18 | [Maximilian228/Geode-ACE-Step-1.5](https://huggingface.co/Maximilian228/Geode-ACE-Step-1.5) | 2026-11-21 | text-to-audio | 14 | 1 | 0 | 0 | mit |
| 19 | [yangsu0423/YuE2-OpenVINO-INT4](https://huggingface.co/yangsu0423/YuE2-OpenVINO-INT4) | 2026-11-21 | text-to-audio | 14 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 20 | [superretrosfx/RVC-MODEL](https://huggingface.co/superretrosfx/RVC-MODEL) | 2026-11-21 | audio-to-audio | 13 | 1 | 0 | 0 | mit |
| 21 | [Firoj112/pawp-tts-1.5m-wsp](https://huggingface.co/Firoj112/pawp-tts-1.5m-wsp) | 2026-11-21 | text-to-speech | 11 | 1 | 0 | 1 | cc-by-4.0 |
| 22 | [Firoj112/pawp-tts-1.5m](https://huggingface.co/Firoj112/pawp-tts-1.5m) | 2026-11-21 | text-to-speech | 11 | 1 | 0 | 1 | cc-by-4.0 |
| 23 | [huybik/hibiki-zero-vi-full-sft](https://huggingface.co/huybik/hibiki-zero-vi-full-sft) | 2026-11-21 | audio-to-audio | 9 | 1 | 0 | 1 | cc-by-nc-sa-4.0 |
| 24 | [RKB109/audio-event-triage-20261121-model](https://huggingface.co/RKB109/audio-event-triage-20261121-model) | 2026-11-21 | audio-classification | 7 | 1 | 0 | 0 | mit |

### Model cards

#### M1. moonbox-dev/MiniMax-Music3-MLX

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: text-to-audio / mlx
- **Relevance**: 47 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / MiniMaxAI/MiniMax-Music3
- **Variants in family**: —

#### M2. moonbox-dev/YuE2-3B-MLX

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: text-to-audio / mlx
- **Relevance**: 44 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2609.33757](https://arxiv.org/abs/2609.33757) · [arXiv:2610.05336](https://arxiv.org/abs/2610.05336) · [arXiv:2503.08638](https://arxiv.org/abs/2503.08638)
- **Datasets / base models**: unknown / m-a-p/YuE2-3B
- **Variants in family**: —

#### M3. snkii/Sori-10B-Speech

- **Created / updated**: 2026-11-20 / 2026-11-21
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 43 pts · Audio & Speech Language Models: audio language model, audio-language model, speech llm; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=58 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.5-9B, Qwen/Qwen3-Omni-30B-A3B-Instruct
- **Variants in family**: —

#### M4. jjcoders/suna-v1

- **Created / updated**: 2026-10-11 / 2026-11-21
- **Task / library**: text-to-audio / diffusers
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license mit
- **Adoption signals**: downloads=2257 · likes=2 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M5. touati-kamel/Hadra-TTS-xtts

- **Created / updated**: 2026-11-16 / 2026-11-21
- **Task / library**: text-to-speech / unknown
- **Relevance**: 28 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; Generative Music & Audio: audio generation; declares license other
- **Adoption signals**: downloads=59 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: oddadmix/arabic-audio-collection-algerian-kahwa-postcast, oddadmix/arabic-audio-collection-algerian-rawi, oddadmix/arabic-audio-collection-algerian-loubna-stories / coqui/XTTS-v2
- **Variants in family**: —

#### M6. warten/Haru-4B

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M7. Evan-Lin/Crossfeed-Unison

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-speech / unknown
- **Relevance**: 25 pts · Generative Music & Audio: text-to-audio; Audio Understanding & Reasoning: audio-text; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen2.5-Omni-7B, jac22/UNISON
- **Variants in family**: —

#### M8. prakharkhatri/dvitts

- **Created / updated**: 2026-11-17 / 2026-11-21
- **Task / library**: text-to-speech / dvitts
- **Relevance**: 22 pts · Speech Generation, Recognition & Dialogue: speech generation, text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=30 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2505.17589](https://arxiv.org/abs/2505.17589)
- **Datasets / base models**: unknown / FunAudioLLM/Fun-CosyVoice3-0.5B-2512
- **Variants in family**: —

#### M9. TheStinger/Ilaria_RVC

- **Created / updated**: 2026-11-01 / 2026-11-21
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: text-to-speech; Audio Understanding & Reasoning: audio-text; declares license mit
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M10. empiriolabsai/canora-dutch

- **Created / updated**: 2026-11-20 / 2026-11-21
- **Task / library**: text-to-speech / kokoro
- **Relevance**: 19 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=138 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / hexgrad/Kokoro-82M
- **Variants in family**: empiriolabsai/canora-polish, empiriolabsai/canora-korean, empiriolabsai/canora-turkish, empiriolabsai/canora-german

#### M11. Mikhailo/mova-tts

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-speech / mova-tts
- **Relevance**: 18 pts · Speech Generation, Recognition & Dialogue: text-to-speech, voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / neuphonic/neutts-air
- **Variants in family**: —

#### M12. TontaubeAI/TontaubeV1

- **Created / updated**: 2026-08-26 / 2026-11-21
- **Task / library**: text-to-speech / unknown
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=0 · likes=18 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2609.08703](https://arxiv.org/abs/2609.08703)
- **Datasets / base models**: unknown / Qwen/Qwen3-1.7B, Qwen/Qwen3-0.6B
- **Variants in family**: TontaubeAI/TontaubeV1.1

#### M13. TontaubeAI/TontaubeV1.1-int4

- **Created / updated**: 2026-11-10 / 2026-11-21
- **Task / library**: text-to-speech / unknown
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other; community likes 24
- **Adoption signals**: downloads=0 · likes=24 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / TontaubeAI/TontaubeV1.1
- **Variants in family**: —

#### M14. hongyanaipro/Capoo-LLM-models

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M15. gabrione/pocket-tts-phonemes-multilang

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-speech / pocket-tts
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/pocket-tts
- **Variants in family**: gabrione/pocket-tts-phonemes-africa

#### M16. Maximilian228/Geode-YuE2

- **Created / updated**: 2026-11-11 / 2026-11-21
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / m-a-p/YuE2-3B, m-a-p/YuE2-Vae
- **Variants in family**: —

#### M17. Maximilian228/Geode-ACE-Step-1.5-turbo

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5
- **Variants in family**: —

#### M18. Maximilian228/Geode-ACE-Step-1.5

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5, ACE-Step/acestep-v15-sft, ACE-Step/acestep-5Hz-lm-1.7B, Qwen/Qwen3-Embedding-0.6B
- **Variants in family**: —

#### M19. yangsu0423/YuE2-OpenVINO-INT4

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M20. superretrosfx/RVC-MODEL

- **Created / updated**: 2025-12-11 / 2026-11-21
- **Task / library**: audio-to-audio / keras-hub
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: voice cloning; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: openbmb/UltraData-SFT-Agent-2609, openbmb/UltraData-RL-2609 / nex-agi/Nex-N2.5-mini
- **Variants in family**: —

#### M21. Firoj112/pawp-tts-1.5m-wsp

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Firoj112/pawp-tts-1.5m
- **Variants in family**: —

#### M22. Firoj112/pawp-tts-1.5m

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M23. huybik/hibiki-zero-vi-full-sft

- **Created / updated**: 2026-07-29 / 2026-11-21
- **Task / library**: audio-to-audio / moshi
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: speech translation; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/hibiki-zero-3b-pytorch-bf16
- **Variants in family**: —

#### M24. RKB109/audio-event-triage-20261121-model

- **Created / updated**: 2026-11-21 / 2026-11-21
- **Task / library**: audio-classification / custom
- **Relevance**: 7 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: RKB109/audio-event-triage-20261121-dataset / unknown
- **Variants in family**: —

## Research signals

- Evaluation, Alignment, Safety & Copyright: 1 papers
- Speech Generation, Recognition & Dialogue: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [DCMC-Fusion: Data-Centric and Model-Centric Ensemble Learning for Audio Deepfake Detection](https://www.semanticscholar.org/paper/64da2b635a7cec671c4f09d773a95d1295f15d1e) | 2026-11-18 | 12 | Evaluation, Alignment, Safety & Copyright | — |
| 2 | [The Who and How of Recreating the Dead: Relational Distance and Acceptance](https://www.semanticscholar.org/paper/2a9dc56113f4967b9f7978ecac67ac903695f6d8) | 2026-11-18 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. DCMC-Fusion: Data-Centric and Model-Centric Ensemble Learning for Audio Deepfake Detection

- **Authors**: D. Ballesteros, Carlos Guerra
- **Date / sources**: 2026-11-18 · semantic_scholar
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake
- **Links**: [Paper](https://www.semanticscholar.org/paper/64da2b635a7cec671c4f09d773a95d1295f15d1e) · [PDF](https://doi.org/10.3390/bdcc10110394)

Audio deepfake detectors often exhibit substantial performance degradation when evaluated on speech generated by synthesis technologies not represented during training. In this study, 20 individual detectors, derived from five deep learning architectures (DenseNet121, ResNet50, InceptionV3, ResNet34, and VGG16) and four spectral representations (LOG, Mel, DWT, and CQT), achieved F1-scores above 0.95 during internal…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. The Who and How of Recreating the Dead: Relational Distance and Acceptance

- **Authors**: Akiko Orita
- **Date / sources**: 2026-11-18 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/2a9dc56113f4967b9f7978ecac67ac903695f6d8) · [PDF](https://doi.org/10.34190/icair.7.1.5179)

Emerging AI technologies allow deceased individuals to be recreated through enhanced images, voice cloning, conversational agents, and AI-generated video, thereby raising urgent questions regarding who may be recreated after death and whether public acceptance adheres to any consistent logic. This exploratory study addresses the following two research questions (RQs): RQ1. Is acceptance patterned across recreation…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
