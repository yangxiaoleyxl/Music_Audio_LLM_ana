# Music / Audio Foundation Model Research Radar — 2026-11-20

> Lookback window: 2026-11-13 to 2026-11-20 · New papers: 5 · New models: 17 · relevant papers/models in window: 36/52 · raw papers/models: 140/353

Sources: arxiv=81 · semantic_scholar=59 · huggingface_models=353

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [moonbox-dev/HeartMuLa-oss-3B-ONNX](https://huggingface.co/moonbox-dev/HeartMuLa-oss-3B-ONNX) | 2026-11-20 | text-to-audio | 59 | 1 | 0 | 0 | apache-2.0 |
| 2 | [snkii/Sori-1B-MCQ](https://huggingface.co/snkii/Sori-1B-MCQ) | 2026-11-20 | audio-text-to-text | 53 | 1 | 2 | 6 | other |
| 3 | [moonbox-dev/stable-audio-3-medium-MLX](https://huggingface.co/moonbox-dev/stable-audio-3-medium-MLX) | 2026-11-20 | text-to-audio | 44 | 1 | 0 | 0 | other |
| 4 | [moonbox-dev/DiffRhythm2-ONNX](https://huggingface.co/moonbox-dev/DiffRhythm2-ONNX) | 2026-11-20 | text-to-audio | 44 | 1 | 0 | 0 | apache-2.0 |
| 5 | [snkii/Sori-10B-Speech](https://huggingface.co/snkii/Sori-10B-Speech) | 2026-11-20 | audio-text-to-text | 43 | 1 | 0 | 1 | cc-by-nc-sa-4.0 |
| 6 | [snkii/Sori-1B](https://huggingface.co/snkii/Sori-1B) | 2026-11-20 | audio-text-to-text | 40 | 1 | 2 | 34 | other |
| 7 | [keyvan-ai/Saturn-Duplex-5B-DE](https://huggingface.co/keyvan-ai/Saturn-Duplex-5B-DE) | 2026-11-20 | audio-to-audio | 33 | 1 | 0 | 1 | cc-by-nc-nd-4.0 |
| 8 | [Twu31/Haru-4B-MLP-GPTQ-W4A16-G32-Lab](https://huggingface.co/Twu31/Haru-4B-MLP-GPTQ-W4A16-G32-Lab) | 2026-11-20 | audio-to-audio | 27 | 1 | 5 | 0 | apache-2.0 |
| 9 | [on1onmangoes/Haru-4B](https://huggingface.co/on1onmangoes/Haru-4B) | 2026-11-20 | audio-to-audio | 27 | 1 | 0 | 0 | apache-2.0 |
| 10 | [TheStinger/Ilaria_RVC](https://huggingface.co/TheStinger/Ilaria_RVC) | 2026-11-20 | audio-to-audio | 21 | 1 | 0 | 1 | mit |
| 11 | [empiriolabsai/kokoro-dutch](https://huggingface.co/empiriolabsai/kokoro-dutch) | 2026-11-20 | text-to-speech | 19 | 4 | 0 | 0 | apache-2.0 |
| 12 | [mimba/mimba-tune](https://huggingface.co/mimba/mimba-tune) | 2026-11-20 | text-to-audio | 14 | 1 | 0 | 0 | other |
| 13 | [neurarank/voice-ai-s2s](https://huggingface.co/neurarank/voice-ai-s2s) | 2026-11-20 | audio-to-audio | 13 | 1 | 172 | 0 | apache-2.0 |
| 14 | [ali-kuba/tropa-voice-mini-onnx](https://huggingface.co/ali-kuba/tropa-voice-mini-onnx) | 2026-11-20 | audio-classification | 13 | 1 | 0 | 0 | apache-2.0 |
| 15 | [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF) | 2026-11-20 | automatic-speech-recognition | 10 | 1 | 23 | 2 | other |
| 16 | [SpeechTek/speechllm_fama_meusli_villanova_multitask_v1](https://huggingface.co/SpeechTek/speechllm_fama_meusli_villanova_multitask_v1) | 2026-11-20 | automatic-speech-recognition | 10 | 1 | 0 | 0 | cc-by-4.0 |
| 17 | [huybik/hibiki-zero-vi-full-sft](https://huggingface.co/huybik/hibiki-zero-vi-full-sft) | 2026-11-20 | audio-to-audio | 9 | 1 | 0 | 1 | cc-by-nc-sa-4.0 |

### Model cards

#### M1. moonbox-dev/HeartMuLa-oss-3B-ONNX

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: text-to-audio / onnx
- **Relevance**: 59 pts · Generative Music & Audio: text-to-music, text to music, music generation; Music Foundation Models & Representations: music foundation model, music language model; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2601.10547](https://arxiv.org/abs/2601.10547)
- **Datasets / base models**: unknown / HeartMuLa/HeartMuLa-oss-3B
- **Variants in family**: —

#### M2. snkii/Sori-1B-MCQ

- **Created / updated**: 2026-09-18 / 2026-11-20
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 53 pts · Audio Understanding & Reasoning: audio question answering, audio understanding, audio-text (pipeline tag); Audio & Speech Language Models: audio language model, audio-language model; declares license other
- **Adoption signals**: downloads=2 · likes=6 · trending=0.0
- **License / access**: other / gated
- **Related papers**: —
- **Datasets / base models**: unknown / LiquidAI/LFM2.5-Encoder-350M, nvidia/audio-flamingo-next-hf
- **Variants in family**: —

#### M3. moonbox-dev/stable-audio-3-medium-MLX

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: text-to-audio / mlx
- **Relevance**: 44 pts · Generative Music & Audio: text-to-music, text to music, audio generation; model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2605.17991](https://arxiv.org/abs/2605.17991)
- **Datasets / base models**: unknown / stabilityai/stable-audio-3-medium
- **Variants in family**: —

#### M4. moonbox-dev/DiffRhythm2-ONNX

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: text-to-audio / onnx
- **Relevance**: 44 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2510.22950](https://arxiv.org/abs/2510.22950) · [arXiv:2503.01183](https://arxiv.org/abs/2503.01183)
- **Datasets / base models**: unknown / ASLP-lab/DiffRhythm2
- **Variants in family**: —

#### M5. snkii/Sori-10B-Speech

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 43 pts · Audio & Speech Language Models: audio language model, audio-language model, speech llm; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.5-9B, Qwen/Qwen3-Omni-30B-A3B-Instruct
- **Variants in family**: —

#### M6. snkii/Sori-1B

- **Created / updated**: 2026-08-28 / 2026-11-20
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 40 pts · Audio & Speech Language Models: audio language model, audio-language model; Audio Understanding & Reasoning: audio understanding, audio-text (pipeline tag); declares license other; community likes 34
- **Adoption signals**: downloads=2 · likes=34 · trending=0.0
- **License / access**: other / gated
- **Related papers**: —
- **Datasets / base models**: unknown / LiquidAI/LFM2.5-350M-Base, LiquidAI/LFM2.5-Encoder-350M, nvidia/audio-flamingo-next-hf
- **Variants in family**: —

#### M7. keyvan-ai/Saturn-Duplex-5B-DE

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license cc-by-nc-nd-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-nd-4.0 / public
- **Related papers**: —
- **Datasets / base models**: deepset/germanquad, OpenAssistant/oasst2, wikimedia/wikipedia, BrunoHays/callhome-telephony / higurashi-ai/Haru-4B
- **Variants in family**: —

#### M8. Twu31/Haru-4B-MLP-GPTQ-W4A16-G32-Lab

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=5 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: shenyunhang/AISHELL-4 / higurashi-ai/Haru-4B
- **Variants in family**: —

#### M9. on1onmangoes/Haru-4B

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M10. TheStinger/Ilaria_RVC

- **Created / updated**: 2026-11-01 / 2026-11-20
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: text-to-speech; Audio Understanding & Reasoning: audio-text; declares license mit
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M11. empiriolabsai/kokoro-dutch

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: text-to-speech / kokoro
- **Relevance**: 19 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / hexgrad/Kokoro-82M
- **Variants in family**: empiriolabsai/kokoro-polish, empiriolabsai/kokoro-turkish, empiriolabsai/kokoro-korean

#### M12. mimba/mimba-tune

- **Created / updated**: 2026-11-07 / 2026-11-20
- **Task / library**: text-to-audio / peft
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / gated
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5
- **Variants in family**: —

#### M13. neurarank/voice-ai-s2s

- **Created / updated**: 2026-11-17 / 2026-11-20
- **Task / library**: audio-to-audio / transformers
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=172 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M14. ali-kuba/tropa-voice-mini-onnx

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: audio-classification / onnx
- **Relevance**: 13 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / wasitaigeneratedcom/ai-voice-detector-small
- **Variants in family**: —

#### M15. nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF

- **Created / updated**: 2026-10-21 / 2026-11-20
- **Task / library**: automatic-speech-recognition / unknown
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license other
- **Adoption signals**: downloads=23 · likes=2 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
- **Variants in family**: —

#### M16. SpeechTek/speechllm_fama_meusli_villanova_multitask_v1

- **Created / updated**: 2026-11-20 / 2026-11-20
- **Task / library**: automatic-speech-recognition / pytorch
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: mozilla-foundation/common_voice_17_0, google/fleurs, facebook/multilingual_librispeech, openslr/librispeech_asr / FBK-MT/fama-medium-asr, VillanovaAI/Villanova-2B-2603, SpeechTek/MEUSLI_projector_v2_Villanova_2B
- **Variants in family**: —

#### M17. huybik/hibiki-zero-vi-full-sft

- **Created / updated**: 2026-07-29 / 2026-11-20
- **Task / library**: audio-to-audio / moshi
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: speech translation; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/hibiki-zero-3b-pytorch-bf16
- **Variants in family**: —

## Research signals

- Evaluation, Alignment, Safety & Copyright: 2 papers
- Audio & Speech Language Models: 2 papers
- Speech Generation, Recognition & Dialogue: 1 papers
- Generative Music & Audio: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [The landscape of AI speech generation and deepfake detection](https://arxiv.org/abs/2611.24993) | 2026-11-18 | 16 | Speech Generation, Recognition & Dialogue, Evaluation, Alignment, Safety & Copyright | — |
| 2 | [When Sounds Turn Heads: Recovering Event Timing That Audio LLMs Fail to Say](https://arxiv.org/abs/2611.25960) | 2026-11-19 | 15 | Audio & Speech Language Models | — |
| 3 | [From Attention to Semantics: Detecting and Mitigating Sound Event Hallucinations in Large Audio-Language Models](https://arxiv.org/abs/2611.25789) | 2026-11-19 | 14 | Audio & Speech Language Models | — |
| 4 | [Audio deepfake detection: a comprehensive survey of features and models](https://www.semanticscholar.org/paper/2ed4b47ca1963817531d5a4b5f7e4b8c211c1767) | 2026-11-20 | 12 | Evaluation, Alignment, Safety & Copyright | — |
| 5 | [Joint Language Modeling for In-the-Wild Speech-Scene Generation with Distinct Token Representations](https://arxiv.org/abs/2611.25503) | 2026-11-19 | 7 | Generative Music & Audio | — |

## Paper cards

### 1. The landscape of AI speech generation and deepfake detection

- **Authors**: Simon King
- **Date / sources**: 2026-11-18 · arxiv
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: speech generation; Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Links**: [Paper](https://arxiv.org/abs/2611.24993) · [PDF](https://arxiv.org/pdf/2611.24993v1)

Synthetic speech has reached a level of naturalness that can deceive listeners into believing they are hearing natural speech. This opens up the possibility of using synthetic speech deepfakes to mislead both human listeners and automated systems. One response to this threat is to attempt to automatically detect deepfakes. This report offers the reader a self-contained overview of the landscape of synthetic speech…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. When Sounds Turn Heads: Recovering Event Timing That Audio LLMs Fail to Say

- **Authors**: Jongbhin Woo, Jaewook Jeong, Joon Son Chung
- **Date / sources**: 2026-11-19 · arxiv, semantic_scholar
- **Relevance**: 15 pts · Audio & Speech Language Models: audio llm; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.25960) · [PDF](https://arxiv.org/pdf/2611.25960v1)

Audio LLMs can know when a queried sound occurs but fail to say it. We find a few attention heads that track the queried sound: they shift when the query changes, follow the sound when it moves, and removing or blocking them often hurts the model's timestamps. Yet the answer does not express what they track. Intervals read directly from these heads outperform the model's original answer and recover events that its…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. From Attention to Semantics: Detecting and Mitigating Sound Event Hallucinations in Large Audio-Language Models

- **Authors**: Tianyi Sun, Minghao Lv, Chunyang Yu, Shenyue Wang, Mengyue Wu
- **Date / sources**: 2026-11-19 · arxiv
- **Relevance**: 14 pts · Audio & Speech Language Models: audio-language model
- **Links**: [Paper](https://arxiv.org/abs/2611.25789) · [PDF](https://arxiv.org/pdf/2611.25789v1)

Large Audio-Language Models (LALMs) excel at diverse audio tasks, yet remain prone to hallucinating sound events absent from the input. Prior work links such hallucinations to insufficient audio attention. However, we find that real and hallucinated events can receive comparable audio attention mass while attending to different audio positions. To examine whether the attended representations support the generated…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Audio deepfake detection: a comprehensive survey of features and models

- **Authors**: Bhagyashree Chauhan, Bhavesh Borisaniya
- **Date / sources**: 2026-11-20 · semantic_scholar
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake
- **Links**: [Paper](https://www.semanticscholar.org/paper/2ed4b47ca1963817531d5a4b5f7e4b8c211c1767)

No abstract

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Joint Language Modeling for In-the-Wild Speech-Scene Generation with Distinct Token Representations

- **Authors**: Semin Kim, Ju Yeon Kang, Sunghwan Ahn, Seonuk Kim, Nam Soo Kim
- **Date / sources**: 2026-11-19 · arxiv, semantic_scholar
- **Relevance**: 7 pts · Generative Music & Audio: neural audio codec; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.25503) · [PDF](https://arxiv.org/pdf/2611.25503v1)

Speech-scene generation aims to synthesize intelligible target speech together with diverse environmental sounds as a coherent acoustic scene. The task is considered challenging in two respects. Speech and environmental audio differ substantially in their semantic and acoustic characteristics, yet existing approaches typically model the complete scene using a single mixed acoustic representation. At the same time,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
