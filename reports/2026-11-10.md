# Music / Audio Foundation Model Research Radar — 2026-11-10

> Lookback window: 2026-11-03 to 2026-11-10 · New papers: 21 · New models: 24 · relevant papers/models in window: 49/48 · raw papers/models: 159/330

Sources: arxiv=72 · semantic_scholar=87 · huggingface_models=330

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [openmartdev/AwakenFullDuplex-FunAudioChat](https://huggingface.co/openmartdev/AwakenFullDuplex-FunAudioChat) | 2026-11-09 | audio-to-audio | 53 | 1 | 44 | 2 | apache-2.0 |
| 2 | [goldhub/Ruach_Studio_Models_v2](https://huggingface.co/goldhub/Ruach_Studio_Models_v2) | 2026-11-09 | text-to-audio | 44 | 3 | 16109 | 18 | other |
| 3 | [arpanpathak/staleynet-checkpoints](https://huggingface.co/arpanpathak/staleynet-checkpoints) | 2026-11-09 | text-to-audio | 42 | 1 | 0 | 2 | cc-by-sa-4.0 |
| 4 | [LouisAmas/acestep-1.5-xl-sft-lora-ambient-downtempo](https://huggingface.co/LouisAmas/acestep-1.5-xl-sft-lora-ambient-downtempo) | 2026-11-09 | text-to-audio | 32 | 2 | 0 | 0 | mit |
| 5 | [mradermacher/LFM3-Omni-2B-heretic-GGUF](https://huggingface.co/mradermacher/LFM3-Omni-2B-heretic-GGUF) | 2026-11-09 | text-to-speech | 27 | 2 | 313 | 1 | other |
| 6 | [KeraAI/Kera](https://huggingface.co/KeraAI/Kera) | 2026-11-09 | text-to-speech | 25 | 1 | 0 | 2 | apache-2.0 |
| 7 | [JinchuanTian/LongCap-35B-A3B](https://huggingface.co/JinchuanTian/LongCap-35B-A3B) | 2026-11-09 | audio-text-to-text | 25 | 1 | 7 | 0 | apache-2.0 |
| 8 | [JinchuanTian/LongCap-35B-A3B-FP8](https://huggingface.co/JinchuanTian/LongCap-35B-A3B-FP8) | 2026-11-09 | audio-text-to-text | 25 | 1 | 6 | 0 | apache-2.0 |
| 9 | [mehdi-hf/pocket-tts-farsi-v2](https://huggingface.co/mehdi-hf/pocket-tts-farsi-v2) | 2026-11-09 | text-to-speech | 24 | 1 | 0 | 51 | cc-by-nc-4.0 |
| 10 | [Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini) | 2026-11-10 | text-to-speech | 16 | 1 | 0 | 11 | apache-2.0 |
| 11 | [remsky/kokoro-inno-clone-tuner](https://huggingface.co/remsky/kokoro-inno-clone-tuner) | 2026-11-09 | text-to-speech | 16 | 1 | 1581783 | 39 | apache-2.0 |
| 12 | [Solidaxel/Qwen3-TTS-GGUF](https://huggingface.co/Solidaxel/Qwen3-TTS-GGUF) | 2026-11-09 | text-to-speech | 15 | 1 | 4686 | 5 | apache-2.0 |
| 13 | [PleasedPenguin/personaplex-gaze-poster](https://huggingface.co/PleasedPenguin/personaplex-gaze-poster) | 2026-11-09 | audio-to-audio | 15 | 1 | 0 | 1 | other |
| 14 | [wasitaigeneratedcom/ai-voice-detector-small](https://huggingface.co/wasitaigeneratedcom/ai-voice-detector-small) | 2026-11-09 | audio-classification | 15 | 1 | 9 | 0 | apache-2.0 |
| 15 | [starrydark/BanG_Dream_Qwen3_TTS](https://huggingface.co/starrydark/BanG_Dream_Qwen3_TTS) | 2026-11-09 | text-to-speech | 13 | 1 | 54 | 1 | other |
| 16 | [lushy/fastspeech2-ljspeech](https://huggingface.co/lushy/fastspeech2-ljspeech) | 2026-11-09 | text-to-speech | 13 | 1 | 0 | 1 | other |
| 17 | [popsi2/supertonic-3](https://huggingface.co/popsi2/supertonic-3) | 2026-11-09 | text-to-speech | 11 | 1 | 0 | 0 | openrail |
| 18 | [samuelolubukun/murivo-tts-21m-igbo](https://huggingface.co/samuelolubukun/murivo-tts-21m-igbo) | 2026-11-09 | text-to-speech | 11 | 1 | 0 | 0 | apache-2.0 |
| 19 | [samuelolubukun/murivo-tts-21m-hausa](https://huggingface.co/samuelolubukun/murivo-tts-21m-hausa) | 2026-11-09 | text-to-speech | 11 | 1 | 0 | 0 | apache-2.0 |
| 20 | [samuelolubukun/murivo-tts-21m-yoruba](https://huggingface.co/samuelolubukun/murivo-tts-21m-yoruba) | 2026-11-09 | text-to-speech | 11 | 1 | 0 | 0 | apache-2.0 |
| 21 | [samuelolubukun/murivo-tts-21m-english](https://huggingface.co/samuelolubukun/murivo-tts-21m-english) | 2026-11-09 | text-to-speech | 11 | 1 | 0 | 0 | apache-2.0 |
| 22 | [adwumatech-ai/nebula-st-twi-en](https://huggingface.co/adwumatech-ai/nebula-st-twi-en) | 2026-11-09 | automatic-speech-recognition | 10 | 1 | 0 | 0 | cc-by-4.0 |
| 23 | [huybik/hibiki-zero-vi-full-sft](https://huggingface.co/huybik/hibiki-zero-vi-full-sft) | 2026-11-10 | audio-to-audio | 9 | 1 | 0 | 1 | cc-by-nc-sa-4.0 |
| 24 | [gertelrina/aadd](https://huggingface.co/gertelrina/aadd) | 2026-11-09 | audio-classification | 7 | 1 | 0 | 1 | mit |

### Model cards

#### M1. openmartdev/AwakenFullDuplex-FunAudioChat

- **Created / updated**: 2026-11-04 / 2026-11-09
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 53 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; Audio & Speech Language Models: audio language model, audio-language model; declares license apache-2.0
- **Adoption signals**: downloads=44 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / FunAudioLLM/Fun-Audio-Chat-8B
- **Variants in family**: —

#### M2. goldhub/Ruach_Studio_Models_v2

- **Created / updated**: 2026-10-04 / 2026-11-09
- **Task / library**: text-to-audio / ggml
- **Relevance**: 44 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=16109 · likes=18 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2503.08638](https://arxiv.org/abs/2503.08638)
- **Datasets / base models**: unknown / m-a-p/YuE2-3B
- **Variants in family**: goldhub/YuE2-RS-Finetunes, goldhub/Ruach_Studio_LoRAs

#### M3. arpanpathak/staleynet-checkpoints

- **Created / updated**: 2026-11-04 / 2026-11-09
- **Task / library**: text-to-audio / unknown
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license cc-by-sa-4.0
- **Adoption signals**: downloads=0 · likes=2 · trending=0.0
- **License / access**: cc-by-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M4. LouisAmas/acestep-1.5-xl-sft-lora-ambient-downtempo

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: text-to-audio / peft
- **Relevance**: 32 pts · Generative Music & Audio: text-to-music, text to music, text-to-audio (pipeline tag); declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/acestep-v15-xl-sft
- **Variants in family**: LouisAmas/acestep-1.5-xl-sft-lora-90s-trance

#### M5. mradermacher/LFM3-Omni-2B-heretic-GGUF

- **Created / updated**: 2026-11-08 / 2026-11-09
- **Task / library**: text-to-speech / transformers
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning, speech-to-speech; declares license other
- **Adoption signals**: downloads=313 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / rodrigomt/LFM3-Omni-2B-heretic
- **Variants in family**: mradermacher/LFM3-Omni-2B-heretic-i1-GGUF

#### M6. KeraAI/Kera

- **Created / updated**: 2026-11-04 / 2026-11-09
- **Task / library**: text-to-speech / unknown
- **Relevance**: 25 pts · Generative Music & Audio: text-to-audio; Audio Understanding & Reasoning: audio-text; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M7. JinchuanTian/LongCap-35B-A3B

- **Created / updated**: 2026-11-08 / 2026-11-09
- **Task / library**: audio-text-to-text / longcap
- **Relevance**: 25 pts · Audio Understanding & Reasoning: audio captioning, sound event detection, audio-text (pipeline tag); Speech Generation, Recognition & Dialogue: automatic speech recognition; declares license apache-2.0
- **Adoption signals**: downloads=7 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.5-35B-A3B-Base
- **Variants in family**: —

#### M8. JinchuanTian/LongCap-35B-A3B-FP8

- **Created / updated**: 2026-10-26 / 2026-11-09
- **Task / library**: audio-text-to-text / longcap
- **Relevance**: 25 pts · Audio Understanding & Reasoning: audio captioning, sound event detection, audio-text (pipeline tag); Speech Generation, Recognition & Dialogue: automatic speech recognition; declares license apache-2.0
- **Adoption signals**: downloads=6 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / JinchuanTian/LongCap-35B-A3B
- **Variants in family**: —

#### M9. mehdi-hf/pocket-tts-farsi-v2

- **Created / updated**: 2026-09-12 / 2026-11-09
- **Task / library**: text-to-speech / pocket-tts
- **Relevance**: 24 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-4.0; community likes 51
- **Adoption signals**: downloads=0 · likes=51 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M10. Zyphra/ZONOS3-Mini

- **Created / updated**: 2026-11-09 / 2026-11-10
- **Task / library**: text-to-speech / zonos2
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0; community likes 11
- **Adoption signals**: downloads=0 · likes=11 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M11. remsky/kokoro-inno-clone-tuner

- **Created / updated**: 2026-08-31 / 2026-11-09
- **Task / library**: text-to-speech / unknown
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0; community likes 39
- **Adoption signals**: downloads=1581783 · likes=39 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: parler-tts/libritts_r_filtered, facebook/voxpopuli, amphion/Emilia-Dataset / hexgrad/Kokoro-82M
- **Variants in family**: —

#### M12. Solidaxel/Qwen3-TTS-GGUF

- **Created / updated**: 2026-04-26 / 2026-11-09
- **Task / library**: text-to-speech / gguf
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=4686 · likes=5 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3-TTS-12Hz-1.7B-Base
- **Variants in family**: —

#### M13. PleasedPenguin/personaplex-gaze-poster

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: audio-to-audio / moshi
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: full duplex speech; declares license other
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / nvidia/personaplex-7b-v1
- **Variants in family**: —

#### M14. wasitaigeneratedcom/ai-voice-detector-small

- **Created / updated**: 2026-11-08 / 2026-11-09
- **Task / library**: audio-classification / transformers
- **Relevance**: 15 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=9 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2503.02857](https://arxiv.org/abs/2503.02857) · [arXiv:2203.16263](https://arxiv.org/abs/2203.16263) · [arXiv:2410.04324](https://arxiv.org/abs/2410.04324)
- **Datasets / base models**: unknown / facebook/wav2vec2-xls-r-300m
- **Variants in family**: —

#### M15. starrydark/BanG_Dream_Qwen3_TTS

- **Created / updated**: 2026-11-06 / 2026-11-09
- **Task / library**: text-to-speech / qwen-tts
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=54 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2601.15621](https://arxiv.org/abs/2601.15621)
- **Datasets / base models**: unknown / Qwen/Qwen3-TTS-12Hz-1.7B-Base
- **Variants in family**: —

#### M16. lushy/fastspeech2-ljspeech

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: text-to-speech / pytorch
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2006.04558](https://arxiv.org/abs/2006.04558) · [arXiv:2203.02395](https://arxiv.org/abs/2203.02395)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M17. popsi2/supertonic-3

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: text-to-speech / supertonic
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license openrail
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: openrail / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M18. samuelolubukun/murivo-tts-21m-igbo

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: multilingual-tts/open-bible, benjaminogbonna/nigerian_common_voice_dataset / unknown
- **Variants in family**: —

#### M19. samuelolubukun/murivo-tts-21m-hausa

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: multilingual-tts/open-bible, benjaminogbonna/nigerian_common_voice_dataset / unknown
- **Variants in family**: —

#### M20. samuelolubukun/murivo-tts-21m-yoruba

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: multilingual-tts/open-bible, benjaminogbonna/nigerian_common_voice_dataset / unknown
- **Variants in family**: —

#### M21. samuelolubukun/murivo-tts-21m-english

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: keithito/lj_speech / unknown
- **Variants in family**: —

#### M22. adwumatech-ai/nebula-st-twi-en

- **Created / updated**: 2026-11-09 / 2026-11-09
- **Task / library**: automatic-speech-recognition / unknown
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M23. huybik/hibiki-zero-vi-full-sft

- **Created / updated**: 2026-07-29 / 2026-11-10
- **Task / library**: audio-to-audio / moshi
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: speech translation; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/hibiki-zero-3b-pytorch-bf16
- **Variants in family**: —

#### M24. gertelrina/aadd

- **Created / updated**: 2026-11-05 / 2026-11-09
- **Task / library**: audio-classification / pytorch
- **Relevance**: 7 pts · Audio Understanding & Reasoning: sound event detection; declares license mit
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: openslr/librispeech_asr, istupakov/russian_librispeech / openai/whisper-small
- **Variants in family**: —

## Research signals

- Audio Understanding & Reasoning: 6 papers
- Speech Generation, Recognition & Dialogue: 5 papers
- Evaluation, Alignment, Safety & Copyright: 5 papers
- Audio & Speech Language Models: 4 papers
- Generative Music & Audio: 4 papers
- Music Foundation Models & Representations: 3 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [OmniDTBC: Dynamic Token Budget Compression for Video-Audio Large Language Model](https://www.semanticscholar.org/paper/77b4b877ece76cfc11453529402e24491c505ff4) | 2026-11-10 | 21 | Audio & Speech Language Models, Audio Understanding & Reasoning | — |
| 2 | [WaveShield: The First-Place Solution for Robust Speech Deepfake Detection in the AT-ADD 2026 Track 1 Challenge](https://www.semanticscholar.org/paper/9df121223c8d598b8cb721fd51f3b0315c3066d2) | 2026-11-10 | 17 | Speech Generation, Recognition & Dialogue, Evaluation, Alignment, Safety & Copyright | — |
| 3 | [Discrete Coding and Masked Modeling for Text-to-Stereo Audio Generation](https://www.semanticscholar.org/paper/e737eba2983f80271ab81a7e7467e7a515a86253) | 2026-11-10 | 17 | Generative Music & Audio | — |
| 4 | [Acoustic Microcues: Breath and Phoneme-Level Signals for Detecting Audio Deepfakes](https://www.semanticscholar.org/paper/5571161d1c24ee5e3db67a96400ce346042e6aaa) | 2026-11-09 | 17 | Speech Generation, Recognition & Dialogue, Evaluation, Alignment, Safety & Copyright | — |
| 5 | [Improving Large Audio-Language Model Embedding Baselines for Instruction-Aware Speech Retrieval](https://arxiv.org/abs/2611.09122) | 2026-11-06 | 17 | Audio & Speech Language Models | [repo](https://github.com/lca0503/IRIS) |
| 6 | [AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models](https://arxiv.org/abs/2611.09351) | 2026-11-06 | 15 | Generative Music & Audio | — |
| 7 | [PAMU: Personalized Affective Music Generation Using U-Transformer with EEG-driven Multimodal Control](https://www.semanticscholar.org/paper/1ac8874b3a45c77b9e37c7d2cc0ae3569d876e0a) | 2026-11-09 | 14 | Music Foundation Models & Representations, Generative Music & Audio | — |
| 8 | [Q2-Loc: Multimodal Query-Conditioned Binaural Sound Source Localization](https://www.semanticscholar.org/paper/6913281b269c6c15c2456683c169d0473fdb88a1) | 2026-11-10 | 13 | Audio & Speech Language Models | — |
| 9 | [Conflict-Aware Meta-Learning for Generalizable Speech Deepfake Detection](https://arxiv.org/abs/2611.08758) | 2026-11-05 | 13 | Evaluation, Alignment, Safety & Copyright | — |
| 10 | [MP-ADD: Multi-Prototype Authenticity Modeling with Decoupled Learning for Generalizable Audio Deepfake Detection](https://www.semanticscholar.org/paper/0727ffc27073df521cbd02395b00a80129d03077) | 2026-11-10 | 12 | Evaluation, Alignment, Safety & Copyright | — |
| 11 | [Every Victim Tells a Dialogue: Reconstructing 80K Audio-Text Anti-Fraud Conversations from Case Narratives](https://www.semanticscholar.org/paper/3d429627123ac425c607b9964cc23cc6ca464e00) | 2026-11-10 | 12 | Audio Understanding & Reasoning | [repo](https://github.com/Henryhe09/FraudRecon) |
| 12 | [ECAQ: Evidence-Constrained Audio Deepfake Answering with Artifact-Query Detection](https://www.semanticscholar.org/paper/757b31527951cae24e790b7d8e00446a46e4551b) | 2026-11-10 | 12 | Evaluation, Alignment, Safety & Copyright | — |
| 13 | [FoleyForge: Free-form, Controllable, Rectified-flow Editing of Sound Effects](https://arxiv.org/abs/2611.08695) | 2026-11-05 | 12 | Audio & Speech Language Models, Generative Music & Audio | — |
| 14 | [Dynamic Margin CLAP: Adaptive Positive-Pair Margins for Audio-Text Retrieval](https://www.semanticscholar.org/paper/1e227204bf25b0c9076725a90d619b4b722319af) | 2026-11-10 | 10 | Audio Understanding & Reasoning | — |
| 15 | [SportVISTA: Scaling Multimodal Audio-Visual Representation Learning to Amateur and Semi-Professional Sports Videos](https://www.semanticscholar.org/paper/99f0968fb534bf7e000e0457721a2fa69ef26f0b) | 2026-11-09 | 10 | Audio Understanding & Reasoning | — |
| 16 | [SPDMX: Large-Scale Open Stem Audio From Symbolic Music](https://arxiv.org/abs/2611.09140) | 2026-11-06 | 9 | Music Foundation Models & Representations | — |
| 17 | [Audio-Only Turn-Taking with Language Model Semantics](https://www.semanticscholar.org/paper/ad8d6c71508f832280c56f65283a65f62b1961b5) | 2026-11-10 | 8 | Audio Understanding & Reasoning, Speech Generation, Recognition & Dialogue | — |
| 18 | [DART: Difficulty-Aware Adaptive Reasoning for Music Information Retrieval](https://www.semanticscholar.org/paper/94ebb8973b80c81ecdbb5a28922f027c4fac8f4c) | 2026-11-10 | 6 | Music Foundation Models & Representations | — |
| 19 | [Impairments and Variability in Auditory-Motor Synchronization in Individuals With Aphasia and With Advancing Age.](https://www.semanticscholar.org/paper/9025c2bc123319c5657b32472211cbcffbadb076) | 2026-11-06 | 6 | Speech Generation, Recognition & Dialogue | — |
| 20 | [Bridging Spiking and Continuous Dynamics in Spiking Neural Networks: A Muscle-Inspired Model](https://arxiv.org/abs/2611.09295) | 2026-11-06 | 6 | Speech Generation, Recognition & Dialogue | — |
| 21 | [AudioSphere: Towards Self-Supervised Spatial Audio Representation Models](https://arxiv.org/abs/2611.09275) | 2026-11-06 | 6 | Audio Understanding & Reasoning | [repo](https://github.com/labhamlet/AudioSphere) |

## Paper cards

### 1. OmniDTBC: Dynamic Token Budget Compression for Video-Audio Large Language Model

- **Authors**: Bo-Yang Sheng, Wei Wang, Zongyang Ma, Rui-Hao Gong, Rui Ma, Hai-Feng Xia
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 21 pts · Audio & Speech Language Models: audio large language model; Audio Understanding & Reasoning: audio understanding
- **Links**: [Paper](https://www.semanticscholar.org/paper/77b4b877ece76cfc11453529402e24491c505ff4) · [PDF](https://doi.org/10.1145/3767308.3836332)

Omni-modal Large Language Models (Omni-LLMs) have demonstrated remarkable capabilities in joint video-audio understanding. However, their practical deployment for efficient inference remains challenging due to the substantial computational and latency overhead. The primary difficulty lies in the massive number of tokens generated from multimodal videos, leading to the difficulty of adapting MLLMs to low-resource…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. WaveShield: The First-Place Solution for Robust Speech Deepfake Detection in the AT-ADD 2026 Track 1 Challenge

- **Authors**: Yu-Cheng Mao, Wen Huang, Hou-Jun Huang, Yan-Min Qian
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 17 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake; Speech Generation, Recognition & Dialogue: speech generation
- **Links**: [Paper](https://www.semanticscholar.org/paper/9df121223c8d598b8cb721fd51f3b0315c3066d2) · [PDF](https://doi.org/10.1145/3767308.3836629)

The AT-ADD 2026 Track 1 task evaluates robust speech deepfake detection under realistic domain shifts, acoustic distortions, and unseen speech generation methods. This paper presents WaveShield, the first-place Track 1 solution from Team WaveShield. The submitted countermeasure is a three-subsystem ensemble built on a public w2v-BERT 2.0 self-supervised frontend and three complementary heads: w2vBERT2.0-AASIST,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. Discrete Coding and Masked Modeling for Text-to-Stereo Audio Generation

- **Authors**: Yi-Ming Li, Pei-Wen Sun, Zhen Ye, Jia-Hao Pan, Si-Tong Cheng, Bo-Yi Kang, Jia Dai, Kai Li et al.
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 17 pts · Generative Music & Audio: audio generation, text-to-audio
- **Links**: [Paper](https://www.semanticscholar.org/paper/e737eba2983f80271ab81a7e7467e7a515a86253) · [PDF](https://doi.org/10.1145/3767308.3835212)

Generating spatially coherent stereo audio from text is an important yet underexplored problem in multi-modal generation. While text-to-audio systems have achieved strong performance, conventional neural codecs and generative frameworks often struggle to preserve intricate inter-channel dependencies for stereo signals, resulting in collapsed soundstage. In this paper, we present a unified framework for…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Acoustic Microcues: Breath and Phoneme-Level Signals for Detecting Audio Deepfakes

- **Authors**: Wu-Qiong Han, Amogh Palasamudram, Boo Fullwood, F. Monrose
- **Date / sources**: 2026-11-09 · semantic_scholar
- **Relevance**: 17 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; Speech Generation, Recognition & Dialogue: text-to-speech
- **Links**: [Paper](https://www.semanticscholar.org/paper/5571161d1c24ee5e3db67a96400ce346042e6aaa) · [PDF](https://doi.org/10.1145/3840473.3840514)

Modern voice conversion (VC) and text-to-speech (TTS) systems have reached a point where synthetic speech can no longer be reliably distinguished from genuine voices by human listeners, creating an epistemic challenge for how authenticity is assessed in audio communication. Despite this shift, robust detection methods that operate beyond human perceptual limits or exploit auxiliary signals outside the speech…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Improving Large Audio-Language Model Embedding Baselines for Instruction-Aware Speech Retrieval

- **Authors**: Chen-An Li, Cheng-Han Chiang, Hung-yi Lee
- **Date / sources**: 2026-11-06 · arxiv, semantic_scholar
- **Relevance**: 17 pts · Audio & Speech Language Models: audio-language model; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.09122) · [PDF](https://arxiv.org/pdf/2611.09122v1) · [Code 1](https://github.com/lca0503/IRIS)

Speech retrieval finds relevant spoken documents given a spoken query. The spoken query alone may not reveal the retrieval goal, such as finding an answer or matching speaker identity. Instruction-aware speech retrieval expresses this goal through a natural-language text instruction. Large audio-language models (LALMs) effectively process speech and text, and our analysis shows that different retrieval requirements…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models

- **Authors**: Jiashu Zhang, Jiaming He, Zheming Zhang, Kaizheng Wang, Bing Li, Zhiyuan Zha, Yi Yu
- **Date / sources**: 2026-11-06 · arxiv, semantic_scholar
- **Relevance**: 15 pts · Generative Music & Audio: text-to-audio; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.09351) · [PDF](https://arxiv.org/pdf/2611.09351v1)

Automated red-teaming of text-to-audio models requires test prompts that pass textual screening and expose harmful acoustic content. The central challenge is to connect the sounds produced by the target model to both reusable test generation and prompt revision. Our key idea is to represent test descriptions as structured acoustic plans that organize foreground sounds, context, and vocal attributes. To this end, we…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. PAMU: Personalized Affective Music Generation Using U-Transformer with EEG-driven Multimodal Control

- **Authors**: Yong-Xiang Wang, Yun-Han Tian, Rui Zha, Jing-Yao Wang, Ramesh C. Jain, Wei-Bei Dou, Luntian Mou
- **Date / sources**: 2026-11-09 · semantic_scholar
- **Relevance**: 14 pts · Generative Music & Audio: music generation; Music Foundation Models & Representations: symbolic music
- **Links**: [Paper](https://www.semanticscholar.org/paper/1ac8874b3a45c77b9e37c7d2cc0ae3569d876e0a) · [PDF](https://doi.org/10.1145/3840470.3841782)

Affective music generation is an important topic in affective computing. However, EEG-driven affective music generation faces substantial cross-subject variability, making stable affective control and personalization for unseen subjects challenging. To address this problem, we propose the Personalized Affective Music Generator using a U-Transformer (PAMU), a personalized autoregressive framework that integrates EEG…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. Q2-Loc: Multimodal Query-Conditioned Binaural Sound Source Localization

- **Authors**: Zi-Yang Jiang, Yu Chen, Xin-Yuan Qian, Kai-Nan Chen, Xu-Cheng Yin
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 13 pts · Audio & Speech Language Models: audio large language model, audio tokenization
- **Links**: [Paper](https://www.semanticscholar.org/paper/6913281b269c6c15c2456683c169d0473fdb88a1) · [PDF](https://doi.org/10.1145/3767308.3835098)

Sound source localization (SSL) estimates the positions of active acoustic sources, but conventional SSL is query-agnostic and does not decide which source a user actually wants. We study query-conditioned binaural localization, where the target is specified by a text query, an audio query, or both, and the goal is to identify and localize the queried source over time. The key challenge is that query semantics and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. Conflict-Aware Meta-Learning for Generalizable Speech Deepfake Detection

- **Authors**: Siqing Qin, Kong Aik Lee, Youzhi TU, Eng Siong Chng, Man-Wai Mak
- **Date / sources**: 2026-11-05 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.08758) · [PDF](https://arxiv.org/pdf/2611.08758v1)

Speech deepfake detectors built on large self-supervised learning front-ends achieve high in-domain accuracy, yet suffer degradation under domain shift caused by unseen synthesizers, transmission codecs, or unfamiliar acoustic conditions. Meta-learning, particularly model-agnostic meta-learning for domain generalization (MLDG), addresses this issue by simulating domain shifts. However, applying MLDG directly…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. MP-ADD: Multi-Prototype Authenticity Modeling with Decoupled Learning for Generalizable Audio Deepfake Detection

- **Authors**: Yi-Ming Zhang, Hao-Nan Cheng
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake
- **Links**: [Paper](https://www.semanticscholar.org/paper/0727ffc27073df521cbd02395b00a80129d03077) · [PDF](https://doi.org/10.1145/3767308.3835850)

Rapid advances in artificial intelligence generated content (AIGC) have enabled increasingly realistic synthetic and manipulated speech, making generalizable audio deepfake detection (ADD) essential for multimedia security. Existing ADD systems are often formulated as binary classifiers and may overfit to attack-specific artifacts, leading to degraded performance under unseen attacks and domain shifts. To address…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 11. Every Victim Tells a Dialogue: Reconstructing 80K Audio-Text Anti-Fraud Conversations from Case Narratives

- **Authors**: Jing-Xuan Liu, Hao-Yang He, Xuan Yang, Shu-Yuan Zhu, Ke Li, Hong-Chuan Wu, Lan Yang, Jian Chang et al.
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 12 pts · Audio Understanding & Reasoning: audio-text; has open-source code link
- **Links**: [Paper](https://www.semanticscholar.org/paper/3d429627123ac425c607b9964cc23cc6ca464e00) · [PDF](https://doi.org/10.1145/3767308.3835796) · [Code 1](https://github.com/Henryhe09/FraudRecon)

As telecom fraud increasingly threatens global financial security, the demand for reliable detection models has surged. Advancing these models, however, is severely bottlenecked by two critical challenges: (i) the limited availability of real-world data due to strict privacy regulations on scam recordings; and (ii) poor annotation quality caused by unstructured formats and unstandardized categories. While existing…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 12. ECAQ: Evidence-Constrained Audio Deepfake Answering with Artifact-Query Detection

- **Authors**: Xue-Yan Hu
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake
- **Links**: [Paper](https://www.semanticscholar.org/paper/757b31527951cae24e790b7d8e00446a46e4551b) · [PDF](https://doi.org/10.1145/3767308.3838615)

Audio deepfake detection is evolving from binary classification toward interpretable forensic analysis, where systems are expected not only to determine authenticity but also to identify the acoustic artifacts that support their decision. This paper presents a solution for the TRIDENT Challenge Audio Track based on a two-stage framework. In the first stage, an artifact-aware audio forensic detector models the…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 13. FoleyForge: Free-form, Controllable, Rectified-flow Editing of Sound Effects

- **Authors**: Giovana Morais, Hugo Flores García, Prem Seetharaman, Johannes Imort, Justin Salamon, Magdalena Fuentes, Oriol Nieto
- **Date / sources**: 2026-11-05 · arxiv, semantic_scholar
- **Relevance**: 12 pts · Audio & Speech Language Models: audio language model; Generative Music & Audio: audio generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.08695) · [PDF](https://arxiv.org/pdf/2611.08695v1)

We present FoleyForge, a generative model for instruction-based editing of sound effects. Given an input clip and a free-form instruction describing the desired change, it applies the edit while preserving the input's identity. A single model handles semantic, stylistic, and DSP-like changes. We introduce a data pipeline that guides an audio language model to author both DSP-based acoustic edits and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 14. Dynamic Margin CLAP: Adaptive Positive-Pair Margins for Audio-Text Retrieval

- **Authors**: Hao-Ran Liang, Feng-Shan Liu, Selene Zhu, Yue-Ling Yang, Xuan-Ting Li
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 10 pts · Audio Understanding & Reasoning: audio-text
- **Links**: [Paper](https://www.semanticscholar.org/paper/1e227204bf25b0c9076725a90d619b4b722319af)

No abstract

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 15. SportVISTA: Scaling Multimodal Audio-Visual Representation Learning to Amateur and Semi-Professional Sports Videos

- **Authors**: Lazhar Bouacha, Laurent Wendling, Camille Kurtz
- **Date / sources**: 2026-11-09 · semantic_scholar
- **Relevance**: 10 pts · Audio Understanding & Reasoning: multimodal audio
- **Links**: [Paper](https://www.semanticscholar.org/paper/99f0968fb534bf7e000e0457721a2fa69ef26f0b) · [PDF](https://doi.org/10.1145/3841455.3841528)

Clubs and event organizers serving amateur and semi-professional competitions generate substantial video archives, yet their non-standardized cameras, framing, illumination, sound, and production quality remain under-represented in sports-video computer vision research. We introduce SportVISTA, a corpus of 8,144 indexed MPEG-4 Part 14 (MP4) video files originating mainly from amateur, school, club, and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 16. SPDMX: Large-Scale Open Stem Audio From Symbolic Music

- **Authors**: Phillip Long, Eduardo Escoto, Julian McAuley, Zachary Novack
- **Date / sources**: 2026-11-06 · arxiv, semantic_scholar
- **Relevance**: 9 pts · Music Foundation Models & Representations: symbolic music; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.09140) · [PDF](https://arxiv.org/pdf/2611.09140v1)

Large public datasets have driven recent progress in machine learning, from text and vision to speech and general audio. Music remains an outlier, as copyright blocks redistribution of training audio, while many modern tasks need individual stems rather than mixtures. Existing multitrack resources trade off realism, scale, and licensing, while synthetic alternatives rely on proprietary VSTs or naive open rendering…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 17. Audio-Only Turn-Taking with Language Model Semantics

- **Authors**: Rita Frieske, Yi-Fan Shen, Bertram E. Shi
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 8 pts · Audio Understanding & Reasoning: audio-text; Speech Generation, Recognition & Dialogue: automatic speech recognition
- **Links**: [Paper](https://www.semanticscholar.org/paper/ad8d6c71508f832280c56f65283a65f62b1961b5) · [PDF](https://doi.org/10.1145/3767308.3835771)

Accurate turn-taking prediction from speech is essential for responsive conversational systems. Existing approaches typically rely either on purely acoustic modeling or on semantic information derived from automatic speech recognition (ASR) transcripts. Acoustic models preserve prosodic cues but have limited access to linguistic completeness, whereas text-based models discard fine-grained acoustic information.…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 18. DART: Difficulty-Aware Adaptive Reasoning for Music Information Retrieval

- **Authors**: Wei Lan, Yin-Yi Feng, Zu-Xuan Wu
- **Date / sources**: 2026-11-10 · semantic_scholar
- **Relevance**: 6 pts · Music Foundation Models & Representations: music information retrieval
- **Links**: [Paper](https://www.semanticscholar.org/paper/94ebb8973b80c81ecdbb5a28922f027c4fac8f4c)

No abstract

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 19. Impairments and Variability in Auditory-Motor Synchronization in Individuals With Aphasia and With Advancing Age.

- **Authors**: Kathleen Günzel, O. Tuomainen, Simon Bross, Sandra Hanne, Isabell Wartenburger
- **Date / sources**: 2026-11-06 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: speech-to-speech
- **Links**: [Paper](https://www.semanticscholar.org/paper/9025c2bc123319c5657b32472211cbcffbadb076) · [PDF](https://doi.org/10.1044/2026_jslhr-25-00612)

PURPOSE Auditory-motor synchronization, the ability to align motor output with external auditory input, reflects neural coupling between auditory and motor cortices and supports tracking of the speech envelope and linguistic cues, essential for speech perception and production. In aphasia, disrupted neural coupling may impair synchronization and affect speech and language processing. While domain-general…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 20. Bridging Spiking and Continuous Dynamics in Spiking Neural Networks: A Muscle-Inspired Model

- **Authors**: Maryam Soltani, Philip N. Garner
- **Date / sources**: 2026-11-06 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.09295) · [PDF](https://arxiv.org/pdf/2611.09295v1)

Transforming the spike trains produced by spiking neural networks (SNNs) into continuous signals through biologically inspired mechanisms remains an open challenge in generative and regression tasks. In biological systems, a similar transformation occurs when muscles integrate neural spikes to produce smooth, coordinated movements. Inspired by this mechanism, we introduce a muscle-response model, a biologically…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 21. AudioSphere: Towards Self-Supervised Spatial Audio Representation Models

- **Authors**: Goksenin Yuksel, Marcel van Gerven, Kiki van der Heijden
- **Date / sources**: 2026-11-06 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Audio Understanding & Reasoning: sound event detection; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.09275) · [PDF](https://arxiv.org/pdf/2611.09275v1) · [Code 1](https://github.com/labhamlet/AudioSphere)

Recent audio embedding models learn representations that transfer across clip- and frame-level tasks, yet they operate almost exclusively on single-channel signals and are blind to spatial structure. Spatial audio models capture that structure but rely on clip-level supervision or contrastive objectives, yielding embeddings unsuitable for frame-level tasks like sound event detection and localization (SELD). We argue…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
