# Music / Audio Foundation Model Research Radar — 2026-11-17

> Lookback window: 2026-11-10 to 2026-11-17 · New papers: 3 · New models: 17 · relevant papers/models in window: 41/65 · raw papers/models: 101/315

Sources: arxiv=39 · semantic_scholar=62 · huggingface_models=315

## Source notes

- arXiv / Audio & Speech Language Models: HTTP Error 429: Unknown Error
- arXiv / Generative Music & Audio: HTTP Error 429: Unknown Error
- arXiv / Audio Understanding & Reasoning: The read operation timed out

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [Jakevin/ACE-Step1.5-Qwen3.5-0.8B-MLX](https://huggingface.co/Jakevin/ACE-Step1.5-Qwen3.5-0.8B-MLX) | 2026-11-16 | text-to-audio | 42 | 1 | 0 | 0 | apache-2.0 |
| 2 | [Jayanth-MKV/Haru-4B-GGUF](https://huggingface.co/Jayanth-MKV/Haru-4B-GGUF) | 2026-11-16 | audio-to-audio | 32 | 1 | 0 | 0 | apache-2.0 |
| 3 | [FireH2O/MrJMThaiTTS_CT](https://huggingface.co/FireH2O/MrJMThaiTTS_CT) | 2026-11-16 | text-to-speech | 17 | 1 | 0 | 0 | cc-by-sa-4.0 |
| 4 | [HAizelf/speecht5_tts_voxpopuli_nl](https://huggingface.co/HAizelf/speecht5_tts_voxpopuli_nl) | 2026-11-16 | text-to-speech | 17 | 1 | 0 | 0 | mit |
| 5 | [fotiecodes/turaco-csm-tts-wes-1b](https://huggingface.co/fotiecodes/turaco-csm-tts-wes-1b) | 2026-11-16 | text-to-speech | 17 | 1 | 0 | 0 | apache-2.0 |
| 6 | [mradermacher/Volt-TTS-GGUF](https://huggingface.co/mradermacher/Volt-TTS-GGUF) | 2026-11-16 | text-to-speech | 15 | 1 | 0 | 1 | apache-2.0 |
| 7 | [Igor282/qwen3-tts-12hz-1.7b-ru-pruned-enru-Q4_K_M](https://huggingface.co/Igor282/qwen3-tts-12hz-1.7b-ru-pruned-enru-Q4_K_M) | 2026-11-16 | text-to-speech | 15 | 1 | 0 | 0 | apache-2.0 |
| 8 | [openarcane/Volt-TTS](https://huggingface.co/openarcane/Volt-TTS) | 2026-11-16 | text-to-speech | 15 | 1 | 0 | 0 | apache-2.0 |
| 9 | [Ansu/Latxa-Omni-SNAC-Qwen3.5-4B](https://huggingface.co/Ansu/Latxa-Omni-SNAC-Qwen3.5-4B) | 2026-11-16 | audio-text-to-text | 15 | 1 | 0 | 0 | other |
| 10 | [mimba/mimba-tune](https://huggingface.co/mimba/mimba-tune) | 2026-11-17 | text-to-audio | 14 | 1 | 0 | 0 | other |
| 11 | [akbargherbal/arabmaqamrock-blend-yue2-lora](https://huggingface.co/akbargherbal/arabmaqamrock-blend-yue2-lora) | 2026-11-16 | text-to-audio | 14 | 3 | 0 | 0 | cc-by-nc-4.0 |
| 12 | [laion/Humaneness-Voice-Converter](https://huggingface.co/laion/Humaneness-Voice-Converter) | 2026-11-16 | audio-to-audio | 13 | 1 | 0 | 2 | cc-by-4.0 |
| 13 | [superretrosfx/RVC-MODEL](https://huggingface.co/superretrosfx/RVC-MODEL) | 2026-11-16 | audio-to-audio | 13 | 1 | 0 | 0 | mit |
| 14 | [MAdel121/LFM3-Audio-2B-Full-Duplex](https://huggingface.co/MAdel121/LFM3-Audio-2B-Full-Duplex) | 2026-11-16 | audio-to-audio | 13 | 1 | 0 | 0 | other |
| 15 | [longcap/LongCap_ICLR](https://huggingface.co/longcap/LongCap_ICLR) | 2026-11-16 | automatic-speech-recognition | 12 | 1 | 0 | 0 | apache-2.0 |
| 16 | [litert-community/granite-speech-5.0-2b](https://huggingface.co/litert-community/granite-speech-5.0-2b) | 2026-11-16 | automatic-speech-recognition | 10 | 1 | 225 | 1 | apache-2.0 |
| 17 | [paincupid/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF](https://huggingface.co/paincupid/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF) | 2026-11-16 | automatic-speech-recognition | 10 | 1 | 0 | 0 | other |

### Model cards

#### M1. Jakevin/ACE-Step1.5-Qwen3.5-0.8B-MLX

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: text-to-audio / mlx
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.5-0.8B-Base
- **Variants in family**: —

#### M2. Jayanth-MKV/Haru-4B-GGUF

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 32 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; Generative Music & Audio: audio generation; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / higurashi-ai/Haru-4B
- **Variants in family**: —

#### M3. FireH2O/MrJMThaiTTS_CT

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: text-to-speech / pocket-tts
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license cc-by-sa-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-sa-4.0 / gated
- **Related papers**: [arXiv:2604.27607](https://arxiv.org/abs/2604.27607)
- **Datasets / base models**: pythainlp/som_tts_dataset, CMKL/Porjai-Thai-voice-dataset-central, airesearch/thai-ser / kyutai/pocket-tts
- **Variants in family**: —

#### M4. HAizelf/speecht5_tts_voxpopuli_nl

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: text-to-speech / transformers
- **Relevance**: 17 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: facebook/voxpopuli / microsoft/speecht5_tts
- **Variants in family**: —

#### M5. fotiecodes/turaco-csm-tts-wes-1b

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: text-to-speech / transformers
- **Relevance**: 17 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unsloth/csm-1b
- **Variants in family**: —

#### M6. mradermacher/Volt-TTS-GGUF

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: text-to-speech / transformers
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / openarcane/Volt-TTS
- **Variants in family**: —

#### M7. Igor282/qwen3-tts-12hz-1.7b-ru-pruned-enru-Q4_K_M

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: text-to-speech / qwentts.cpp
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3-TTS-12Hz-1.7B-Base, Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign, siriusfreak/qwen3-tts-12hz-1.7b-ru-stress-cf
- **Variants in family**: —

#### M8. openarcane/Volt-TTS

- **Created / updated**: 2026-11-11 / 2026-11-16
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M9. Ansu/Latxa-Omni-SNAC-Qwen3.5-4B

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: audio-text-to-text / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / HiTZ/Latxa-Qwen3.5-4B, openai/whisper-large-v3, meta-llama/Llama-3.2-1B-Instruct
- **Variants in family**: —

#### M10. mimba/mimba-tune

- **Created / updated**: 2026-11-07 / 2026-11-17
- **Task / library**: text-to-audio / peft
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / gated
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5
- **Variants in family**: —

#### M11. akbargherbal/arabmaqamrock-blend-yue2-lora

- **Created / updated**: 2026-10-13 / 2026-11-16
- **Task / library**: text-to-audio / audiocpp
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / m-a-p/YuE2-3B
- **Variants in family**: akbargherbal/arabic-instrumental-yue2-lora, akbargherbal/arabmaqamrock-yue2-lora

#### M12. laion/Humaneness-Voice-Converter

- **Created / updated**: 2026-10-11 / 2026-11-16
- **Task / library**: audio-to-audio / pytorch
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=2 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / ResembleAI/chatterbox
- **Variants in family**: —

#### M13. superretrosfx/RVC-MODEL

- **Created / updated**: 2025-12-11 / 2026-11-16
- **Task / library**: audio-to-audio / keras-hub
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: voice cloning; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: openbmb/UltraData-SFT-Agent-2609, openbmb/UltraData-RL-2609 / nex-agi/Nex-N2.5-mini
- **Variants in family**: —

#### M14. MAdel121/LFM3-Audio-2B-Full-Duplex

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: audio-to-audio / peft
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / LiquidAI/LFM3-Audio-2B
- **Variants in family**: —

#### M15. longcap/LongCap_ICLR

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: automatic-speech-recognition / unknown
- **Relevance**: 12 pts · Audio Understanding & Reasoning: audio captioning; declares license apache-2.0; Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag)
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M16. litert-community/granite-speech-5.0-2b

- **Created / updated**: 2026-11-06 / 2026-11-16
- **Task / library**: automatic-speech-recognition / litert-lm
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license apache-2.0
- **Adoption signals**: downloads=225 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / ibm-granite/granite-speech-5.0-2b
- **Variants in family**: —

#### M17. paincupid/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF

- **Created / updated**: 2026-11-16 / 2026-11-16
- **Task / library**: automatic-speech-recognition / gguf
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
- **Variants in family**: —

## Research signals

- Audio & Speech Language Models: 1 papers
- Audio Understanding & Reasoning: 1 papers
- Evaluation, Alignment, Safety & Copyright: 1 papers
- Generative Music & Audio: 1 papers
- Speech Generation, Recognition & Dialogue: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [Any Channel Count, One Token Stream: Incorporating Spatial Audio Understanding and Reasoning into Large Audio-Language Models](https://arxiv.org/abs/2611.18112) | 2026-11-13 | 27 | Audio & Speech Language Models, Audio Understanding & Reasoning, Evaluation, Alignment, Safety & Copyright | [repo](https://github.com/Konoyo-014/SpheraQA) |
| 2 | [CoTTAGE: An Explainable Judge for Text-to-Audio Generation](https://arxiv.org/abs/2611.17644) | 2026-11-13 | 24 | Generative Music & Audio | — |
| 3 | [The Cost of Being Out of Sync: How Voice Realism and Lip-Sync Quality Shape Trust and Perception of Virtual Humans](https://www.semanticscholar.org/paper/5fffd685ea4d7bc34d3616a116dacf4c2c2fd8e2) | 2026-11-16 | 10 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. Any Channel Count, One Token Stream: Incorporating Spatial Audio Understanding and Reasoning into Large Audio-Language Models

- **Authors**: Yuhuan You, Wenxiang Guo, Zhifang Guo, Yuxuan Wang, Jin Xu
- **Date / sources**: 2026-11-13 · arxiv, semantic_scholar
- **Relevance**: 27 pts · Audio & Speech Language Models: audio-language model; Audio Understanding & Reasoning: audio understanding; Evaluation, Alignment, Safety & Copyright: audio benchmark; has open-source code link
- **Links**: [Paper](https://arxiv.org/abs/2611.18112) · [PDF](https://arxiv.org/pdf/2611.18112v1) · [Code 1](https://github.com/Konoyo-014/SpheraQA)

Audio phase relations encode source locations, yet existing large audio-language models (LALM) reduce audio to single-channel content to stabilise general audio understanding, leaving spatial information for direction, distance, and source-relation questions unused. We present SpheraAudio, which accepts recordings with any channel count -- mono, stereo, First-Order Ambisonics (FOA), or higher -- and maps them into a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. CoTTAGE: An Explainable Judge for Text-to-Audio Generation

- **Authors**: Yu-Xiang Lin, Yun-Man Hsu, Bo-Ru Lu, Kuan-Po Huang, Wen-Ze Ren, Ming-To Chuang, Chun-Yi Kuan, Jia-Wei Du et al.
- **Date / sources**: 2026-11-13 · semantic_scholar
- **Relevance**: 24 pts · Generative Music & Audio: audio generation, text-to-audio
- **Links**: [Paper](https://arxiv.org/abs/2611.17644)

Rapid progress in text-to-audio (TTA) generation demands reliable and explainable automatic evaluation. However, existing metrics fail to simultaneously deliver high correlation with human judgments and meaningful, audio-grounded explanations, forcing reliance on labor-intensive human evaluation that bottlenecks model development iteration. To address this, we propose CoTTAGE, a reasoning-based evaluator for text…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. The Cost of Being Out of Sync: How Voice Realism and Lip-Sync Quality Shape Trust and Perception of Virtual Humans

- **Authors**: Samer Al Hussban, Nick van Apeldoorn, A. van Buggenum, Niels Voskens, M. Alimardani
- **Date / sources**: 2026-11-16 · semantic_scholar
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: speech synthesis, voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/5fffd685ea4d7bc34d3616a116dacf4c2c2fd8e2) · [PDF](https://doi.org/10.1145/3841580.3841614)

Advancements in artificial intelligence (AI) and virtual human (VH) technologies have enabled highly realistic digital agents, raising users’ expectations for natural interaction. This study investigated how voice-generation realism and lip-sync quality influence user perception and trust in a photorealistic VH. The VH was developed in Unreal Engine using photogrammetry data captured from a real person. The same…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
