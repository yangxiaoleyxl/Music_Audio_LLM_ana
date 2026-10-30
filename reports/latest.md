# Music / Audio Foundation Model Research Radar — 2026-10-30

> Lookback window: 2026-10-23 to 2026-10-30 · New papers: 35 · New models: 30 · relevant papers/models in window: 35/81 · raw papers/models: 149/357

Sources: arxiv=93 · semantic_scholar=56 · huggingface_models=357

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [inclusionAI/Ming-3.0-audio-flash](https://huggingface.co/inclusionAI/Ming-3.0-audio-flash) | 2026-10-29 | audio-to-audio | 52 | 1 | 1053 | 68 | mit |
| 2 | [MiniMaxAI/MiniMax-Music3](https://huggingface.co/MiniMaxAI/MiniMax-Music3) | 2026-10-26 | text-to-audio | 47 | 1 | 5921 | 1490 | unknown |
| 3 | [inclusionAI/Ming-3.0-audio-tiny](https://huggingface.co/inclusionAI/Ming-3.0-audio-tiny) | 2026-10-29 | audio-to-audio | 46 | 1 | 2222 | 53 | mit |
| 4 | [milliwattlabs/YuE2-3B-MLX-4bit](https://huggingface.co/milliwattlabs/YuE2-3B-MLX-4bit) | 2026-10-30 | text-to-audio | 44 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 5 | [yonghyunk1m/TTM-HumanPref](https://huggingface.co/yonghyunk1m/TTM-HumanPref) | 2026-10-24 | text-to-audio | 44 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 6 | [jjcoders/suna-v1](https://huggingface.co/jjcoders/suna-v1) | 2026-10-25 | text-to-audio | 42 | 1 | 1517 | 1 | mit |
| 7 | [Zixchen/FineAudio-Judge](https://huggingface.co/Zixchen/FineAudio-Judge) | 2026-10-27 | audio-text-to-text | 37 | 1 | 20 | 0 | apache-2.0 |
| 8 | [twangodev/Ming-3.0-audio-tiny-NVFP4](https://huggingface.co/twangodev/Ming-3.0-audio-tiny-NVFP4) | 2026-10-26 | audio-text-to-text | 36 | 1 | 83 | 1 | mit |
| 9 | [twangodev/Ming-3.0-audio-flash-NVFP4](https://huggingface.co/twangodev/Ming-3.0-audio-flash-NVFP4) | 2026-10-26 | audio-text-to-text | 36 | 1 | 59 | 0 | mit |
| 10 | [ArchiveStudio/MOSS-Music-8B-Thinking](https://huggingface.co/ArchiveStudio/MOSS-Music-8B-Thinking) | 2026-10-24 | audio-text-to-text | 35 | 1 | 25 | 0 | apache-2.0 |
| 11 | [ArchiveStudio/MOSS-Music-8B-Instruct](https://huggingface.co/ArchiveStudio/MOSS-Music-8B-Instruct) | 2026-10-24 | audio-text-to-text | 35 | 1 | 25 | 0 | apache-2.0 |
| 12 | [QuantumDesk-AI/ultravox-qwen3.6-27b-base](https://huggingface.co/QuantumDesk-AI/ultravox-qwen3.6-27b-base) | 2026-10-26 | audio-text-to-text | 33 | 3 | 149 | 3 | apache-2.0 |
| 13 | [BNarayanaReddy/siba](https://huggingface.co/BNarayanaReddy/siba) | 2026-10-29 | audio-to-audio | 32 | 1 | 0 | 0 | cc-by-4.0 |
| 14 | [RetentionLabs/PolyPlex-14B-CJKE](https://huggingface.co/RetentionLabs/PolyPlex-14B-CJKE) | 2026-10-29 | audio-to-audio | 29 | 1 | 0 | 0 | other |
| 15 | [qqjz/TextPro-SLM-3B-Global](https://huggingface.co/qqjz/TextPro-SLM-3B-Global) | 2026-10-29 | audio-text-to-text | 29 | 1 | 0 | 0 | other |
| 16 | [qqjz/TextPro-SLM-7B-Interleaving](https://huggingface.co/qqjz/TextPro-SLM-7B-Interleaving) | 2026-10-29 | audio-text-to-text | 29 | 1 | 0 | 0 | apache-2.0 |
| 17 | [Muiru/Audio8-TTS-Realistic-0.6b](https://huggingface.co/Muiru/Audio8-TTS-Realistic-0.6b) | 2026-10-30 | text-to-speech | 28 | 1 | 1 | 0 | apache-2.0 |
| 18 | [prakharkhatri/IndiCodec](https://huggingface.co/prakharkhatri/IndiCodec) | 2026-10-29 | audio-to-audio | 27 | 1 | 34 | 2 | apache-2.0 |
| 19 | [agentory/stable-audio-3-small-music-GGUF](https://huggingface.co/agentory/stable-audio-3-small-music-GGUF) | 2026-10-29 | text-to-audio | 26 | 1 | 102 | 0 | other |
| 20 | [third-intelligence/RubatoCodec](https://huggingface.co/third-intelligence/RubatoCodec) | 2026-10-28 | audio-to-audio | 26 | 1 | 266 | 11 | apache-2.0 |
| 21 | [WhissleAI/steer-tts](https://huggingface.co/WhissleAI/steer-tts) | 2026-10-30 | text-to-speech | 24 | 1 | 144 | 16 | cc-by-nc-4.0 |
| 22 | [HirCoir/piper-checkpoint-es-mx-astra](https://huggingface.co/HirCoir/piper-checkpoint-es-mx-astra) | 2026-10-28 | text-to-audio | 21 | 1 | 26 | 0 | unknown |
| 23 | [Im-fin3/hibiki-zero-3b-mlx-q4](https://huggingface.co/Im-fin3/hibiki-zero-3b-mlx-q4) | 2026-10-24 | audio-to-audio | 21 | 1 | 37 | 0 | cc-by-nc-sa-4.0 |
| 24 | [AEmotionStudio/drama-3-models](https://huggingface.co/AEmotionStudio/drama-3-models) | 2026-10-30 | text-to-speech | 20 | 1 | 9 | 0 | other |
| 25 | [wegotomars/OmniVoice-CoreAI-ANE](https://huggingface.co/wegotomars/OmniVoice-CoreAI-ANE) | 2026-10-30 | text-to-speech | 19 | 1 | 41 | 0 | cc-by-nc-4.0 |
| 26 | [NearAndDear98/Audio-R1-Qwen2.5-Omni-7B](https://huggingface.co/NearAndDear98/Audio-R1-Qwen2.5-Omni-7B) | 2026-10-27 | audio-text-to-text | 19 | 1 | 54 | 0 | apache-2.0 |
| 27 | [NearAndDear98/Audio-R1-Gemma-4-E4B-it](https://huggingface.co/NearAndDear98/Audio-R1-Gemma-4-E4B-it) | 2026-10-27 | audio-text-to-text | 19 | 1 | 20 | 0 | apache-2.0 |
| 28 | [NearAndDear98/Audio-R1-AF-Next-Think](https://huggingface.co/NearAndDear98/Audio-R1-AF-Next-Think) | 2026-10-27 | audio-text-to-text | 19 | 1 | 19 | 0 | other |
| 29 | [stabilityai/stable-audio-3-optimized](https://huggingface.co/stabilityai/stable-audio-3-optimized) | 2026-10-30 | text-to-audio | 17 | 1 | 47656 | 62 | other |
| 30 | [LattifAI/YuE2-3B-GGUF](https://huggingface.co/LattifAI/YuE2-3B-GGUF) | 2026-10-30 | text-to-audio | 16 | 1 | 261 | 0 | cc-by-nc-4.0 |

### Model cards

#### M1. inclusionAI/Ming-3.0-audio-flash

- **Created / updated**: 2026-09-03 / 2026-10-29
- **Task / library**: audio-to-audio / transformers
- **Relevance**: 52 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech, automatic speech recognition; Audio Understanding & Reasoning: audio reasoning, audio understanding; declares license mit; community likes 68
- **Adoption signals**: downloads=1053 · likes=68 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M2. MiniMaxAI/MiniMax-Music3

- **Created / updated**: 2026-08-07 / 2026-10-26
- **Task / library**: text-to-audio / diffusers
- **Relevance**: 47 pts · Generative Music & Audio: text-to-music, text to music, music generation; community likes 1490
- **Adoption signals**: downloads=5921 · likes=1490 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M3. inclusionAI/Ming-3.0-audio-tiny

- **Created / updated**: 2026-09-03 / 2026-10-29
- **Task / library**: audio-to-audio / transformers
- **Relevance**: 46 pts · Audio Understanding & Reasoning: audio reasoning, audio understanding; Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech, automatic speech recognition; declares license mit; community likes 53
- **Adoption signals**: downloads=2222 · likes=53 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M4. milliwattlabs/YuE2-3B-MLX-4bit

- **Created / updated**: 2026-09-26 / 2026-10-30
- **Task / library**: text-to-audio / mlx
- **Relevance**: 44 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2503.08638](https://arxiv.org/abs/2503.08638)
- **Datasets / base models**: unknown / m-a-p/YuE2-3B
- **Variants in family**: —

#### M5. yonghyunk1m/TTM-HumanPref

- **Created / updated**: 2026-10-24 / 2026-10-24
- **Task / library**: text-to-audio / pytorch
- **Relevance**: 44 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2606.21670](https://arxiv.org/abs/2606.21670)
- **Datasets / base models**: unknown / AndreasXi/MeanAudio
- **Variants in family**: —

#### M6. jjcoders/suna-v1

- **Created / updated**: 2026-10-11 / 2026-10-25
- **Task / library**: text-to-audio / diffusers
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license mit
- **Adoption signals**: downloads=1517 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M7. Zixchen/FineAudio-Judge

- **Created / updated**: 2026-10-27 / 2026-10-27
- **Task / library**: audio-text-to-text / peft
- **Relevance**: 37 pts · Audio & Speech Language Models: audio language model, audio-language model; Audio Understanding & Reasoning: audio-text; declares license apache-2.0
- **Adoption signals**: downloads=20 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3-Omni-30B-A3B-Instruct
- **Variants in family**: —

#### M8. twangodev/Ming-3.0-audio-tiny-NVFP4

- **Created / updated**: 2026-10-25 / 2026-10-26
- **Task / library**: audio-text-to-text / Model Optimizer
- **Relevance**: 36 pts · Audio Understanding & Reasoning: audio reasoning, audio understanding, audio-text; Speech Generation, Recognition & Dialogue: automatic speech recognition; declares license mit
- **Adoption signals**: downloads=83 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / inclusionAI/Ming-3.0-audio-tiny
- **Variants in family**: —

#### M9. twangodev/Ming-3.0-audio-flash-NVFP4

- **Created / updated**: 2026-10-25 / 2026-10-26
- **Task / library**: audio-text-to-text / Model Optimizer
- **Relevance**: 36 pts · Audio Understanding & Reasoning: audio reasoning, audio understanding, audio-text; Speech Generation, Recognition & Dialogue: automatic speech recognition; declares license mit
- **Adoption signals**: downloads=59 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / inclusionAI/Ming-3.0-audio-flash
- **Variants in family**: —

#### M10. ArchiveStudio/MOSS-Music-8B-Thinking

- **Created / updated**: 2026-10-24 / 2026-10-24
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 35 pts · Audio & Speech Language Models: audio language model, audio-language model; Music Foundation Models & Representations: music understanding; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=25 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M11. ArchiveStudio/MOSS-Music-8B-Instruct

- **Created / updated**: 2026-10-24 / 2026-10-24
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 35 pts · Audio & Speech Language Models: audio language model, audio-language model; Music Foundation Models & Representations: music understanding; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=25 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M12. QuantumDesk-AI/ultravox-qwen3.6-27b-base

- **Created / updated**: 2026-07-07 / 2026-10-26
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 33 pts · Audio & Speech Language Models: speech language model, speech-language model; Speech Generation, Recognition & Dialogue: automatic speech recognition; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=149 · likes=3 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.6-27B, openai/whisper-large-v3-turbo
- **Variants in family**: QuantumDesk-AI/ultravox-qwen3.6-27b-v2, QuantumDesk-AI/ultravox-qwen3.6-27b-v3

#### M13. BNarayanaReddy/siba

- **Created / updated**: 2026-10-28 / 2026-10-29
- **Task / library**: audio-to-audio / moshi
- **Relevance**: 32 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, speech dialogue, full duplex speech; declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/moshiko-pytorch-bf16
- **Variants in family**: —

#### M14. RetentionLabs/PolyPlex-14B-CJKE

- **Created / updated**: 2026-10-24 / 2026-10-29
- **Task / library**: audio-to-audio / transformers
- **Relevance**: 29 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2410.00037](https://arxiv.org/abs/2410.00037) · [arXiv:2602.06053](https://arxiv.org/abs/2602.06053) · [arXiv:2506.02979](https://arxiv.org/abs/2506.02979) · [arXiv:2604.23295](https://arxiv.org/abs/2604.23295) · [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) · [arXiv:2509.25149](https://arxiv.org/abs/2509.25149) · [arXiv:2505.02214](https://arxiv.org/abs/2505.02214)
- **Datasets / base models**: unknown / nvidia/personaplex-7b-v1, Qwen/Qwen3-8B
- **Variants in family**: —

#### M15. qqjz/TextPro-SLM-3B-Global

- **Created / updated**: 2026-10-29 / 2026-10-29
- **Task / library**: audio-text-to-text / pytorch
- **Relevance**: 29 pts · Audio & Speech Language Models: speech language model, speech-language model; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen2.5-3B-Instruct, qqjz/WhisperPro
- **Variants in family**: —

#### M16. qqjz/TextPro-SLM-7B-Interleaving

- **Created / updated**: 2026-10-29 / 2026-10-29
- **Task / library**: audio-text-to-text / pytorch
- **Relevance**: 29 pts · Audio & Speech Language Models: speech language model, speech-language model; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen2.5-7B-Instruct, qqjz/WhisperPro
- **Variants in family**: —

#### M17. Muiru/Audio8-TTS-Realistic-0.6b

- **Created / updated**: 2026-10-30 / 2026-10-30
- **Task / library**: text-to-speech / transformers
- **Relevance**: 28 pts · Speech Generation, Recognition & Dialogue: speech generation, text-to-speech (pipeline tag), voice cloning; Generative Music & Audio: neural audio codec; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=1 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2610.14776](https://arxiv.org/abs/2610.14776)
- **Datasets / base models**: unknown / Edge0/Audio8-TTS-Preview-0.6b
- **Variants in family**: —

#### M18. prakharkhatri/IndiCodec

- **Created / updated**: 2026-10-25 / 2026-10-29
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 27 pts · Audio & Speech Language Models: speech language model, speech-language model; declares license apache-2.0
- **Adoption signals**: downloads=34 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: amphion/Emilia-Dataset, mythicinfinity/libritts, mythicinfinity/libritts_r, CSTR-Edinburgh/vctk, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M19. agentory/stable-audio-3-small-music-GGUF

- **Created / updated**: 2026-10-29 / 2026-10-29
- **Task / library**: text-to-audio / unknown
- **Relevance**: 26 pts · Generative Music & Audio: audio generation, text-to-audio (pipeline tag), music diffusion; declares license other
- **Adoption signals**: downloads=102 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / stabilityai/stable-audio-3-small-music
- **Variants in family**: —

#### M20. third-intelligence/RubatoCodec

- **Created / updated**: 2026-10-20 / 2026-10-28
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 26 pts · Generative Music & Audio: neural audio codec; Speech Generation, Recognition & Dialogue: text-to-speech; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=266 · likes=11 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2610.29434](https://arxiv.org/abs/2610.29434)
- **Datasets / base models**: amphion/Emilia-Dataset, nvidia/hifitts-2, reazon-research/reazonspeech, MLCommons/peoples_speech, facebook/voxpopuli / unknown
- **Variants in family**: —

#### M21. WhissleAI/steer-tts

- **Created / updated**: 2026-10-15 / 2026-10-30
- **Task / library**: text-to-speech / steertts
- **Relevance**: 24 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-4.0; community likes 16
- **Adoption signals**: downloads=144 · likes=16 · trending=0.0
- **License / access**: cc-by-nc-4.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M22. HirCoir/piper-checkpoint-es-mx-astra

- **Created / updated**: 2026-10-23 / 2026-10-28
- **Task / library**: text-to-audio / unknown
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; Generative Music & Audio: text-to-audio (pipeline tag)
- **Adoption signals**: downloads=26 · likes=0 · trending=0.0
- **License / access**: unknown / gated
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M23. Im-fin3/hibiki-zero-3b-mlx-q4

- **Created / updated**: 2026-10-24 / 2026-10-24
- **Task / library**: audio-to-audio / mlx
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: speech translation, speech-to-speech; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=37 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/hibiki-zero-3b-pytorch-bf16
- **Variants in family**: —

#### M24. AEmotionStudio/drama-3-models

- **Created / updated**: 2026-10-29 / 2026-10-30
- **Task / library**: text-to-speech / pytorch
- **Relevance**: 20 pts · Speech Generation, Recognition & Dialogue: speech generation, text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=9 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / fishaudio/drama-3-int4, fishaudio/drama-3
- **Variants in family**: —

#### M25. wegotomars/OmniVoice-CoreAI-ANE

- **Created / updated**: 2026-10-25 / 2026-10-30
- **Task / library**: text-to-speech / coreai
- **Relevance**: 19 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=41 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / k2-fsa/OmniVoice
- **Variants in family**: —

#### M26. NearAndDear98/Audio-R1-Qwen2.5-Omni-7B

- **Created / updated**: 2026-10-27 / 2026-10-27
- **Task / library**: audio-text-to-text / peft
- **Relevance**: 19 pts · Audio Understanding & Reasoning: audio reasoning, audio-text (pipeline tag); model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=54 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2610.34609](https://arxiv.org/abs/2610.34609)
- **Datasets / base models**: unknown / Qwen/Qwen2.5-Omni-7B
- **Variants in family**: —

#### M27. NearAndDear98/Audio-R1-Gemma-4-E4B-it

- **Created / updated**: 2026-10-27 / 2026-10-27
- **Task / library**: audio-text-to-text / peft
- **Relevance**: 19 pts · Audio Understanding & Reasoning: audio reasoning, audio-text (pipeline tag); model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=20 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2610.34609](https://arxiv.org/abs/2610.34609)
- **Datasets / base models**: unknown / google/gemma-4-E4B-it
- **Variants in family**: —

#### M28. NearAndDear98/Audio-R1-AF-Next-Think

- **Created / updated**: 2026-10-27 / 2026-10-27
- **Task / library**: audio-text-to-text / peft
- **Relevance**: 19 pts · Audio Understanding & Reasoning: audio reasoning, audio-text (pipeline tag); model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=19 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2610.34609](https://arxiv.org/abs/2610.34609)
- **Datasets / base models**: unknown / nvidia/audio-flamingo-next-think-hf
- **Variants in family**: —

#### M29. stabilityai/stable-audio-3-optimized

- **Created / updated**: 2026-05-18 / 2026-10-30
- **Task / library**: text-to-audio / stable-audio-3
- **Relevance**: 17 pts · Generative Music & Audio: audio generation, text-to-audio (pipeline tag); model card links an arXiv paper; declares license other; community likes 62
- **Adoption signals**: downloads=47656 · likes=62 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2605.17991](https://arxiv.org/abs/2605.17991)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M30. LattifAI/YuE2-3B-GGUF

- **Created / updated**: 2026-10-27 / 2026-10-30
- **Task / library**: text-to-audio / unknown
- **Relevance**: 16 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=261 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2609.33757](https://arxiv.org/abs/2609.33757) · [arXiv:2610.05336](https://arxiv.org/abs/2610.05336)
- **Datasets / base models**: unknown / m-a-p/YuE2-3B, m-a-p/YuE2-Vae
- **Variants in family**: —

## Research signals

- Audio & Speech Language Models: 16 papers
- Speech Generation, Recognition & Dialogue: 12 papers
- Generative Music & Audio: 11 papers
- Audio Understanding & Reasoning: 4 papers
- Evaluation, Alignment, Safety & Copyright: 1 papers
- Music Foundation Models & Representations: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [TAC2: Timestamped Audio Captioning as composable functions](https://arxiv.org/abs/2610.36568) | 2026-10-27 | 28 | Audio & Speech Language Models, Generative Music & Audio, Audio Understanding & Reasoning | — |
| 2 | [Audio-R1: Audio Reasoning through Reinforcement Learning on Self-Supervised Tasks](https://arxiv.org/abs/2610.34609) | 2026-10-25 | 27 | Audio & Speech Language Models, Audio Understanding & Reasoning, Evaluation, Alignment, Safety & Copyright | — |
| 3 | [Does Notation Matter? MusicXML Tokenisation for Symbolic Music Generation and Understanding](https://arxiv.org/abs/2610.34247) | 2026-10-25 | 23 | Music Foundation Models & Representations, Generative Music & Audio | — |
| 4 | [S3-S2ST: Semantically Supervised Streaming Speech-to-Speech Translation](https://arxiv.org/abs/2610.36777) | 2026-10-27 | 21 | Speech Generation, Recognition & Dialogue | — |
| 5 | [Uni-Stream: A Unified Streaming Speech Language Model for Speech Synthesis and Recognition](https://arxiv.org/abs/2610.32187) | 2026-10-23 | 21 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 6 | [Do Audio LLMs HEAR Pain? Tracing Acoustic Evidence from Speech to Language Reasoning](https://arxiv.org/abs/2610.38570) | 2026-10-28 | 20 | Audio & Speech Language Models | — |
| 7 | [In-Context Adapter Generation for Compositional Generalization in Large Audio Language Models](https://arxiv.org/abs/2610.34413) | 2026-10-25 | 18 | Audio & Speech Language Models, Audio Understanding & Reasoning | — |
| 8 | [Melody Guidance for Audio Diffusion Models Without Retraining](https://arxiv.org/abs/2610.32211) | 2026-10-23 | 18 | Generative Music & Audio | — |
| 9 | [Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis](https://arxiv.org/abs/2610.39168) | 2026-10-29 | 17 | Speech Generation, Recognition & Dialogue | — |
| 10 | [A Tutorial on Generative Models for Music Audio](https://arxiv.org/abs/2610.38252) | 2026-10-28 | 16 | Generative Music & Audio | — |
| 11 | [AudioRSI: Recursively Self-Improving Audio Reasoners](https://arxiv.org/abs/2610.36578) | 2026-10-27 | 16 | Audio & Speech Language Models | — |
| 12 | [MusicTwins: Training Audio-Language Models to Listen like Their Persona](https://arxiv.org/abs/2610.32495) | 2026-10-23 | 15 | Audio & Speech Language Models | — |
| 13 | [Concentrated Causal Influence, Distributed Diagnostic Information: Cognitive Impairment Decisions in Large Audio-Language Models](https://arxiv.org/abs/2610.32061) | 2026-10-23 | 15 | Audio & Speech Language Models | — |
| 14 | [Pronunciation-Supervised Text-to-Speech for Irish (Gaeilge)](https://arxiv.org/abs/2610.38384) | 2026-10-28 | 14 | Speech Generation, Recognition & Dialogue | — |
| 15 | [DRC-TTS: A Dual-Resolution Codec-Based Architecture for Lexicon-Free Malay Speech Synthesis](https://arxiv.org/abs/2610.38316) | 2026-10-28 | 14 | Generative Music & Audio, Speech Generation, Recognition & Dialogue | — |
| 16 | [MixCards: Evaluating Structured Descriptions of Multi-Source Sound Scenes](https://arxiv.org/abs/2610.38276) | 2026-10-28 | 13 | Audio & Speech Language Models, Audio Understanding & Reasoning | [repo](https://github.com/Sound-Captioning-for-Accessibility/mixcardbench) |
| 17 | [StreamSE: Neural Audio Codec-based Streaming Speech Enhancement for On-device Inference](https://arxiv.org/abs/2610.37024) | 2026-10-27 | 13 | Generative Music & Audio | — |
| 18 | [Developing a Speech Language Model for Basque](https://arxiv.org/abs/2610.36911) | 2026-10-27 | 13 | Audio & Speech Language Models | — |
| 19 | [From Speech Tokens to Stolen Voices: Attacker-Chosen-Text Speaker Impersonation via Representation Inversion](https://arxiv.org/abs/2610.34688) | 2026-10-26 | 12 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 20 | [Beyond Utterance-Level Speaker Similarity: Perception-Aligned Segmental Evaluation of Accent in Speech Generation](https://arxiv.org/abs/2610.37912) | 2026-10-27 | 11 | Speech Generation, Recognition & Dialogue | — |
| 21 | [Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion](https://arxiv.org/abs/2610.34415) | 2026-10-25 | 11 | Generative Music & Audio | — |
| 22 | [Beyond Answer Changes: Matched Same-Class Controls for Local Audio Evidence](https://arxiv.org/abs/2610.37605) | 2026-10-27 | 10 | Audio & Speech Language Models | [repo](https://github.com/huaruoji/beyond-answer-changes) |
| 23 | [AI-Based Voice to Music Generation System](https://www.semanticscholar.org/paper/10e6814b5482779878101e4f92b87ec9494b5422) | 2026-10-26 | 10 | Generative Music & Audio | — |
| 24 | [Understanding Everyday Communication Patterns, Stress, and Productivity in Hybrid Work through Egocentric Wearable Audio Sensing](https://arxiv.org/abs/2610.37270) | 2026-10-27 | 8 | Audio & Speech Language Models | — |
| 25 | [SimPOTrans: Self-Adaptation for Offline-to-Simultaneous Speech Translation via Reinforcement Learning](https://arxiv.org/abs/2610.35042) | 2026-10-26 | 8 | Speech Generation, Recognition & Dialogue | — |
| 26 | [Preserve to Expand: Source-Aware Adaptation and Model Merging for Multilingual LLM-Based ASR](https://arxiv.org/abs/2610.35846) | 2026-10-26 | 8 | Audio & Speech Language Models | — |
| 27 | [ImageTTS: Repurposing Pretrained Image Diffusion Transformers for Speech Synthesis](https://arxiv.org/abs/2610.34807) | 2026-10-26 | 8 | Speech Generation, Recognition & Dialogue | — |
| 28 | [ASR-Protected Fusion and Reference-Anchored Policy Optimization for Joint ASR and Word-Level Speech Anti-Spoofing](https://arxiv.org/abs/2610.34156) | 2026-10-25 | 8 | Audio & Speech Language Models | — |
| 29 | [Probing the phon* representations of the Mimi codebooks](https://arxiv.org/abs/2610.35432) | 2026-10-26 | 7 | Generative Music & Audio | — |
| 30 | [SpeakerTurn: Target-Speaker Semantic Turn Detection in Multi-Speaker Environments](https://arxiv.org/abs/2610.39828) | 2026-10-29 | 6 | Audio & Speech Language Models | — |
| 31 | [SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization](https://arxiv.org/abs/2610.40640) | 2026-10-29 | 6 | Generative Music & Audio | — |
| 32 | [Partially Edited Audio: Generation, Defense, and Open Problems](https://arxiv.org/abs/2610.37640) | 2026-10-27 | 6 | Generative Music & Audio | — |
| 33 | [WiP: VishGuard-M: Toward Voice-Authenticity-Aware Vishing Detection on Mobile Devices](https://www.semanticscholar.org/paper/7dc887e0768076ce0ecdb1573782b51c4a86630c) | 2026-10-26 | 6 | Speech Generation, Recognition & Dialogue | — |
| 34 | [ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling](https://arxiv.org/abs/2610.36126) | 2026-10-26 | 6 | Speech Generation, Recognition & Dialogue | — |
| 35 | [Artificial Intelligence for Elder-Scam Defense: A Review of Detection Methods for Human- and AI-Generated Fraud and a Layered Protection Framework](https://www.semanticscholar.org/paper/cfcace78eb128ccaf89996e340a95665ee862aa8) | 2026-10-25 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. TAC2: Timestamped Audio Captioning as composable functions

- **Authors**: Swapnil Bhosale, Prem Seetharaman, Ke Chen, Haonan Chen, Justin Salamon, Zeyu Jin
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 28 pts · Audio Understanding & Reasoning: audio captioning, audio understanding; Generative Music & Audio: audio generation, text-to-audio; Audio & Speech Language Models: audio-language model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.36568) · [PDF](https://arxiv.org/pdf/2610.36568v1)

Real-world audio applications require precise, queryable representations grounded in physical time. Yet modern Large Audio-Language Models (LALMs) increasingly favor conversational generation, producing free-form descriptions that conflate acoustic perception with higher-level reasoning and lack precise temporal grounding. We introduce TAC2, a foundation model that casts timestamped audio captioning as composable…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. Audio-R1: Audio Reasoning through Reinforcement Learning on Self-Supervised Tasks

- **Authors**: Jihoon Jeong, Mirco Ravanelli, Zhepei Wang, Cem Subakan
- **Date / sources**: 2026-10-25 · arxiv, semantic_scholar
- **Relevance**: 27 pts · Audio Understanding & Reasoning: audio reasoning, audio understanding; Audio & Speech Language Models: audio-language model; Evaluation, Alignment, Safety & Copyright: audio benchmark; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.34609) · [PDF](https://arxiv.org/pdf/2610.34609v1)

Reasoning is increasingly important for large audio-language models (LALMs), yet remains relatively underexplored compared with text-only and vision-language models. We introduce Audio-R1, a reinforcement learning (RL) post-training framework that revisits audio self-supervised learning as a source of verifiable rewards for improving audio understanding and reasoning task performance. Audio-R1 uses answers…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. Does Notation Matter? MusicXML Tokenisation for Symbolic Music Generation and Understanding

- **Authors**: Andrea Poltronieri, Matteo Spanio, Simone Chieppa, Xavier Serra, Martín Rocamora
- **Date / sources**: 2026-10-25 · arxiv, semantic_scholar
- **Relevance**: 23 pts · Music Foundation Models & Representations: music understanding, symbolic music; Generative Music & Audio: music generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.34247) · [PDF](https://arxiv.org/pdf/2610.34247v1)

Symbolic music representations encode musical content at varying levels of completeness, from performance-oriented formats such as MIDI to fully notated scores such as MusicXML. Yet the impact of this representational richness on deep learning models remains poorly understood. While tokenisation has been extensively studied for MIDI, score-based formats have received considerably less attention, and MusicXML in…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. S3-S2ST: Semantically Supervised Streaming Speech-to-Speech Translation

- **Authors**: Yuxiang Zhao, Zhiyun Fan, Yu Pu, Yanjie An, Yushen Chen, Wenrui Liang, Baiji Liu, Yunchong Xiao et al.
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: speech translation, speech-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.36777) · [PDF](https://arxiv.org/pdf/2610.36777v1)

Streaming speech-to-speech translation requires timely decisions about when partial input is sufficient for accurate translation. We present S3-S2ST, a model that learns to translate and speak from semantically aligned streaming supervision. By converting utterance-level speech pairs into incremental training examples, we teach a learned policy when to commit translations. Its adjustable threshold controls the…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Uni-Stream: A Unified Streaming Speech Language Model for Speech Synthesis and Recognition

- **Authors**: Xuan Shi, Chang Zeng, Tiantian Feng, Ye Zhang, Jun Liu, Shih-Heng Wang, Lie Lu, Shrikanth Narayanan
- **Date / sources**: 2026-10-23 · arxiv, semantic_scholar
- **Relevance**: 21 pts · Audio & Speech Language Models: speech language model; Speech Generation, Recognition & Dialogue: speech synthesis; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.32187) · [PDF](https://arxiv.org/pdf/2610.32187v1)

Unified streaming speech language models aim to support speech recognition and synthesis within a single model, enabling real-time human-computer interaction. However, jointly supporting these two directions of speech-text conversion while preserving task-specific performance remains challenging. We propose Uni-Stream, a unified streaming speech language model built on compact pretrained speech models. Uni-Stream…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. Do Audio LLMs HEAR Pain? Tracing Acoustic Evidence from Speech to Language Reasoning

- **Authors**: Wenqi Li, Xiangjue Dong, Sulaiman Vesal
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 20 pts · Audio & Speech Language Models: audio language model, audio llm
- **Links**: [Paper](https://arxiv.org/abs/2610.38570) · [PDF](https://arxiv.org/pdf/2610.38570v1)

Large audio language models (LALMs) can process speech directly, but it remains unclear how well they use the non-lexical acoustic information that speech carries. We study this question through pain, using TAME-Pain, which contains pain-neutral Harvard sentences and spoken pain ratings recorded at different self-reported pain levels. We introduce HEAR, a four-stage diagnostic framework that traces pain-related…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. In-Context Adapter Generation for Compositional Generalization in Large Audio Language Models

- **Authors**: Yiwei Guo, Siqi Huang, Bohan Li, Jing Peng, Hankun Wang, Zhihan Li, Kai Yu
- **Date / sources**: 2026-10-25 · arxiv, semantic_scholar
- **Relevance**: 18 pts · Audio & Speech Language Models: audio language model; Audio Understanding & Reasoning: audio understanding; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.34413) · [PDF](https://arxiv.org/pdf/2610.34413v1)

Large audio language models (LALMs) have achieved strong performance on standard speech and audio understanding tasks, yet their ability to systematically generalize to novel task compositions remains underexplored. Taking a meta-learning view, we extend Text-to-LoRA (T2L) to LALMs, generating instruction-conditioned LoRA adapters with a Transformer hypernetwork rather than learning a single fixed adapter shared…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. Melody Guidance for Audio Diffusion Models Without Retraining

- **Authors**: Cristobal Andrade, Sebastian J. Schlecht, Ben Maman, Meinard Müller
- **Date / sources**: 2026-10-23 · arxiv, semantic_scholar
- **Relevance**: 18 pts · Generative Music & Audio: audio generation, audio diffusion; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.32211) · [PDF](https://arxiv.org/pdf/2610.32211v1)

Controlling melody in audio generation normally requires training a conditional generative model on audio paired with pitch curves or MIDI notes. We instead guide an existing unconditional diffusion model, originally trained without melody inputs, to follow a target melody without retraining or modifying it. During inference, a differentiable pitch detector steers the sampled audio toward the desired pitches, while…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis

- **Authors**: Cheng Zhang
- **Date / sources**: 2026-10-29 · arxiv
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: speech synthesis, automatic speech recognition, voice cloning
- **Links**: [Paper](https://arxiv.org/abs/2610.39168) · [PDF](https://arxiv.org/pdf/2610.39168v1)

Few-shot voice cloning makes it cheap to produce daily Japanese financial commentary with several synthetic speakers, but kanji words with more than one reading, such as the word for "market" (shijo vs. ichiba) or "overall trend" (taisei vs. oze), are still misread. A common quality gate transcribes each synthesized sentence with automatic speech recognition (ASR), converts both the input and the transcript to kana,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. A Tutorial on Generative Models for Music Audio

- **Authors**: Mateusz Modrzejewski, Joanna Kurkowska, Dorien Herremans
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 16 pts · Generative Music & Audio: music generation, audio generation, neural audio codec
- **Links**: [Paper](https://arxiv.org/abs/2610.38252) · [PDF](https://arxiv.org/pdf/2610.38252v1)

Music audio generation spans instrumental clips, full songs with vocals, edits of existing recordings, and systems that play alongside a musician in real time. This monograph explains the methods behind these systems for readers familiar with neural-network training who are new to music generation. It introduces neural audio codecs and autoencoders, autoregressive and masked token models, diffusion and flow…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 11. AudioRSI: Recursively Self-Improving Audio Reasoners

- **Authors**: Jiajun Fan, Roger Ren, Jingyuan Li, Rahul Pandey, Prashanth Gurunath Shivakumar, Ankur Gandhe, Yile Gu, Ge Liu et al.
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 16 pts · Audio & Speech Language Models: audio large language model, audio llm; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.36578) · [PDF](https://arxiv.org/pdf/2610.36578v1)

Reinforcement learning has made Audio Large Language Models (Audio LLMs) better reasoners, but the reward that drives it still comes from outside the model: a final-answer check, a hand-crafted process score, or an external LLM judge that stays fixed while the policy improves. We show that an Audio LLM can supply this reward itself, and can do so recursively: each improved model becomes the critic that trains its…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 12. MusicTwins: Training Audio-Language Models to Listen like Their Persona

- **Authors**: Milan Liessens Dujardin, Kevin Miao
- **Date / sources**: 2026-10-23 · arxiv, semantic_scholar
- **Relevance**: 15 pts · Audio & Speech Language Models: audio-language model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.32495) · [PDF](https://arxiv.org/pdf/2610.32495v1)

People differ in how they perceive music, what associations they make with it, what they like about it, and how they respond to it. Computational models intended to simulate people in environments that include music should account for these differences. Although LLMs have been shown to reproduce aspects of human behavior, whether audio-language models (ALMs) can reproduce a specific person's responses to textual and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 13. Concentrated Causal Influence, Distributed Diagnostic Information: Cognitive Impairment Decisions in Large Audio-Language Models

- **Authors**: Xiutian Zhao, Luqi Sun, Björn Schuller, Berrak Sisman
- **Date / sources**: 2026-10-23 · arxiv, semantic_scholar
- **Relevance**: 15 pts · Audio & Speech Language Models: audio-language model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.32061) · [PDF](https://arxiv.org/pdf/2610.32061v1)

Large audio-language models (LALMs) can assess cognitive impairment (CI) from speech, yet their answers reveal neither which internal components control the decision nor how much CI information is accessible in their representations. We investigate both questions through CI-contrast neurons (CICNs), selected by class-contrastive activation frequency in decoder MLPs. Across eight open LALMs and two corpora (Pitt and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 14. Pronunciation-Supervised Text-to-Speech for Irish (Gaeilge)

- **Authors**: William Lane
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 14 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech
- **Links**: [Paper](https://arxiv.org/abs/2610.38384) · [PDF](https://arxiv.org/pdf/2610.38384v1)

Speech technology for Irish must be built from very little transcribed speech, yet the language's pronunciation is thoroughly documented in dictionaries and dialect descriptions. We ask whether that documentation can supervise the adaptation of a large pretrained text-to-speech model to a language it was never trained on. We adapt Qwen3-TTS to Irish using 12.8 hours of crowdsourced Common Voice speech, correcting…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 15. DRC-TTS: A Dual-Resolution Codec-Based Architecture for Lexicon-Free Malay Speech Synthesis

- **Authors**: Tianhui Su, Tien-Ping Tan
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 14 pts · Speech Generation, Recognition & Dialogue: speech synthesis; Generative Music & Audio: neural audio codec
- **Links**: [Paper](https://arxiv.org/abs/2610.38316) · [PDF](https://arxiv.org/pdf/2610.38316v1)

Modern discrete neural audio codecs facilitate speech synthesis by replacing continuous acoustic representations with low-frame-rate discrete token sequences. For Malay speech synthesis, character-level input reduces reliance on pronunciation lexicons. However, combining character-level inputs with low-frame-rate discrete codecs introduces a temporal alignment challenge. When predicted character durations are…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 16. MixCards: Evaluating Structured Descriptions of Multi-Source Sound Scenes

- **Authors**: Sripathi Sridhar, Yujin Kim, Giovana Morais, Liang-Yuan Wu, Mehmet Atilay Kucukoglu, Prem Seetharaman, Lloyd May, Mark Cartwright et al.
- **Date / sources**: 2026-10-28 · arxiv
- **Relevance**: 13 pts · Audio & Speech Language Models: audio language model; Audio Understanding & Reasoning: audio captioning; has open-source code link
- **Links**: [Paper](https://arxiv.org/abs/2610.38276) · [PDF](https://arxiv.org/pdf/2610.38276v1) · [Code 1](https://github.com/Sound-Captioning-for-Accessibility/mixcardbench)

Audio captioning benchmarks typically evaluate a single unstructured free-text description of an audio scene, providing limited insight into how a model fails to understand polyphonic audio. A plausible caption may omit a source, or conflate multiple sources into one, or assign an attribute of one source to another, and conventional captioning evaluation cannot locate these errors. We introduce MixCardBench, a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 17. StreamSE: Neural Audio Codec-based Streaming Speech Enhancement for On-device Inference

- **Authors**: Hyunjin Choi, Zinu Kim, Junwon Moon, Jeongyun Chae, Seungbeom Kim, Kyuhong Shim
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Generative Music & Audio: neural audio codec; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.37024) · [PDF](https://arxiv.org/pdf/2610.37024v1)

Recent generative speech enhancement (SE) models achieve high perceptual quality, but their non-causal processing and expensive computation make them difficult to use for streaming, on-device inference. We propose StreamSE, a 20M-parameter streaming SE model that operates in the latent space of a frozen pretrained neural audio codec. At each frame, StreamSE directly regresses a clean continuous latent from the noisy…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 18. Developing a Speech Language Model for Basque

- **Authors**: Andoni Sudupe, Inma Hernaez, Ander Arriandiaga, Christoforos Souganidis, Ibon Saratxaga, Eva Navas
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Audio & Speech Language Models: speech language model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.36911) · [PDF](https://arxiv.org/pdf/2610.36911v1)

Although the recent development of LLMs has paved the way for multi-modal interaction, minority languages face difficulties keeping pace. This work presents the first open Speech Language Model for Basque, designed for low-latency, end-to-end spoken interaction. Based on the LLaMA-Omni architecture, the system integrates a Latxa model as its backbone, transferring its Basque capabilities to the spoken modality by…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 19. From Speech Tokens to Stolen Voices: Attacker-Chosen-Text Speaker Impersonation via Representation Inversion

- **Authors**: Ye Lu, Shen Wang, Runze Liu, Zhitao Ou, Haonan Huang, Yihan Yan, Fanghui Sun, Zhaoyang Zhang
- **Date / sources**: 2026-10-26 · arxiv, semantic_scholar
- **Relevance**: 12 pts · Audio & Speech Language Models: speech language model; Speech Generation, Recognition & Dialogue: speech generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.34688) · [PDF](https://arxiv.org/pdf/2610.34688v1)

Speech interaction systems have gradually evolved from traditional cascaded systems that use text as intermediate information to end-to-end speech language models that directly process speech representations. In some applications, the speech frontend runs on the user's device and sends speech representations to a remote server for inference, while the original audio remains local. However, these representations may…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 20. Beyond Utterance-Level Speaker Similarity: Perception-Aligned Segmental Evaluation of Accent in Speech Generation

- **Authors**: Jinzuomu Zhong, Alice Ross, Catherine Lai, Korin Richmond
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.37912) · [PDF](https://arxiv.org/pdf/2610.37912v1)

Utterance-level similarity ratings do not reveal where perceived accent differences occur in generated speech. We introduce a segmental evaluation protocol combining speaker and accent similarity ratings with subword annotations of perceived accent differences provided by listeners from target accent regions. Using newly collected recordings, 47 retained listeners evaluate 200 content-matched reference--candidate…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 21. Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion

- **Authors**: Kam Man Wu, Yu Zhang, Pengjun Fang, Mingfei Chen, Weijia Chen, Zeyue Tian, Qifeng Chen
- **Date / sources**: 2026-10-25 · arxiv, semantic_scholar
- **Relevance**: 11 pts · Generative Music & Audio: audio generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.34415) · [PDF](https://arxiv.org/pdf/2610.34415v1)

Spatial audio authoring coordinates source decisions with soundfield synthesis. For editing, plans specify what to change and retain, while reference audio supplies further acoustic detail. We present AMBIT, a unified framework for native First-Order Ambisonics (FOA) generation and editing with three connected contributions. First, a shared Transfusion backbone couples autoregressive planning with rectified-flow…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 22. Beyond Answer Changes: Matched Same-Class Controls for Local Audio Evidence

- **Authors**: Yunuo Wang, Maoyuan Chen, Yuanjin Huang, Xing Liu
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 10 pts · Audio & Speech Language Models: audio-language model; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.37605) · [PDF](https://arxiv.org/pdf/2610.37605v1) · [Code 1](https://github.com/huaruoji/beyond-answer-changes)

For audio-language models, an answer change after a local sound-event edit can reflect a response to the event's class, sensitivity to waveform rewriting, or both. We compare matched same-class and different-class replacements of a queried event. Both use the same interval, level estimate, donor fitting, and crossfade, while the same-class replacement preserves the correct answer. Across 600 synthetic soundscapes…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 23. AI-Based Voice to Music Generation System

- **Authors**: Abdul Razzaq, Arun Kumar Kh, Bhaskar V, Lohith C. N., Mounashree Hs
- **Date / sources**: 2026-10-26 · semantic_scholar
- **Relevance**: 10 pts · Generative Music & Audio: music generation
- **Links**: [Paper](https://www.semanticscholar.org/paper/10e6814b5482779878101e4f92b87ec9494b5422) · [PDF](https://ijcope.org/wp-content/uploads/2026/10/AI-Based-Voice-to-Music-Generation-System.pdf)

The rapid advancement of Artificial Intelligence (AI), Machine Learning (ML), Natural Language Processing (NLP), and generative models has created new opportunities for automating creative processes, particularly in music composition and audio production. Traditional music creation often requires musical knowledge, instrument-playing skills, professional audio-editing tools, and considerable time. These requirements…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 24. Understanding Everyday Communication Patterns, Stress, and Productivity in Hybrid Work through Egocentric Wearable Audio Sensing

- **Authors**: Tiantian Feng, Aditya Kommineni, Emily Zhou, Burcin Becerik-Gerber, Gale Lucas, Shawn C. Roll, Shrikanth Narayanan
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 8 pts · Audio & Speech Language Models: speech foundation model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.37270) · [PDF](https://arxiv.org/pdf/2610.37270v1)

The hybrid work trend in the post-COVID period has transformed how people communicate while at work. However, there is a lack of quantitative understanding of how home and office environments shape communicative behavior and affective well-being. To study this, as a part of a larger study of the role of work environment on stress, we designed an egocentric wearable audio sensing system that captured interpersonal…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 25. SimPOTrans: Self-Adaptation for Offline-to-Simultaneous Speech Translation via Reinforcement Learning

- **Authors**: Hao-Tian Tan, Hiroki Ouchi, S. Sakti
- **Date / sources**: 2026-10-26 · semantic_scholar
- **Relevance**: 8 pts · Speech Generation, Recognition & Dialogue: speech translation
- **Links**: [Paper](https://arxiv.org/abs/2610.35042)

Simultaneous speech translation (SimulST) aims to translate ongoing speech with low latency while preserving translation quality. Recent studies have adopted large language models (LLMs) for SimulST and formulated it as a multi-turn dialogue task for efficient generation, achieving state-of-the-art performance. However, existing dialogue-style SimulST approaches typically rely on specialized training schemes to…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 26. Preserve to Expand: Source-Aware Adaptation and Model Merging for Multilingual LLM-Based ASR

- **Authors**: Yuchen Zhang, Haralambos Mouratidis, Ravi Shekhar
- **Date / sources**: 2026-10-26 · arxiv, semantic_scholar
- **Relevance**: 8 pts · Audio & Speech Language Models: speech llm; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.35846) · [PDF](https://arxiv.org/pdf/2610.35846v1)

Expanding multilingual ASR systems to new languages is challenging when adaptation must preserve previously supported languages without replaying source-language training data. We study this problem in connector-based Speech LLMs, where a trainable connector maps speech representations into a frozen large language model. We evaluate target-update construction and merging strategies for adapting the connector while…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 27. ImageTTS: Repurposing Pretrained Image Diffusion Transformers for Speech Synthesis

- **Authors**: Han-Chen Pei, Shu-Jie Liu, Ya-Yue Deng, Fang-Yun Wei, Yan-Qing Liu, Jian-Wei Yu, Gong-Ping Huang
- **Date / sources**: 2026-10-26 · semantic_scholar
- **Relevance**: 8 pts · Speech Generation, Recognition & Dialogue: speech synthesis
- **Links**: [Paper](https://arxiv.org/abs/2610.34807)

Pretrained image-generation models have been successfully repurposed for various downstream visual tasks. Whether their learned representations and generative priors can transfer beyond vision to other modalities remains largely unresolved, particularly for speech synthesis, which requires linguistic fidelity and preservation of speaker identity from a short reference. We present ImageTTS, which repurposes FLUX.2…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 28. ASR-Protected Fusion and Reference-Anchored Policy Optimization for Joint ASR and Word-Level Speech Anti-Spoofing

- **Authors**: Xueping Zhang, Xiaoxiao Miao, Tiantian Feng, Ming Li
- **Date / sources**: 2026-10-25 · arxiv, semantic_scholar
- **Relevance**: 8 pts · Audio & Speech Language Models: audio llm; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.34156) · [PDF](https://arxiv.org/pdf/2610.34156v1)

Existing anti-spoofing systems report either an utterance-level score or a time-based spoof interval: the former cannot show which words are spoofed, while the latter does not directly match the transcript and must be post-aligned with words, so alignment errors can lead to wrong word-level labels. Standard ASR model outputs only text; spoof information in the audio is lost after recognition and is not passed with…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 29. Probing the phon* representations of the Mimi codebooks

- **Authors**: Artem Saloev, Nicolas Ballier, Erin Pacquetet
- **Date / sources**: 2026-10-26 · arxiv, semantic_scholar
- **Relevance**: 7 pts · Generative Music & Audio: neural audio codec; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.35432) · [PDF](https://arxiv.org/pdf/2610.35432v1)

Neural audio codecs are increasingly used to encode speech for integration with large language models. This paper investigates the phonetic representations in the first codebook (CB0) of the Mimi codec. ABX style evaluation is poorly suited to Mimi fixed 80 ms tokenization window, which often spans multiple phonemes; we instead use forced alignment, entropy analysis, and Phone-Normalized Mutual Information (PNMI).…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 30. SpeakerTurn: Target-Speaker Semantic Turn Detection in Multi-Speaker Environments

- **Authors**: Nan Li, Hetao Shan, Jintao Liang, Jiahao Yan, Longbiao Wang, Tubin Huang, Min Xu
- **Date / sources**: 2026-10-29 · arxiv
- **Relevance**: 6 pts · Audio & Speech Language Models: speech language model
- **Links**: [Paper](https://arxiv.org/abs/2610.39828) · [PDF](https://arxiv.org/pdf/2610.39828v1)

Semantic completeness alone cannot determine when an assistant should respond in a multi-speaker environment: a completed utterance may belong to an interfering speaker, while the designated user is still speaking, acknowledging, or requesting time. We therefore study semantic turn inference conditioned on speaker identity. We propose SpeakerTurn, a framework that jointly predicts the target transcript and turn…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 31. SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization

- **Authors**: Derong Jin, Xiyi Chen, Ming C. Lin, Ruohan Gao
- **Date / sources**: 2026-10-29 · arxiv
- **Relevance**: 6 pts · Generative Music & Audio: audio diffusion
- **Links**: [Paper](https://arxiv.org/abs/2610.40640) · [PDF](https://arxiv.org/pdf/2610.40640v1)

Recent progress in visual scene generation has extended beyond static 3D scenes toward the more challenging problem of generating dynamic 4D scenes from minimal input. However, sound, despite being intrinsically coupled with dynamic objects and events, remains largely unmodeled in prior work. We introduce Video-to-4DAVScene, a new task that turns a video into an explorable, time-varying 4D audio-visual scene, and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 32. Partially Edited Audio: Generation, Defense, and Open Problems

- **Authors**: Lin Zhang, You Zhang, Nicholas Evans, Xin Wang, David Harwath, Abhinav Dhall, Bowen Shi, Chengzhe Sun et al.
- **Date / sources**: 2026-10-27 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Generative Music & Audio: audio generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.37640) · [PDF](https://arxiv.org/pdf/2610.37640v1)

Recent advances in generative audio models facilitate increasingly flexible and selective editing of linguistic content and paralinguistic, extralinguistic, and other attributes. This paradigm, named partially edited audio, differs from full audio generation as only portions of the real recording are edited. This technique can serve both beneficial and harmful applications. We therefore present a concise survey from…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 33. WiP: VishGuard-M: Toward Voice-Authenticity-Aware Vishing Detection on Mobile Devices

- **Authors**: Rina Mishra, Gaurav Varshney, D. Sahithi
- **Date / sources**: 2026-10-26 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/7dc887e0768076ce0ecdb1573782b51c4a86630c) · [PDF](https://doi.org/10.1145/3795866.3844752)

Generative AI has intensified voice phishing (vishing) through real-time voice cloning and LLM-driven conversational adaptation. State-of-the-art on-device defenses such as MmVTD analyze only transcripts and on-screen behavior, with no mechanism to verify the acoustic stream's authenticity. We present VishGuard-M, a lightweight dual branch framework pairing local voice-authenticity verification with linguistic…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 34. ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling

- **Authors**: Kehinde Elelu, Joshua E. Siegel, Mohammadali Saffary, Tashfain Ahmed, Simeon Babatunde, Ebuka Okpala
- **Date / sources**: 2026-10-26 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2610.36126) · [PDF](https://arxiv.org/pdf/2610.36126v1)

Accurate prediction of human Mean Opinion Scores (MOS) is crucial for evaluating synthetic speech quality in text-to-speech (TTS) and voice conversion (VC). Most MOS predictors output only point estimates and ignore uncertainty, limiting reliability in model selection and deployment. We propose ConformalMOS, a framework that augments MOS prediction with conformal prediction to produce statistically valid prediction…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 35. Artificial Intelligence for Elder-Scam Defense: A Review of Detection Methods for Human- and AI-Generated Fraud and a Layered Protection Framework

- **Authors**: B. Vörös, Cecilia Sik-Lányi
- **Date / sources**: 2026-10-25 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/cfcace78eb128ccaf89996e340a95665ee862aa8) · [PDF](https://doi.org/10.3390/info17111065)

Scams targeting older adults increasingly combine social engineering with generative technology such as voice cloning, video deepfakes and text produced by large language models (LLMs). Adults aged 60 and over reported losses of USD 7.7 billion to the FBI Internet Crime Complaint Center in 2025, 59% more than in 2024. This review, supported by a documented search of four databases (2019–2026), examines how such…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
