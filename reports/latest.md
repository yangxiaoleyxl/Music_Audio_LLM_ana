# Music / Audio Foundation Model Research Radar — 2026-11-25

> Lookback window: 2026-11-18 to 2026-11-25 · New papers: 24 · New models: 30 · relevant papers/models in window: 41/67 · raw papers/models: 124/352

Sources: arxiv=79 · semantic_scholar=45 · huggingface_models=352

## Source notes

- Semantic Scholar / Generative Music & Audio: HTTP Error 429: 
- Semantic Scholar / Evaluation, Alignment, Safety & Copyright: HTTP Error 429: 

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [snkii/Sori-10B-Speech](https://huggingface.co/snkii/Sori-10B-Speech) | 2026-11-24 | audio-text-to-text | 43 | 1 | 152 | 1 | cc-by-nc-sa-4.0 |
| 2 | [adventists-ai/Sophon-Realtime-4B-Flash](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Flash) | 2026-11-24 | audio-to-audio | 34 | 1 | 933 | 22 | apache-2.0 |
| 3 | [adventists-ai/Sophon-Realtime-32B-Tag](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag) | 2026-11-24 | audio-to-audio | 34 | 1 | 1251 | 16 | apache-2.0 |
| 4 | [adventists-ai/Sophon-Realtime-32B-Flash](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash) | 2026-11-24 | audio-to-audio | 34 | 2 | 1197 | 14 | apache-2.0 |
| 5 | [adventists-ai/Sophon-Realtime-32B-E2E](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-E2E) | 2026-11-24 | audio-to-audio | 33 | 1 | 402 | 7 | apache-2.0 |
| 6 | [adventists-ai/Sophon-Realtime-32B-Flash-4bit-MLX](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash-4bit-MLX) | 2026-11-24 | audio-to-audio | 33 | 2 | 488 | 2 | apache-2.0 |
| 7 | [adventists-ai/Sophon-Realtime-4B-E2E](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-E2E) | 2026-11-24 | audio-to-audio | 33 | 1 | 89 | 2 | apache-2.0 |
| 8 | [adventists-ai/Sophon-Realtime-4B-Tag-W4](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Tag-W4) | 2026-11-24 | audio-to-audio | 33 | 1 | 185 | 1 | apache-2.0 |
| 9 | [adventists-ai/Sophon-Realtime-4B-Flash-MLX](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Flash-MLX) | 2026-11-24 | audio-to-audio | 33 | 1 | 236 | 0 | apache-2.0 |
| 10 | [adventists-ai/Sophon-Realtime-4B-Tag](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Tag) | 2026-11-24 | audio-to-audio | 33 | 1 | 131 | 0 | apache-2.0 |
| 11 | [urbanhorizons/ada-omni-tr](https://huggingface.co/urbanhorizons/ada-omni-tr) | 2026-11-24 | audio-to-audio | 32 | 1 | 0 | 0 | apache-2.0 |
| 12 | [jsaigou/Haru-4B-bf16-radiance](https://huggingface.co/jsaigou/Haru-4B-bf16-radiance) | 2026-11-24 | audio-to-audio | 27 | 1 | 0 | 0 | apache-2.0 |
| 13 | [audio-cpp/audio.cpp-gguf](https://huggingface.co/audio-cpp/audio.cpp-gguf) | 2026-11-24 | text-to-speech | 24 | 1 | 9890552 | 343 | other |
| 14 | [HirCoir/piper-checkpoint-es-mx-astra](https://huggingface.co/HirCoir/piper-checkpoint-es-mx-astra) | 2026-11-25 | text-to-audio | 21 | 1 | 14 | 0 | unknown |
| 15 | [TheStinger/Ilaria_RVC](https://huggingface.co/TheStinger/Ilaria_RVC) | 2026-11-24 | audio-to-audio | 21 | 1 | 0 | 1 | mit |
| 16 | [empiriolabsai/canora-dutch](https://huggingface.co/empiriolabsai/canora-dutch) | 2026-11-24 | text-to-speech | 19 | 11 | 629 | 1 | apache-2.0 |
| 17 | [arupDesigns/higgs-tts-2-3b-base](https://huggingface.co/arupDesigns/higgs-tts-2-3b-base) | 2026-11-24 | text-to-speech | 19 | 1 | 0 | 0 | other |
| 18 | [davitlive5/sonabo-v1](https://huggingface.co/davitlive5/sonabo-v1) | 2026-11-24 | text-to-speech | 17 | 1 | 0 | 0 | apache-2.0 |
| 19 | [Dijo-404/madhan-tts-finetuned](https://huggingface.co/Dijo-404/madhan-tts-finetuned) | 2026-11-24 | text-to-speech | 15 | 3 | 0 | 2 | apache-2.0 |
| 20 | [Mikhailo/mova-tts](https://huggingface.co/Mikhailo/mova-tts) | 2026-11-24 | text-to-speech | 15 | 1 | 392 | 0 | apache-2.0 |
| 21 | [NikitHamal/sakhiya-pro-v1](https://huggingface.co/NikitHamal/sakhiya-pro-v1) | 2026-11-24 | text-to-speech | 15 | 1 | 105 | 0 | other |
| 22 | [mradermacher/sonabo-v2-GGUF](https://huggingface.co/mradermacher/sonabo-v2-GGUF) | 2026-11-24 | text-to-speech | 15 | 1 | 0 | 0 | apache-2.0 |
| 23 | [beleata74/BgTTS-40M-Engram-Loop](https://huggingface.co/beleata74/BgTTS-40M-Engram-Loop) | 2026-11-24 | text-to-speech | 15 | 1 | 0 | 0 | apache-2.0 |
| 24 | [baker76/voicegen-models](https://huggingface.co/baker76/voicegen-models) | 2026-11-24 | text-to-speech | 15 | 1 | 0 | 0 | apache-2.0 |
| 25 | [mimba/mimba-tune](https://huggingface.co/mimba/mimba-tune) | 2026-11-25 | text-to-audio | 14 | 1 | 0 | 0 | other |
| 26 | [Maximilian228/Geode-YuE2](https://huggingface.co/Maximilian228/Geode-YuE2) | 2026-11-24 | text-to-audio | 14 | 1 | 0 | 1 | cc-by-nc-4.0 |
| 27 | [Maximilian228/Geode-ACE-Step-1.5-turbo](https://huggingface.co/Maximilian228/Geode-ACE-Step-1.5-turbo) | 2026-11-24 | text-to-audio | 14 | 1 | 0 | 0 | mit |
| 28 | [Maximilian228/Geode-ACE-Step-1.5](https://huggingface.co/Maximilian228/Geode-ACE-Step-1.5) | 2026-11-24 | text-to-audio | 14 | 1 | 0 | 0 | mit |
| 29 | [ESpeech/ECodec-FAST](https://huggingface.co/ESpeech/ECodec-FAST) | 2026-11-24 | audio-to-audio | 13 | 1 | 0 | 1 | other |
| 30 | [nphearum/PsarAI-Omni](https://huggingface.co/nphearum/PsarAI-Omni) | 2026-11-24 | audio-to-audio | 13 | 1 | 66 | 0 | gemma |

### Model cards

#### M1. snkii/Sori-10B-Speech

- **Created / updated**: 2026-11-20 / 2026-11-24
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 43 pts · Audio & Speech Language Models: audio language model, audio-language model, speech llm; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=152 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.5-9B, Qwen/Qwen3-Omni-30B-A3B-Instruct
- **Variants in family**: —

#### M2. adventists-ai/Sophon-Realtime-4B-Flash

- **Created / updated**: 2026-11-16 / 2026-11-24
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 34 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0; community likes 22
- **Adoption signals**: downloads=933 · likes=22 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M3. adventists-ai/Sophon-Realtime-32B-Tag

- **Created / updated**: 2026-10-29 / 2026-11-24
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 34 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0; community likes 16
- **Adoption signals**: downloads=1251 · likes=16 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M4. adventists-ai/Sophon-Realtime-32B-Flash

- **Created / updated**: 2026-11-07 / 2026-11-24
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 34 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0; community likes 14
- **Adoption signals**: downloads=1197 · likes=14 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: adventists-ai/Sophon-Realtime-32B-Flash-BF16

#### M5. adventists-ai/Sophon-Realtime-32B-E2E

- **Created / updated**: 2026-11-08 / 2026-11-24
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=402 · likes=7 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M6. adventists-ai/Sophon-Realtime-32B-Flash-4bit-MLX

- **Created / updated**: 2026-11-12 / 2026-11-24
- **Task / library**: audio-to-audio / mlx
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=488 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / adventists-ai/Sophon-Realtime-32B-Flash
- **Variants in family**: adventists-ai/Sophon-Realtime-32B-Flash-4bit

#### M7. adventists-ai/Sophon-Realtime-4B-E2E

- **Created / updated**: 2026-11-16 / 2026-11-24
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=89 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M8. adventists-ai/Sophon-Realtime-4B-Tag-W4

- **Created / updated**: 2026-11-18 / 2026-11-24
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=185 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / adventists-ai/Sophon-Realtime-4B-Tag
- **Variants in family**: —

#### M9. adventists-ai/Sophon-Realtime-4B-Flash-MLX

- **Created / updated**: 2026-11-18 / 2026-11-24
- **Task / library**: audio-to-audio / mlx
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=236 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / adventists-ai/Sophon-Realtime-4B-Flash
- **Variants in family**: —

#### M10. adventists-ai/Sophon-Realtime-4B-Tag

- **Created / updated**: 2026-11-16 / 2026-11-24
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=131 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M11. urbanhorizons/ada-omni-tr

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 32 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; Audio Understanding & Reasoning: audio understanding; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unsloth/gemma-3n-E2B-it, erkamk/qwen3-0.6b-tr
- **Variants in family**: —

#### M12. jsaigou/Haru-4B-bf16-radiance

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: audio-to-audio / radiance
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / higurashi-ai/Haru-4B
- **Variants in family**: —

#### M13. audio-cpp/audio.cpp-gguf

- **Created / updated**: 2026-07-14 / 2026-11-24
- **Task / library**: text-to-speech / audio.cpp
- **Relevance**: 24 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), automatic speech recognition; declares license other; community likes 343
- **Adoption signals**: downloads=9890552 · likes=343 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / ASLP-lab/M5-TTS-50M-VoiceClone, ASLP-lab/M5-TTS-50M-CustomVoice, ASLP-lab/M5-TTS-Audio-Tokenizer, ibm-granite/granite-speech-5.0-2b, VoxDance-Lab/VoxMel-0.6B
- **Variants in family**: —

#### M14. HirCoir/piper-checkpoint-es-mx-astra

- **Created / updated**: 2026-10-23 / 2026-11-25
- **Task / library**: text-to-audio / unknown
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; Generative Music & Audio: text-to-audio (pipeline tag)
- **Adoption signals**: downloads=14 · likes=0 · trending=0.0
- **License / access**: unknown / gated
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M15. TheStinger/Ilaria_RVC

- **Created / updated**: 2026-11-01 / 2026-11-24
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: text-to-speech; Audio Understanding & Reasoning: audio-text; declares license mit
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M16. empiriolabsai/canora-dutch

- **Created / updated**: 2026-11-20 / 2026-11-24
- **Task / library**: text-to-speech / kokoro
- **Relevance**: 19 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=629 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / hexgrad/Kokoro-82M
- **Variants in family**: empiriolabsai/canora-turkish, empiriolabsai/canora-korean, empiriolabsai/canora-polish, empiriolabsai/canora-german, empiriolabsai/canora-norwegian, empiriolabsai/canora-russian, empiriolabsai/canora-french, empiriolabsai/canora-spanish, empiriolabsai/canora-portuguese, empiriolabsai/canora-italian

#### M17. arupDesigns/higgs-tts-2-3b-base

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: text-to-speech / transformers
- **Relevance**: 19 pts · Generative Music & Audio: text-to-audio; model card links an arXiv paper; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2505.23009](https://arxiv.org/abs/2505.23009)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M18. davitlive5/sonabo-v1

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: text-to-speech / qwen-tts
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2601.15621](https://arxiv.org/abs/2601.15621)
- **Datasets / base models**: unknown / Qwen/Qwen3-TTS-12Hz-0.6B-Base
- **Variants in family**: —

#### M19. Dijo-404/madhan-tts-finetuned

- **Created / updated**: 2026-11-20 / 2026-11-24
- **Task / library**: text-to-speech / qwen3-tts
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3-TTS-12Hz-0.6B-Base
- **Variants in family**: Dijo-404/madhan-tts, Dijo-404/kavi-tts

#### M20. Mikhailo/mova-tts

- **Created / updated**: 2026-11-21 / 2026-11-24
- **Task / library**: text-to-speech / mova-tts
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=392 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / neuphonic/neutts-air
- **Variants in family**: —

#### M21. NikitHamal/sakhiya-pro-v1

- **Created / updated**: 2026-11-23 / 2026-11-24
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=105 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / k2-fsa/OmniVoice
- **Variants in family**: —

#### M22. mradermacher/sonabo-v2-GGUF

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: text-to-speech / transformers
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / davitlive5/sonabo-v1
- **Variants in family**: —

#### M23. beleata74/BgTTS-40M-Engram-Loop

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: text-to-speech / pytorch
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / beleata74/BgTTS-38M-V2
- **Variants in family**: —

#### M24. baker76/voicegen-models

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: text-to-speech / onnx
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / openbmb/VoxCPM2
- **Variants in family**: —

#### M25. mimba/mimba-tune

- **Created / updated**: 2026-11-07 / 2026-11-25
- **Task / library**: text-to-audio / peft
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / gated
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5
- **Variants in family**: —

#### M26. Maximilian228/Geode-YuE2

- **Created / updated**: 2026-11-11 / 2026-11-24
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / m-a-p/YuE2-3B, m-a-p/YuE2-Vae
- **Variants in family**: —

#### M27. Maximilian228/Geode-ACE-Step-1.5-turbo

- **Created / updated**: 2026-11-21 / 2026-11-24
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5
- **Variants in family**: —

#### M28. Maximilian228/Geode-ACE-Step-1.5

- **Created / updated**: 2026-11-21 / 2026-11-24
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5, ACE-Step/acestep-v15-sft, ACE-Step/acestep-5Hz-lm-1.7B, Qwen/Qwen3-Embedding-0.6B
- **Variants in family**: —

#### M29. ESpeech/ECodec-FAST

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 13 pts · Generative Music & Audio: neural audio codec; declares license other
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M30. nphearum/PsarAI-Omni

- **Created / updated**: 2026-11-01 / 2026-11-24
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license gemma
- **Adoption signals**: downloads=66 · likes=0 · trending=0.0
- **License / access**: gemma / public
- **Related papers**: —
- **Datasets / base models**: unknown / google/gemma-4-E2B-it
- **Variants in family**: —

## Research signals

- Speech Generation, Recognition & Dialogue: 12 papers
- Audio & Speech Language Models: 6 papers
- Evaluation, Alignment, Safety & Copyright: 6 papers
- Music Foundation Models & Representations: 3 papers
- Generative Music & Audio: 3 papers
- Audio Understanding & Reasoning: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [MusicListenBench: Can Audio LLMs Hear the Difference Yet?](https://arxiv.org/abs/2611.29375) | 2026-11-22 | 27 | Audio & Speech Language Models, Music Foundation Models & Representations | — |
| 2 | [Can Speech LLMs Recognize When Audio Evidence Is Insufficient? A Diagnostic Study and a Pre-Generation Probing Mitigation](https://arxiv.org/abs/2611.29393) | 2026-11-22 | 22 | Audio & Speech Language Models, Evaluation, Alignment, Safety & Copyright | [repo](https://github.com/ladnlav/slm-audio-evidence) |
| 3 | [S$2$SCORE: A Textless Unified Evaluation Metric for Speech-to-Speech Translation Systems](https://arxiv.org/abs/2611.29557) | 2026-11-22 | 21 | Speech Generation, Recognition & Dialogue | — |
| 4 | [SWIFT: A Handcrafted, Arithmetic-Minimal FPGA Engine for Real-Time Audio Deepfake Detection](https://arxiv.org/abs/2611.29315) | 2026-11-22 | 19 | Speech Generation, Recognition & Dialogue, Evaluation, Alignment, Safety & Copyright | — |
| 5 | [BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models](https://arxiv.org/abs/2611.30723) | 2026-11-23 | 18 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 6 | [PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis](https://arxiv.org/abs/2611.29455) | 2026-11-22 | 16 | Speech Generation, Recognition & Dialogue | [repo](https://github.com/Firojpaudel/PAWP_TTS) |
| 7 | [Restorable Multilingual Voice Anonymization via Audio Watermarking](https://arxiv.org/abs/2611.28863) | 2026-11-21 | 14 | Evaluation, Alignment, Safety & Copyright | — |
| 8 | [From Spatial Perception to Speech Recovery: Binaural Semantic Adaptation for Spatially Grounded Multi-Talker Transcription](https://arxiv.org/abs/2611.29012) | 2026-11-21 | 14 | Audio & Speech Language Models, Audio Understanding & Reasoning | — |
| 9 | [Beyond File-Level Splits: Rethinking Symbolic Music Evaluation via Multi-View Alignment](https://arxiv.org/abs/2611.28765) | 2026-11-21 | 14 | Music Foundation Models & Representations, Generative Music & Audio | — |
| 10 | [EdgeALM: An Efficient and Unified Edge Accelerator for Large Audio Language Models via Full-Stack Hardware-Software Co-Design and Agent-Driven Recursive Optimization](https://arxiv.org/abs/2611.30216) | 2026-11-23 | 13 | Audio & Speech Language Models | — |
| 11 | [Characterizing Frozen SSL Encoders and Backends for Cross-Domain Speech Deepfake Detection](https://arxiv.org/abs/2611.29865) | 2026-11-23 | 12 | Evaluation, Alignment, Safety & Copyright | — |
| 12 | [Training speech deepfake detectors against worst-case filters: Gains, Costs and Limits](https://arxiv.org/abs/2611.28718) | 2026-11-21 | 12 | Evaluation, Alignment, Safety & Copyright | — |
| 13 | [LEGAL AND GOVERNANCE STANDARDS FOR REGULATING BIOMETRIC IDENTIFICATION AND VOICE CLONING TECHNOLOGIES](https://www.semanticscholar.org/paper/188638bcb1c7409cf70bf3bba43649040809a532) | 2026-11-20 | 12 | Speech Generation, Recognition & Dialogue | — |
| 14 | [When Being Wrong Is Right: Reverse-Capability Audio CAPTCHAs through Psychoacoustic Design](https://arxiv.org/abs/2611.28823) | 2026-11-21 | 11 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 15 | [Ultrasound Watermark: Real-time Acoustic Watermarking against Voice Scams on Smartphones](https://arxiv.org/abs/2611.30106) | 2026-11-23 | 10 | Speech Generation, Recognition & Dialogue | — |
| 16 | [LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation](https://arxiv.org/abs/2611.30714) | 2026-11-23 | 10 | Generative Music & Audio | — |
| 17 | [Music Circuit: Trace and Control Style Dynamics in Large Music Generation Model](https://arxiv.org/abs/2611.29475) | 2026-11-22 | 10 | Generative Music & Audio | — |
| 18 | [Synthetic Twins: Closing the Gap Between TTS Test Sets and Real Recordings in Turkish ASR Evaluation](https://arxiv.org/abs/2611.30694) | 2026-11-23 | 9 | Speech Generation, Recognition & Dialogue | — |
| 19 | [IteraSong: LLM-Guided Iterative Symbolic Music Creation in a Web DAW](https://arxiv.org/abs/2611.29225) | 2026-11-22 | 9 | Music Foundation Models & Representations | — |
| 20 | [Which Layer to Trust? Layer Selection in Frozen Speech Encoders for Singing-Voice Deepfake Detection under Signal Corruption](https://arxiv.org/abs/2611.29871) | 2026-11-23 | 6 | Evaluation, Alignment, Safety & Copyright | — |
| 21 | [SpeechSplice: Pronunciation Control in Encoder-Decoder LLM-based TTS by Replacing Encoder Hidden States](https://arxiv.org/abs/2611.30927) | 2026-11-23 | 6 | Speech Generation, Recognition & Dialogue | — |
| 22 | [Scoring L2 Pronunciation Without Synthesis: Counterfactual Velocity Contrast in Frozen Flow-Matching TTS](https://arxiv.org/abs/2611.29985) | 2026-11-23 | 6 | Speech Generation, Recognition & Dialogue | — |
| 23 | [SayWhen: Set-Valued Semantic Commitment for Low-Regret Early Speech](https://arxiv.org/abs/2611.31101) | 2026-11-23 | 6 | Speech Generation, Recognition & Dialogue | — |
| 24 | [Tenlai-TTS 2.0: Continuous-Representation LLM-Based TTS System with End-to-End Training](https://arxiv.org/abs/2611.29226) | 2026-11-22 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. MusicListenBench: Can Audio LLMs Hear the Difference Yet?

- **Authors**: Abhinaba Roy, Ambuj Mehrish, Dorien Herremans
- **Date / sources**: 2026-11-22 · arxiv, semantic_scholar
- **Relevance**: 27 pts · Audio & Speech Language Models: audio large language model, audio llm; Music Foundation Models & Representations: symbolic music; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29375) · [PDF](https://arxiv.org/pdf/2611.29375v1)

Audio large language models (LLMs) are typically evaluated on song genre, mood, and instrumentation. A more basic skill is telling whether two short clips play the same melody, chord or instrument. We introduce MusicListenBench, a benchmark of paired listening tests for melody, harmony, timbre, and tempo. Each test item comes with two variants. A FLIP variant changes the music, so the answer must change. A STAY…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. Can Speech LLMs Recognize When Audio Evidence Is Insufficient? A Diagnostic Study and a Pre-Generation Probing Mitigation

- **Authors**: Vladislav Nesterenko, Polina Doronicheva, Olga Golubeva, Polina Sheviakova
- **Date / sources**: 2026-11-22 · arxiv, semantic_scholar
- **Relevance**: 22 pts · Audio & Speech Language Models: speech llm; Evaluation, Alignment, Safety & Copyright: audio benchmark; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29393) · [PDF](https://arxiv.org/pdf/2611.29393v1) · [Code 1](https://github.com/ladnlav/slm-audio-evidence)

Speech large language models are usually evaluated on questions that have answers. We ask what they do when a recording establishes none, and whether the standard way of finding out is sound. Diagnosed on synthesized speech the answer looks clear: Qwen2-Audio fabricates an answer to 92.5% of unanswerable questions, while an ASR cascade reading the same recordings reaches 2.5% hallucination at 6.7% over-refusal,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. S$2$SCORE: A Textless Unified Evaluation Metric for Speech-to-Speech Translation Systems

- **Authors**: Lalaram Arya, Mrinmoy Bhattacharjee, S. R. Mahadeva Prasanna
- **Date / sources**: 2026-11-22 · arxiv, semantic_scholar
- **Relevance**: 21 pts · Speech Generation, Recognition & Dialogue: speech translation, speech-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29557) · [PDF](https://arxiv.org/pdf/2611.29557v1)

Evaluating speech-to-speech translation (S$2$ST) systems requires assessing multiple dimensions of translated speech, including semantic adequacy, speaker similarity, and acoustic naturalness. Existing approaches are largely text-based, relying on ASR transcripts and primarily assessing semantic adequacy, while other dimensions require separate metrics. We propose S$2$SCORE, a unified text-free evaluation framework…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. SWIFT: A Handcrafted, Arithmetic-Minimal FPGA Engine for Real-Time Audio Deepfake Detection

- **Authors**: Chirantan Banerjee, Soumita Chatterjee, Bhargab B. Bhattacharya, Hafizur Rahaman
- **Date / sources**: 2026-11-22 · arxiv, semantic_scholar
- **Relevance**: 19 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; Speech Generation, Recognition & Dialogue: voice cloning; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29315) · [PDF](https://arxiv.org/pdf/2611.29315v1)

Generative voice cloning threatens voice-based authentication, yet current deepfake detectors rely on power-hungry, high-precision models unsuited to edge hardware. We present SWIFT (Streaming Whiten-Integer Forensic Trust-Engine), a handcrafted detector that works in the high-frequency noise domain where synthesis artifacts concentrate. A first-order integer high-pass residual drives nine families of fixed-point…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language Models

- **Authors**: Y. Lu, L. Wang, S. Okada
- **Date / sources**: 2026-11-23 · arxiv, semantic_scholar
- **Relevance**: 18 pts · Audio & Speech Language Models: speech language model; Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.30723) · [PDF](https://arxiv.org/pdf/2611.30723v1)

Speech language models (LMs) generate speech as sequences of discrete tokens. Their tokenizer must therefore preserve both acoustic detail and linguistic content at a low bitrate. Semantic-enhanced tokenizers may lose acoustic detail, whereas acoustic-oriented tokenizers retain acoustic variation that makes language modeling harder. Unified tokenizers combine both, but representing acoustic detail and linguistic…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis

- **Authors**: Firoj Paudel
- **Date / sources**: 2026-11-22 · arxiv, semantic_scholar
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29455) · [PDF](https://arxiv.org/pdf/2611.29455v1) · [Code 1](https://github.com/Firojpaudel/PAWP_TTS)

This paper presents PAWP-TTS, a compact non-autoregressive text-to-speech system for English, Nepali, and English-Nepali code-mixed speech at 24 kHz, with no language model at inference. Deterministic pronunciation knowledge lives in a rule- and lexicon-based bilingual frontend that preserves native Nepali contrasts and avoids Hindi phonology, so the network only models acoustics. Counting every learned inference…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. Restorable Multilingual Voice Anonymization via Audio Watermarking

- **Authors**: Haoyuan Zheng, Guang Hua, Xiaoxiao Miao
- **Date / sources**: 2026-11-21 · arxiv
- **Relevance**: 14 pts · Evaluation, Alignment, Safety & Copyright: audio watermarking
- **Links**: [Paper](https://arxiv.org/abs/2611.28863) · [PDF](https://arxiv.org/pdf/2611.28863v1)

Voice anonymization aims to conceal speaker identity while preserving linguistic and paralinguistic information. However, certain applications also require the ability to attribute anonymized recordings to their original speakers. Existing recovery approaches often rely on specially designed reversible anonymization systems, limiting their applicability to different anonymization architectures. In this work, we…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. From Spatial Perception to Speech Recovery: Binaural Semantic Adaptation for Spatially Grounded Multi-Talker Transcription

- **Authors**: Wenxuan He, Shan Liang
- **Date / sources**: 2026-11-21 · arxiv, semantic_scholar
- **Relevance**: 14 pts · Audio & Speech Language Models: audio large language model; Audio Understanding & Reasoning: audio understanding; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29012) · [PDF](https://arxiv.org/pdf/2611.29012v1)

Spatial audio large language models increasingly combine general audio understanding with spatial perception. Yet overlapping conversations require more than locating speakers. A model must also recover what each person says and match the words to their positions. We examine this challenge in MiDashengLM-Spatial, a binaural model designed for both spatial reasoning and general audio understanding. To test these…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. Beyond File-Level Splits: Rethinking Symbolic Music Evaluation via Multi-View Alignment

- **Authors**: Kun Bai, Yinghan Wang, Canran Xiao, Jiachen Luo, Huy Phan, Yong Dai, Jiaqi Zhang, Yunwei Li et al.
- **Date / sources**: 2026-11-21 · arxiv, semantic_scholar
- **Relevance**: 14 pts · Music Foundation Models & Representations: symbolic music; Generative Music & Audio: music generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.28765) · [PDF](https://arxiv.org/pdf/2611.28765v1)

Symbolic music generation often continues MIDI passages by predicting subsequent notes or events. Held-out prediction loss can overestimate generalization to unseen compositions when training contains another performance or arrangement of a test work. We introduce Multi-View Alignment-Aware Same-Work Identification, combining complementary musical representations with temporal alignment of shared passages to remove…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. EdgeALM: An Efficient and Unified Edge Accelerator for Large Audio Language Models via Full-Stack Hardware-Software Co-Design and Agent-Driven Recursive Optimization

- **Authors**: Chenglin Yang, Feifan Xu, Xingyuan Li, Xinpeng Xing, Dihu Chen
- **Date / sources**: 2026-11-23 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Audio & Speech Language Models: audio language model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.30216) · [PDF](https://arxiv.org/pdf/2611.30216v1)

Edge deployment of audio language models (ALMs) is constrained by large model footprints, heterogeneous workloads, and limited software support. This paper presents EdgeALM, an efficient and unified FPGA accelerator for ALMs that combines full-stack hardware-software co-design with agent-driven recursive optimization. An end-to-end ALM compression flow is developed, combining a unified AWQ-style quantizer with…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 11. Characterizing Frozen SSL Encoders and Backends for Cross-Domain Speech Deepfake Detection

- **Authors**: Benjamin Hurt, Oscar O'Donnell, Yefei Yang, Anjani Sethi, Priyanka Durai
- **Date / sources**: 2026-11-23 · arxiv
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Links**: [Paper](https://arxiv.org/abs/2611.29865) · [PDF](https://arxiv.org/pdf/2611.29865v1)

Self-supervised learning (SSL) encoders are the dominant front end for speech deepfake detection, and the prevailing recipe fine-tunes the full encoder on a small spoofing corpus, maximizing in-domain accuracy at the cost of known degradation under domain shift. Taking a recent cross-attention fusion of SSL and constant-Q cepstral features as a fixed reference recipe, we freeze its encoder and ask which encoder and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 12. Training speech deepfake detectors against worst-case filters: Gains, Costs and Limits

- **Authors**: Ali Alavi
- **Date / sources**: 2026-11-21 · arxiv
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Links**: [Paper](https://arxiv.org/abs/2611.28718) · [PDF](https://arxiv.org/pdf/2611.28718v1)

Speech deepfake detectors make few errors on standard benchmarks, yet a simple attack defeats them: the attacker passes fake speech through one short filter, tuned against the detector, and many fakes then pass as real. Training with random filters does not stop this attack, because the attacker uses the worst filter, not a random one. We therefore train the detector against the worst case: during training, a small…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 13. LEGAL AND GOVERNANCE STANDARDS FOR REGULATING BIOMETRIC IDENTIFICATION AND VOICE CLONING TECHNOLOGIES

- **Authors**: Abdulfayz Şerali Öğli Turdiyev
- **Date / sources**: 2026-11-20 · semantic_scholar
- **Relevance**: 12 pts · Speech Generation, Recognition & Dialogue: voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/188638bcb1c7409cf70bf3bba43649040809a532) · [PDF](https://www.in-academy.uz/index.php/YOITJ/article/download/93751/65927)

Maqolada biometrik identifikatsiya va ovoz klonlaş texnologiyalarini tartibga solişning huquqiy-boşqaruv standartlari tahlil qilinadi. Generativ sun’iy intellekt davrida ovoz klonlaş va Deepfake biometrik autentifikatsiya tizimlari uçun yangi xavflar tuğdirayotgani asoslanadi. «Şaxsga doir ma’lumotlar töğrisida»gi Qonundagi böşliqlar (ovoz klonining huquqiy maqomi, oçiq manbalardan foydalaniş, transçegaraviy uzatiş,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 14. When Being Wrong Is Right: Reverse-Capability Audio CAPTCHAs through Psychoacoustic Design

- **Authors**: Mingjie Bao, Yu Dai, Guangke Chen, Guozhu Meng
- **Date / sources**: 2026-11-21 · arxiv, semantic_scholar
- **Relevance**: 11 pts · Audio & Speech Language Models: audio-language model; Speech Generation, Recognition & Dialogue: automatic speech recognition; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.28823) · [PDF](https://arxiv.org/pdf/2611.28823v1)

Large audio-language models (LALMs) have recently been shown to bypass audio CAPTCHAs designed around limitations of automatic speech recognition. To address this threat, we introduce reverse-capability verification, a general CAPTCHA framework that reverses the conventional human-easy, machine-hard relationship with respect to the physical ground truth. It selects challenges in which stable human perceptual…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 15. Ultrasound Watermark: Real-time Acoustic Watermarking against Voice Scams on Smartphones

- **Authors**: Renzhi Hao, Shirui Cao, Yizhu Wen, Rishav Gupta, Dharani Nadendla, Mehran Kafai, Hanqing Guo, Dong Li
- **Date / sources**: 2026-11-23 · arxiv, semantic_scholar
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.30106) · [PDF](https://arxiv.org/pdf/2611.30106v1)

Recent advances in text-to-speech (TTS), voice conversion (VC), and AI-driven speech synthesis enable adversaries to convincingly impersonate trusted individuals during phone calls. Existing defenses often rely on offline analysis, degrade under telephony distortions, or remain vulnerable to adaptive attacks. To address these limitations, we present Ultrasound Watermark, a real-time, smartphone-native framework that…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 16. LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation

- **Authors**: Yuxuan Jiang, Zehua Chen, Yusheng Dai, Andong Wang, Weibei Dou, Jun Zhu
- **Date / sources**: 2026-11-23 · arxiv
- **Relevance**: 10 pts · Generative Music & Audio: audio generation
- **Links**: [Paper](https://arxiv.org/abs/2611.30714) · [PDF](https://arxiv.org/pdf/2611.30714v1)

Video-to-audio generation synthesizes sound that matches a video in content and timing, with applications ranging from film post-production to live streaming, games and interactive world models. Interactive applications receive video continuously and need the sound to follow it in real time, yet most existing video-to-audio models are bidirectional and must observe an entire clip before producing any sound. We…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 17. Music Circuit: Trace and Control Style Dynamics in Large Music Generation Model

- **Authors**: Ruiji Yu, Wenye Ma, Gus Xia
- **Date / sources**: 2026-11-22 · arxiv
- **Relevance**: 10 pts · Generative Music & Audio: music generation
- **Links**: [Paper](https://arxiv.org/abs/2611.29475) · [PDF](https://arxiv.org/pdf/2611.29475v1)

Musical style, a global attribute that functions throughout a whole piece, is a lever widely used by users in modern large music generation models. Yet how style is represented inside these models, and which components drive it, remains largely unexplored. In language models, circuit analysis traces a representation to a sparse sub-network of a few key components, namely attention heads and MLP neurons, and has been…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 18. Synthetic Twins: Closing the Gap Between TTS Test Sets and Real Recordings in Turkish ASR Evaluation

- **Authors**: Nur Yağmur Tuncer, Mustafa Sertaç Türkel, Fatma Nur Korkmaz, Ahmet Tuğrul Bayrak
- **Date / sources**: 2026-11-23 · arxiv, semantic_scholar
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: text-to-speech, automatic speech recognition; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.30694) · [PDF](https://arxiv.org/pdf/2611.30694v1)

Speech synthesized by text-to-speech engines is a low-cost substitute for recorded test sets in automatic speech recognition, yet an off-the-shelf synthetic test set is worth only a few dozen real recordings for estimating the real error rate of a recognizer. This paper examines which properties of real recordings are missing from synthetic speech and how much of the gap can be closed. For 507 Turkish Common Voice…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 19. IteraSong: LLM-Guided Iterative Symbolic Music Creation in a Web DAW

- **Authors**: Di Lu, Xinran Zhang, Yan Gao, Yuan Zhang, Xiaoqing Wang, Qingwen Zhou, Xiaobing Li, Maosong Sun
- **Date / sources**: 2026-11-22 · arxiv, semantic_scholar
- **Relevance**: 9 pts · Music Foundation Models & Representations: symbolic music; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29225) · [PDF](https://arxiv.org/pdf/2611.29225v1)

Music creation is inherently iterative, yet many symbolic generation systems still center on producing or regenerating isolated outputs. We present IteraSong, an interactive web-based Digital Audio Workstation (DAW) for LLM-guided iterative symbolic music creation. Unlike one-shot generation systems, IteraSong supports a generate-audition-edit-refine loop over a persistent multi-track project. Users initialize a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 20. Which Layer to Trust? Layer Selection in Frozen Speech Encoders for Singing-Voice Deepfake Detection under Signal Corruption

- **Authors**: Benjamin Hurt, Yefei Yang
- **Date / sources**: 2026-11-23 · arxiv
- **Relevance**: 6 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake
- **Links**: [Paper](https://arxiv.org/abs/2611.29871) · [PDF](https://arxiv.org/pdf/2611.29871v1)

Frozen self-supervised speech encoders have been frequently used for audio deepfake detection. However, the layers are usually chosen from a development set. We examine this choice for singing-voice deepfake detection on CtrSVDD. We train one detection head per layer, plus a learned layer mix, on frozen XEUS (3-4 seeds) and XLS-R (2 seeds). We test on clean audio and under noise, reverberation and lossy coding. On…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 21. SpeechSplice: Pronunciation Control in Encoder-Decoder LLM-based TTS by Replacing Encoder Hidden States

- **Authors**: Kiyoshi Kurihara, Jumpei Ukita, Yusuke Iwasawa, Yutaka Matsuo
- **Date / sources**: 2026-11-23 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.30927) · [PDF](https://arxiv.org/pdf/2611.30927v1)

Most large language model (LLM)-based text-to-speech (TTS) methods offer no explicit function for correcting pronunciation. Consequently, these systems frequently mispronounce many everyday words, such as proper nouns, heteronyms, numerals, and domain-specific terms. While weight-editing or fine-tuning can mitigate this, these solutions risk quality degradation and must operate offline. We propose SpeechSplice, a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 22. Scoring L2 Pronunciation Without Synthesis: Counterfactual Velocity Contrast in Frozen Flow-Matching TTS

- **Authors**: Zehan Liu
- **Date / sources**: 2026-11-23 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29985) · [PDF](https://arxiv.org/pdf/2611.29985v1)

Flow-matching text-to-speech (TTS) models learn how native speakers realize a text, yet this knowledge is used only for synthesis. We show that a frozen TTS model can score non-native (L2) pronunciation without generating audio. For a learner utterance, we compare the model's velocity-prediction error under the target text with its error under a counterfactual text (dropped or swapped) on the same noised input; the…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 23. SayWhen: Set-Valued Semantic Commitment for Low-Regret Early Speech

- **Authors**: Tianyi Huang, Lucas Su, Fred Zhang, Andy Liang, Gordon Li
- **Date / sources**: 2026-11-23 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.31101) · [PDF](https://arxiv.org/pdf/2611.31101v1)

Speaking early turns a prediction into an irreversible public commitment. We introduce SayWhen, a test-time controller that selects a task-directed act shared across typed continuation plans and controls its release as speech. A persistent veto blocks playback when intervening transcripts invalidate the candidate. We define regret-free early speech (RFES) to measure supported pre-endpoint releases without scored…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 24. Tenlai-TTS 2.0: Continuous-Representation LLM-Based TTS System with End-to-End Training

- **Authors**: Changfeng Gao, Yong Ren, Jun Yuan, Zhengkun Tian, Ye Bai, Zhao You, Shidong Shang
- **Date / sources**: 2026-11-22 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.29226) · [PDF](https://arxiv.org/pdf/2611.29226v1)

Autoregressive text-to-speech (TTS) with continuous speech latents avoids quantization-induced information loss, but typically relies on a latent space that is learned separately and then frozen before language-model training. Such a space must satisfy two competing requirements: it must retain enough acoustic detail for high-fidelity reconstruction, yet be sufficiently structured and regularized to support…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
