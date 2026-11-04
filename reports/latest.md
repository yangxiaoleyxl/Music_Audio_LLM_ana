# Music / Audio Foundation Model Research Radar — 2026-11-04

> Lookback window: 2026-10-28 to 2026-11-04 · New papers: 22 · New models: 30 · relevant papers/models in window: 50/64 · raw papers/models: 195/353

Sources: arxiv=106 · semantic_scholar=89 · huggingface_models=353

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [arpanpathak/staleynet-checkpoints](https://huggingface.co/arpanpathak/staleynet-checkpoints) | 2026-11-04 | text-to-audio | 42 | 1 | 0 | 1 | cc-by-sa-4.0 |
| 2 | [khaled5/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/khaled5/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) | 2026-11-04 | automatic-speech-recognition | 40 | 1 | 0 | 0 | other |
| 3 | [Infinix-io/maya2-native](https://huggingface.co/Infinix-io/maya2-native) | 2026-11-04 | text-to-speech | 39 | 1 | 0 | 0 | apache-2.0 |
| 4 | [MusicForge/magnet-medium-8bit](https://huggingface.co/MusicForge/magnet-medium-8bit) | 2026-11-04 | text-to-audio | 34 | 2 | 0 | 0 | cc-by-nc-4.0 |
| 5 | [MusicForge/magnet-small-8bit](https://huggingface.co/MusicForge/magnet-small-8bit) | 2026-11-04 | text-to-audio | 34 | 2 | 0 | 0 | cc-by-nc-4.0 |
| 6 | [netease-youdao/Confucius4-TTS](https://huggingface.co/netease-youdao/Confucius4-TTS) | 2026-11-04 | text-to-speech | 31 | 1 | 1902 | 43 | apache-2.0 |
| 7 | [adventists-ai/DuplexJev-4B-Para](https://huggingface.co/adventists-ai/DuplexJev-4B-Para) | 2026-11-04 | audio-text-to-text | 19 | 1 | 217 | 4 | cc-by-nc-4.0 |
| 8 | [goaicorp/mos-mms-tts](https://huggingface.co/goaicorp/mos-mms-tts) | 2026-11-04 | text-to-speech | 17 | 1 | 0 | 1 | cc-by-nc-4.0 |
| 9 | [goaicorp/dyu-mms-tts](https://huggingface.co/goaicorp/dyu-mms-tts) | 2026-11-04 | text-to-speech | 17 | 1 | 0 | 1 | cc-by-nc-4.0 |
| 10 | [goaicorp/mos-tts](https://huggingface.co/goaicorp/mos-tts) | 2026-11-04 | text-to-speech | 17 | 1 | 3 | 0 | cc-by-nc-4.0 |
| 11 | [goaicorp/mos-omnivoice](https://huggingface.co/goaicorp/mos-omnivoice) | 2026-11-04 | text-to-speech | 15 | 1 | 6 | 0 | cc-by-nc-4.0 |
| 12 | [goaicorp/mos-pocket-tts](https://huggingface.co/goaicorp/mos-pocket-tts) | 2026-11-04 | text-to-speech | 15 | 1 | 0 | 0 | cc-by-4.0 |
| 13 | [deinhofe/pocket-tts-onnx](https://huggingface.co/deinhofe/pocket-tts-onnx) | 2026-11-04 | text-to-speech | 15 | 1 | 0 | 0 | cc-by-4.0 |
| 14 | [wjcwqc/MireskaVoice-ming](https://huggingface.co/wjcwqc/MireskaVoice-ming) | 2026-11-04 | text-to-speech | 15 | 1 | 0 | 0 | mit |
| 15 | [muhammedekinci/ema-lightning-safe](https://huggingface.co/muhammedekinci/ema-lightning-safe) | 2026-11-04 | text-to-speech | 13 | 1 | 0 | 1 | apache-2.0 |
| 16 | [litert-community/DAC-16kHz-LiteRT](https://huggingface.co/litert-community/DAC-16kHz-LiteRT) | 2026-11-04 | audio-to-audio | 13 | 1 | 74 | 0 | mit |
| 17 | [superretrosfx/RVC-MODEL](https://huggingface.co/superretrosfx/RVC-MODEL) | 2026-11-04 | audio-to-audio | 13 | 1 | 0 | 0 | mit |
| 18 | [sulabhkatiyar/indic-tiny-tts-hindi](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-hindi) | 2026-11-04 | text-to-speech | 11 | 1 | 141 | 0 | cc-by-4.0 |
| 19 | [sulabhkatiyar/indic-tiny-tts-gujarati](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-gujarati) | 2026-11-04 | text-to-speech | 11 | 1 | 6 | 0 | cc-by-4.0 |
| 20 | [sulabhkatiyar/indic-tiny-tts-punjabi](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-punjabi) | 2026-11-04 | text-to-speech | 11 | 1 | 4 | 0 | cc-by-4.0 |
| 21 | [sulabhkatiyar/indic-tiny-tts-malayalam](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-malayalam) | 2026-11-04 | text-to-speech | 11 | 1 | 4 | 0 | cc-by-4.0 |
| 22 | [sulabhkatiyar/indic-tiny-tts-telugu](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-telugu) | 2026-11-04 | text-to-speech | 11 | 1 | 4 | 0 | cc-by-4.0 |
| 23 | [sulabhkatiyar/indic-tiny-tts-bengali](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-bengali) | 2026-11-04 | text-to-speech | 11 | 1 | 4 | 0 | cc-by-4.0 |
| 24 | [sulabhkatiyar/indic-tiny-tts-tamil](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-tamil) | 2026-11-04 | text-to-speech | 11 | 1 | 4 | 0 | cc-by-4.0 |
| 25 | [sulabhkatiyar/indic-tiny-tts-english](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-english) | 2026-11-04 | text-to-speech | 11 | 1 | 0 | 0 | cc-by-4.0 |
| 26 | [sulabhkatiyar/indic-tiny-tts-odia](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-odia) | 2026-11-04 | text-to-speech | 11 | 1 | 0 | 0 | cc-by-4.0 |
| 27 | [sulabhkatiyar/indic-tiny-tts-assamese](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-assamese) | 2026-11-04 | text-to-speech | 11 | 1 | 0 | 0 | cc-by-4.0 |
| 28 | [sulabhkatiyar/indic-tiny-tts-marathi](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-marathi) | 2026-11-04 | text-to-speech | 11 | 1 | 0 | 0 | cc-by-4.0 |
| 29 | [sulabhkatiyar/indic-tiny-tts-kannada](https://huggingface.co/sulabhkatiyar/indic-tiny-tts-kannada) | 2026-11-04 | text-to-speech | 11 | 1 | 0 | 0 | cc-by-4.0 |
| 30 | [AlmawaveLabs/Velvet2-3B-Speech](https://huggingface.co/AlmawaveLabs/Velvet2-3B-Speech) | 2026-11-04 | audio-text-to-text | 10 | 1 | 145 | 15 | apache-2.0 |

### Model cards

#### M1. arpanpathak/staleynet-checkpoints

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-audio / unknown
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license cc-by-sa-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M2. khaled5/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: automatic-speech-recognition / nemo
- **Relevance**: 40 pts · Audio Understanding & Reasoning: audio reasoning, audio question answering, audio understanding; Speech Generation, Recognition & Dialogue: automatic speech recognition, speech translation; Audio & Speech Language Models: speech llm; model card links an arXiv paper
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2310.09424](https://arxiv.org/abs/2310.09424)
- **Datasets / base models**: nvidia/Granary-v2 / nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16
- **Variants in family**: —

#### M3. Infinix-io/maya2-native

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 39 pts · Speech Generation, Recognition & Dialogue: speech generation, speech synthesis, text-to-speech (pipeline tag); Generative Music & Audio: audio generation, neural audio codec; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3-1.7B-Base
- **Variants in family**: —

#### M4. MusicForge/magnet-medium-8bit

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-audio / mlx
- **Relevance**: 34 pts · Generative Music & Audio: text-to-music, text to music, text-to-audio (pipeline tag); model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2401.04577](https://arxiv.org/abs/2401.04577)
- **Datasets / base models**: unknown / facebook/magnet-medium-30secs
- **Variants in family**: MusicForge/magnet-medium-4bit

#### M5. MusicForge/magnet-small-8bit

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-audio / mlx
- **Relevance**: 34 pts · Generative Music & Audio: text-to-music, text to music, text-to-audio (pipeline tag); model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2401.04577](https://arxiv.org/abs/2401.04577)
- **Datasets / base models**: unknown / facebook/magnet-small-30secs
- **Variants in family**: MusicForge/magnet-small-4bit

#### M6. netease-youdao/Confucius4-TTS

- **Created / updated**: 2026-06-02 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 31 pts · Speech Generation, Recognition & Dialogue: speech generation, speech synthesis, text-to-speech (pipeline tag); model card links an arXiv paper; declares license apache-2.0; community likes 43
- **Adoption signals**: downloads=1902 · likes=43 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2608.11650](https://arxiv.org/abs/2608.11650)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M7. adventists-ai/DuplexJev-4B-Para

- **Created / updated**: 2026-10-08 / 2026-11-04
- **Task / library**: audio-text-to-text / vllm
- **Relevance**: 19 pts · Audio & Speech Language Models: speech llm; model card links an arXiv paper; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=217 · likes=4 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2610.02638](https://arxiv.org/abs/2610.02638)
- **Datasets / base models**: unknown / adventists-ai/DuplexJev-4B-Turn, Qwen/Qwen3-4B, Qwen/Qwen3-ASR-0.6B
- **Variants in family**: —

#### M8. goaicorp/mos-mms-tts

- **Created / updated**: 2024-07-17 / 2026-11-04
- **Task / library**: text-to-speech / transformers
- **Relevance**: 17 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-4.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / facebook/mms-tts-mos
- **Variants in family**: —

#### M9. goaicorp/dyu-mms-tts

- **Created / updated**: 2026-05-24 / 2026-11-04
- **Task / library**: text-to-speech / transformers
- **Relevance**: 17 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-4.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / facebook/mms-tts
- **Variants in family**: —

#### M10. goaicorp/mos-tts

- **Created / updated**: 2026-05-05 / 2026-11-04
- **Task / library**: text-to-speech / transformers
- **Relevance**: 17 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=3 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / goaicorp/mos-mms-tts
- **Variants in family**: —

#### M11. goaicorp/mos-omnivoice

- **Created / updated**: 2026-11-03 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=6 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / k2-fsa/OmniVoice
- **Variants in family**: —

#### M12. goaicorp/mos-pocket-tts

- **Created / updated**: 2026-11-03 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/pocket-tts
- **Variants in family**: —

#### M13. deinhofe/pocket-tts-onnx

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-speech / pocket-tts-onnx
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/pocket-tts
- **Variants in family**: —

#### M14. wjcwqc/MireskaVoice-ming

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / inclusionAI/Ming-3.0-tts-0.5b
- **Variants in family**: —

#### M15. muhammedekinci/ema-lightning-safe

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-speech / ema-lightning
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2405.14867](https://arxiv.org/abs/2405.14867)
- **Datasets / base models**: unknown / canberkkkkkk/ema-lightning
- **Variants in family**: —

#### M16. litert-community/DAC-16kHz-LiteRT

- **Created / updated**: 2026-09-22 / 2026-11-04
- **Task / library**: audio-to-audio / litert
- **Relevance**: 13 pts · Generative Music & Audio: neural audio codec; declares license mit
- **Adoption signals**: downloads=74 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / descript/dac_16khz
- **Variants in family**: —

#### M17. superretrosfx/RVC-MODEL

- **Created / updated**: 2025-12-11 / 2026-11-04
- **Task / library**: audio-to-audio / keras-hub
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: voice cloning; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: openbmb/UltraData-SFT-Agent-2609, openbmb/UltraData-RL-2609 / nex-agi/Nex-N2.5-mini
- **Variants in family**: —

#### M18. sulabhkatiyar/indic-tiny-tts-hindi

- **Created / updated**: 2026-10-18 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=141 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M19. sulabhkatiyar/indic-tiny-tts-gujarati

- **Created / updated**: 2026-11-02 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=6 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M20. sulabhkatiyar/indic-tiny-tts-punjabi

- **Created / updated**: 2026-11-02 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=4 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M21. sulabhkatiyar/indic-tiny-tts-malayalam

- **Created / updated**: 2026-10-23 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=4 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M22. sulabhkatiyar/indic-tiny-tts-telugu

- **Created / updated**: 2026-10-23 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=4 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M23. sulabhkatiyar/indic-tiny-tts-bengali

- **Created / updated**: 2026-10-23 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=4 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M24. sulabhkatiyar/indic-tiny-tts-tamil

- **Created / updated**: 2026-10-23 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=4 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M25. sulabhkatiyar/indic-tiny-tts-english

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, iAkashPaul/limmits-2024 / unknown
- **Variants in family**: —

#### M26. sulabhkatiyar/indic-tiny-tts-odia

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M27. sulabhkatiyar/indic-tiny-tts-assamese

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa / unknown
- **Variants in family**: —

#### M28. sulabhkatiyar/indic-tiny-tts-marathi

- **Created / updated**: 2026-11-04 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa, iAkashPaul/limmits-2024 / unknown
- **Variants in family**: —

#### M29. sulabhkatiyar/indic-tiny-tts-kannada

- **Created / updated**: 2026-11-02 / 2026-11-04
- **Task / library**: text-to-speech / unknown
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: sulabhkatiyar/indic-tts-mini-24k, sulabhkatiyar/indic-tts-multilingual-prepared, ai4bharat/Rasa, iAkashPaul/limmits-2024 / unknown
- **Variants in family**: —

#### M30. AlmawaveLabs/Velvet2-3B-Speech

- **Created / updated**: 2026-10-23 / 2026-11-04
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0; community likes 15
- **Adoption signals**: downloads=145 · likes=15 · trending=0.0
- **License / access**: apache-2.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / AlmawaveLabs/Velvet2-3B
- **Variants in family**: —

## Research signals

- Speech Generation, Recognition & Dialogue: 8 papers
- Audio & Speech Language Models: 7 papers
- Evaluation, Alignment, Safety & Copyright: 4 papers
- Generative Music & Audio: 4 papers
- Audio Understanding & Reasoning: 3 papers
- Music Foundation Models & Representations: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [Confidence-Aware Aggregation for Multimodal Audio Reasoning](https://arxiv.org/abs/2611.04580) | 2026-11-03 | 38 | Audio & Speech Language Models, Audio Understanding & Reasoning | [repo](https://github.com/michelolzam/lalm-self-consistency) |
| 2 | [TTSonic: A Unified Framework for Composable and Controllable Speech Generation](https://arxiv.org/abs/2611.04282) | 2026-11-03 | 29 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 3 | [VeriSpoof: Beyond Real or Fake with One Audio LLM](https://arxiv.org/abs/2611.04634) | 2026-11-03 | 27 | Audio & Speech Language Models, Evaluation, Alignment, Safety & Copyright | — |
| 4 | [Detector-Guided Vocoder Training for Adversarial Text-to-Speech Synthesis](https://arxiv.org/abs/2611.04511) | 2026-11-03 | 25 | Speech Generation, Recognition & Dialogue, Evaluation, Alignment, Safety & Copyright | — |
| 5 | [Averaging Collusion Breaks Traceability in Personalized Neural Audio Watermarking](https://arxiv.org/abs/2611.04400) | 2026-11-03 | 17 | Evaluation, Alignment, Safety & Copyright | [repo](https://github.com/Silwan5z/neural-audio-watermark-collusion-attack) |
| 6 | [ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models](https://arxiv.org/abs/2611.04480) | 2026-11-03 | 13 | Audio & Speech Language Models | — |
| 7 | [Technical Evaluations in the Field of AI Music Composition](https://www.semanticscholar.org/paper/f3554f8aaf94ab41137142194ebcf8c394ad0041) | 2026-11-02 | 12 | Generative Music & Audio | — |
| 8 | [PianoBench: Evaluating Musical Perception and Reasoning in Language Models](https://arxiv.org/abs/2611.03839) | 2026-11-02 | 12 | Audio & Speech Language Models, Music Foundation Models & Representations | — |
| 9 | [NepTTS-Bench: Native-Speaker Benchmarking and NepaliMOS for Nepali Text-to-Speech](https://arxiv.org/abs/2611.03718) | 2026-10-31 | 12 | Speech Generation, Recognition & Dialogue | [repo](https://github.com/Ampixa/neptts-bench) |
| 10 | [SciPhi-Chat: Training a Spatial Audio Agent for Question Answering, Dialogue, and Tool Use](https://arxiv.org/abs/2611.04114) | 2026-11-03 | 10 | Audio Understanding & Reasoning | [repo](https://github.com/microsoft/sciphi-chat) |
| 11 | [Do Multi-Turn Conversational Capabilities Carry Over from Text to Speech? A Parallel Multilingual Benchmark](https://arxiv.org/abs/2611.04390) | 2026-11-03 | 10 | Audio & Speech Language Models | [repo](https://github.com/QwenLM/Omnilingua-Bench) |
| 12 | [ATLAS-Audio Translation for Live Attraction System](https://www.semanticscholar.org/paper/12b1b4497011a3132be9dfc30777ee14b2ac4d9d) | 2026-10-29 | 9 | Speech Generation, Recognition & Dialogue | — |
| 13 | [Cross-Codec Robustness in Speech Watermarking](https://arxiv.org/abs/2611.04716) | 2026-11-03 | 7 | Generative Music & Audio | — |
| 14 | [Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](https://arxiv.org/abs/2611.05275) | 2026-11-03 | 6 | Speech Generation, Recognition & Dialogue | — |
| 15 | [Hybrid acoustic and pretrained embedding feature fusion for unmanned aerial vehicle detection using stacking ensemble learning under a leakage-aware evaluation protocol](https://arxiv.org/abs/2611.04714) | 2026-11-03 | 6 | Evaluation, Alignment, Safety & Copyright | — |
| 16 | [AI for eGovernance: Leveraging Language Technologies For Digital Inclusion](https://arxiv.org/abs/2611.04820) | 2026-11-03 | 6 | Speech Generation, Recognition & Dialogue | — |
| 17 | [Transformer-Based Automatic Speech Recognition Development for Transcription and Clinical Information Extraction in Indonesian on Electronic Health Records](https://www.semanticscholar.org/paper/607975e9d07e2377b8627befe9a0af22f4eeedd6) | 2026-11-02 | 6 | Speech Generation, Recognition & Dialogue | — |
| 18 | [Performance evaluation of deep learning models for Indian-accented English automatic speech recognition](https://www.semanticscholar.org/paper/e04503f82e7fe59842e08c9a64db97048edacdd6) | 2026-11-02 | 6 | Speech Generation, Recognition & Dialogue | — |
| 19 | [Fuse To Align: Multimodal Representation Learning for Retrieval via Hypergraph Regularization](https://arxiv.org/abs/2611.03370) | 2026-11-02 | 6 | Audio Understanding & Reasoning | — |
| 20 | [CrowdForge: Effects of Audio and Visual Audience Participation Modalities on Agency, Collaboration, and Engagement in AI-Mediated MR Performances](https://arxiv.org/abs/2611.03389) | 2026-11-02 | 6 | Generative Music & Audio | — |
| 21 | [Be My Ears: Enabling Semantic Alerting for Earphone Wearers with Pheme](https://www.semanticscholar.org/paper/105c2cd974adfca639a9e5edee251ba8bf7b68c6) | 2026-11-01 | 6 | Audio & Speech Language Models | — |
| 22 | [Reflex: Fast Robot Policy Serving by Reusing and Correcting Past Actions](https://arxiv.org/abs/2611.00524) | 2026-10-31 | 6 | Generative Music & Audio | — |

## Paper cards

### 1. Confidence-Aware Aggregation for Multimodal Audio Reasoning

- **Authors**: Michel Olvera, Paraskevas Stamatiadis, Ga{ë}l Richard
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 38 pts · Audio Understanding & Reasoning: audio reasoning, audio understanding, multimodal audio; Audio & Speech Language Models: audio language model; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04580) · [PDF](https://arxiv.org/pdf/2611.04580v1) · [Code 1](https://github.com/michelolzam/lalm-self-consistency)

Large Audio Language Models (LALMs) enable generative reasoning over complex acoustic scenes but often exhibit prediction instability. We show that this variability can serve as a reliability metric via inference-time self-consistency and confidence-aware aggregation. Using a log-probability--based scoring framework, candidate answers are weighted by model likelihoods, leveraging reasoning diversity and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. TTSonic: A Unified Framework for Composable and Controllable Speech Generation

- **Authors**: Zhedong Zhang, Kaiwen Zhou, Junyan Wu, Shengqiang Li, Xuran Chi, Xingui Zeng, Rui Yan, Xu Chen
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 29 pts · Speech Generation, Recognition & Dialogue: speech generation, text-to-speech, voice cloning; Audio & Speech Language Models: speech foundation model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04282) · [PDF](https://arxiv.org/pdf/2611.04282v1)

Modern text-to-speech (TTS) systems can synthesize natural and expressive speech, yet a practical speech foundation model must go beyond naturalness to offer stable quality, precise controllability, and a broad set of composable capabilities within a unified framework. We present TTSonic, a unified speech generation model that supports zero-shot TTS, voice cloning, prosody cloning, instruction following, voice…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. VeriSpoof: Beyond Real or Fake with One Audio LLM

- **Authors**: Yang Xiao, Ting Dang
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 27 pts · Audio & Speech Language Models: audio language model, audio llm; Evaluation, Alignment, Safety & Copyright: speech deepfake; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04634) · [PDF](https://arxiv.org/pdf/2611.04634v1)

A speech deepfake detector estimates whether a recording is synthetic, but a forensic analyst also asks which system produced it, whether recordings share a source, and what evidence supports each conclusion. We present VeriSpoof, an audio language model that unifies five tasks with shared weights: deepfake detection, generator attribution (generator, acoustic model and vocoder), recording-condition analysis,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Detector-Guided Vocoder Training for Adversarial Text-to-Speech Synthesis

- **Authors**: Jiayan Cui, Davide Salvi, Paolo Bestagini, Stefano Tubaro
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 25 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; Evaluation, Alignment, Safety & Copyright: speech deepfake; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04511) · [PDF](https://arxiv.org/pdf/2611.04511v1)

In this paper, we propose a novel Text-to-Speech (TTS) framework designed to perform adversarial attacks against speech deepfake detection systems. Given a TTS model and a detector capable of classifying its outputs as synthetic, our approach fine-tunes the vocoder by integrating the detector into the TTS training loop. Unlike traditional adversarial methods that rely on post-hoc perturbations or external noise…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Averaging Collusion Breaks Traceability in Personalized Neural Audio Watermarking

- **Authors**: Yangming Liu, Haiyun Li, Dongfu Song, Ziang Xu, Jiehui Luo, Yining Zhang, Zhiyong Wu
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 17 pts · Evaluation, Alignment, Safety & Copyright: audio watermarking; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04400) · [PDF](https://arxiv.org/pdf/2611.04400v1) · [Code 1](https://github.com/Silwan5z/neural-audio-watermark-collusion-attack)

Personalized neural audio watermarking systems embed user-specific payloads into audio to trace the user associated with a leaked or misused copy. Existing evaluations mainly assume access to a single personalized copy, but real-world distribution may expose multiple copies of the same recording. We find that simple sample-wise averaging breaks traceability: averaging only two copies produces tracing-failure rates…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models

- **Authors**: Ming-Hao Hsu, Shujie Liu, Yuxuan Hu, Yuxiang Wang, Yingda Shen, Jinyu Li, Zhizheng Wu
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Audio & Speech Language Models: audio language model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04480) · [PDF](https://arxiv.org/pdf/2611.04480v1)

Audio language models are meant to answer questions from the audio itself, but an hour-long recording rarely fits in their context, and the answer often depends on a few seconds of it. Transcribing the recording first makes it fit but discards sounds and voices, while systems that return to the audio must be trained for this behavior. We propose ReListen, a training-free method in which a frozen audio language model…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. Technical Evaluations in the Field of AI Music Composition

- **Authors**: M. S. D. Prithaviraj Ashok Londhe, H. B. J. L. S. Bhadake
- **Date / sources**: 2026-11-02 · semantic_scholar
- **Relevance**: 12 pts · Generative Music & Audio: text-to-music, music generation
- **Links**: [Paper](https://www.semanticscholar.org/paper/f3554f8aaf94ab41137142194ebcf8c394ad0041) · [PDF](https://doi.org/10.48175/ijarsct-40525)

AI-based music composition has progressed from symbolic melody generation to systems that produce audio from natural-language prompts, melodic references, or combinations of both. However, the perceived usefulness of a generated track cannot be captured by audio realism alone. A system may sound convincing yet ignore the requested mood, lose musical structure over time, offer little editing control, or provide…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. PianoBench: Evaluating Musical Perception and Reasoning in Language Models

- **Authors**: Louis Bradshaw, Irmak Bukey, Daniel Chenyu Lin, John Thickstun, Chris Donahue
- **Date / sources**: 2026-11-02 · arxiv, semantic_scholar
- **Relevance**: 12 pts · Audio & Speech Language Models: audio-language model; Music Foundation Models & Representations: music understanding; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.03839) · [PDF](https://arxiv.org/pdf/2611.03839v1)

Multimodal language models continue to improve on broad music understanding benchmarks, but which musical features can they perceive and reason about? We investigate this question by introducing PianoBench, a benchmark that tasks language models with reasoning about musical performances across congruent acoustic and symbolic input representations. PianoBench is derived from our new multimodal, training-scale dataset…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. NepTTS-Bench: Native-Speaker Benchmarking and NepaliMOS for Nepali Text-to-Speech

- **Authors**: Ashish Thapa, Rupak Ghimire, Lekhnath Sharma Pathak
- **Date / sources**: 2026-10-31 · arxiv
- **Relevance**: 12 pts · Speech Generation, Recognition & Dialogue: text-to-speech; has open-source code link
- **Links**: [Paper](https://arxiv.org/abs/2611.03718) · [PDF](https://arxiv.org/pdf/2611.03718v1) · [Code 1](https://github.com/Ampixa/neptts-bench)

Nepali TTS has reached a point where multiple systems are available, but there is no shared evaluation to compare them. NepTTS-Bench was created to address what existing automated and manual evaluation systems lack for Nepali TTS. A controlled benchmark with phonological grounding which contains 205 sentences (77 minimal pairs targeting aspiration, retroflex/dental contrasts, nasalization, gemination, and schwa…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. SciPhi-Chat: Training a Spatial Audio Agent for Question Answering, Dialogue, and Tool Use

- **Authors**: Gijs Wijngaard, Hannes Gamper, Sebastian Braun
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 10 pts · Audio Understanding & Reasoning: audio question answering; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04114) · [PDF](https://arxiv.org/pdf/2611.04114v1) · [Code 1](https://github.com/microsoft/sciphi-chat)

Spatial audio question answering requires associating sound identities with locations and reasoning about their relations. This paper introduces SciPhi-Chat, a spatial audio agent that answers questions, conducts multi-turn dialogue, and calls tools on first-order ambisonic recordings. The accompanying MASU benchmark contains 12,000 samples across 42 task categories, the widest task coverage of any spatial model,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 11. Do Multi-Turn Conversational Capabilities Carry Over from Text to Speech? A Parallel Multilingual Benchmark

- **Authors**: Jiaming Zhou, Pei Zhang, Shiwan Zhao, Zhijun Wang, Baosong Yang, Yong Qin
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 10 pts · Audio & Speech Language Models: speech-language model; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04390) · [PDF](https://arxiv.org/pdf/2611.04390v1) · [Code 1](https://github.com/QwenLM/Omnilingua-Bench)

Successful multi-turn voice interaction requires models to retain information from earlier turns, follow persistent instructions, and track revisions to conversational state. These abilities are usually evaluated from transcripts, leaving open whether successes demonstrated from text carry over when the same turns are spoken, and whether this transfer is consistent across languages. We introduce Omnilingua-AudioMC,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 12. ATLAS-Audio Translation for Live Attraction System

- **Authors**: Vinutha H. P. Dr., G. Ramya, S. K. Sanjana, S. Shrusti, D. Vidya
- **Date / sources**: 2026-10-29 · semantic_scholar
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech
- **Links**: [Paper](https://www.semanticscholar.org/paper/12b1b4497011a3132be9dfc30777ee14b2ac4d9d) · [PDF](https://www.indjcst.com/archiver/archives/atlas_audio_translation_for_live_attraction_system.pdf)

Tourists visiting unfamiliar regions often face language barriers that make it difficult to understand local attractions, historical landmarks, and cultural information. To address this challenge, this paper presents ATLAS (Audio Translation for Live Attraction Systems), a web-based application designed to facilitate multilingual communication through speech processing and language translation. The system integrates…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 13. Cross-Codec Robustness in Speech Watermarking

- **Authors**: Olli-Pekka Pauna, Xin Wang, Lauri Juvela
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 7 pts · Generative Music & Audio: neural audio codec; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04716) · [PDF](https://arxiv.org/pdf/2611.04716v1)

Generative speech models synthesize audio that is difficult to distinguish from human recordings. Synthetic speech can be watermarked as a proactive disclosure method, but watermarking models remain vulnerable to resynthesis attacks using neural audio codecs. This article investigates speech watermarking robustness across neural codec and digital signal processing attacks, when specific neural codecs are used for…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 14. Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems

- **Authors**: Pengfei Zhou, Yixing Ma, Hexin Wang, Weidong Tang, Zhenglin Wan, Wangbo Zhao, Yang You
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: speech generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.05275) · [PDF](https://arxiv.org/pdf/2611.05275v1)

Artificial general intelligence (AGI) requires a method that can understand, generate, reason, and act across diverse domains and modalities. Rather than relying on a single model to master every capability, a promising path toward AGI now is to orchestrate a heterogeneous ecosystem of specialized models, tools, and policies (candidates) into a unified AI system. At the heart of this vision lies a fundamental…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 15. Hybrid acoustic and pretrained embedding feature fusion for unmanned aerial vehicle detection using stacking ensemble learning under a leakage-aware evaluation protocol

- **Authors**: Zahid Iqbal
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Evaluation, Alignment, Safety & Copyright: audio benchmark; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04714) · [PDF](https://arxiv.org/pdf/2611.04714v1)

Small multirotor drones produce a characteristic acoustic signature, and microphones offer a low-cost way to detect them. High accuracies have been reported on public drone audio benchmarks, often with random clip-level splits of datasets built from a few long recordings and pieces of existing sound collections, so pieces of one source can appear in both training and test data. We study the binary task of the public…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 16. AI for eGovernance: Leveraging Language Technologies For Digital Inclusion

- **Authors**: Cynthia Jayne Amol, Lilian Wanzare
- **Date / sources**: 2026-11-03 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.04820) · [PDF](https://arxiv.org/pdf/2611.04820v1)

The Kenyan government has invested heavily in the digitisation of public service delivery, in line with the Kenya Digital Master Plan 2022-2032. The national eGovernment platform, eCitizen, hosts services that are vital to citizens'livelihoods, including business registration, youth enterprise lending, digital literacy and tax filing. However, the platform faces digital inclusion challenges that limit equitable…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 17. Transformer-Based Automatic Speech Recognition Development for Transcription and Clinical Information Extraction in Indonesian on Electronic Health Records

- **Authors**: Bachtiyar Wahab, F. Harahap, Khairul Anwar, Nabila Mahyuda, Nur Asiah Hasibuan
- **Date / sources**: 2026-11-02 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition
- **Links**: [Paper](https://www.semanticscholar.org/paper/607975e9d07e2377b8627befe9a0af22f4eeedd6) · [PDF](https://doi.org/10.52088/ijesty.v6i4.1938)

Integrating Automatic Speech Recognition (ASR) into Electronic Health Records (EHR) has the potential to boost the efficiency of clinical documentation by automating the transcription of doctor-patient conversations. However, high-quality transcription doesn't necessarily mean the clinical information will be classified accurately. This study aims to analyze the quality of ASR transcriptions and compare the…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 18. Performance evaluation of deep learning models for Indian-accented English automatic speech recognition

- **Authors**: R. Mallikharjun, Bittu Kumar
- **Date / sources**: 2026-11-02 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition
- **Links**: [Paper](https://www.semanticscholar.org/paper/e04503f82e7fe59842e08c9a64db97048edacdd6)

No abstract

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 19. Fuse To Align: Multimodal Representation Learning for Retrieval via Hypergraph Regularization

- **Authors**: Anindya Nag, Ambuj Mehrish, Sebastiano Vascon
- **Date / sources**: 2026-11-02 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Audio Understanding & Reasoning: audio-text; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.03370) · [PDF](https://arxiv.org/pdf/2611.03370v1)

Multimodal retrieval must integrate complementary evidence from views that may be missing, noisy, or unequally informative. When a sample provides limited reliable evidence, learning from its views alone can hinder the acquisition of useful retrieval representations. Semantically related training samples may provide complementary observations, yet existing volume-based objectives jointly align modalities within each…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 20. CrowdForge: Effects of Audio and Visual Audience Participation Modalities on Agency, Collaboration, and Engagement in AI-Mediated MR Performances

- **Authors**: Torin Hopkins, Shih-Yu Ma, Zander Trafton-Hancock, Ellen Yi-Luen Do, Luca Turchet
- **Date / sources**: 2026-11-02 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Generative Music & Audio: audio generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.03389) · [PDF](https://arxiv.org/pdf/2611.03389v1)

Technology-mediated audience participation (TMAP) enables audiences to influence live performances, yet balancing interaction with meaningful agency remains challenging. While AI-generated music and MR enable new forms of audio and visual audience participation, little is known about how these participation modalities influence audience experiences during live musical performance. In particular, it remains unclear…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 21. Be My Ears: Enabling Semantic Alerting for Earphone Wearers with Pheme

- **Authors**: Zhi-Wei Ren, Yong-Jie Yang, Long-Fei Shangguan
- **Date / sources**: 2026-11-01 · semantic_scholar
- **Relevance**: 6 pts · Audio & Speech Language Models: audio language model
- **Links**: [Paper](https://www.semanticscholar.org/paper/105c2cd974adfca639a9e5edee251ba8bf7b68c6) · [PDF](https://doi.org/10.1145/3830398.3830640)

Active Noise Cancellation (ANC) earphones provide immersive listening experiences but induce auditory isolation to earphone users, leaving them vulnerable to hazards and socially disconnected. We present Pheme, an agentic framework that transforms ANC earphones into context-aware auditory assistants. Informed by two user studies (N = 385 and N = 34) that reveal a high prevalence of missed critical sounds and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 22. Reflex: Fast Robot Policy Serving by Reusing and Correcting Past Actions

- **Authors**: Ziyang Lin, Zixuan Sun, Rami Nasser, Jianli Jin, Xuanle Li, Jayanth Srinivasa, Fan Lai
- **Date / sources**: 2026-10-31 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Generative Music & Audio: audio generation; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.00524) · [PDF](https://arxiv.org/pdf/2611.00524v1)

Modern robot policies often perform expensive inference to generate action chunks, making serving a latency bottleneck for real-time control and a throughput bottleneck for multi-robot serving. Building on the success of caching in image, video, and audio generation, recent robot-policy advances have reported promising speedups by reusing intermediate denoising states to avoid redundant computation. Surprisingly, we…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
