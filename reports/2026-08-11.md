# Music / Audio Foundation Model Research Radar — 2026-08-11

> Lookback window: 2026-08-04 to 2026-08-11 · New papers: 1 · New models: 17 · relevant papers/models in window: 28/36 · raw papers/models: 62/233

Sources: arxiv=0 · semantic_scholar=62 · huggingface_models=233

## Source notes

- arXiv: HTTP Error 500: Internal Server Error

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [bhushan1729/orpheus-3b-stage3-tagged-checkpoint-296](https://huggingface.co/bhushan1729/orpheus-3b-stage3-tagged-checkpoint-296) | 2026-08-11 | text-to-speech | 26 | 1 | 0 | 0 | apache-2.0 |
| 2 | [dots-studio/dots.tts-mf-2steps-stts](https://huggingface.co/dots-studio/dots.tts-mf-2steps-stts) | 2026-08-11 | text-to-speech | 25 | 1 | 0 | 0 | apache-2.0 |
| 3 | [dots-studio/dots.tts-mf-2steps](https://huggingface.co/dots-studio/dots.tts-mf-2steps) | 2026-08-11 | text-to-speech | 25 | 1 | 0 | 0 | apache-2.0 |
| 4 | [dots-studio/dots.tts-soar](https://huggingface.co/dots-studio/dots.tts-soar) | 2026-08-11 | text-to-speech | 24 | 1 | 1515 | 90 | apache-2.0 |
| 5 | [dots-studio/dots.tts-base](https://huggingface.co/dots-studio/dots.tts-base) | 2026-08-11 | text-to-speech | 24 | 1 | 304 | 48 | apache-2.0 |
| 6 | [audio-cpp/audio.cpp-gguf](https://huggingface.co/audio-cpp/audio.cpp-gguf) | 2026-08-11 | text-to-speech | 24 | 1 | 106617 | 46 | other |
| 7 | [dots-studio/dots.tts-mf](https://huggingface.co/dots-studio/dots.tts-mf) | 2026-08-11 | text-to-speech | 24 | 1 | 1557 | 27 | apache-2.0 |
| 8 | [Prince-1/VibeVoice-Realtime-0.5B-Onnx](https://huggingface.co/Prince-1/VibeVoice-Realtime-0.5B-Onnx) | 2026-08-11 | text-to-speech | 24 | 1 | 0 | 0 | mit |
| 9 | [IndexTeam/IndexTTS-2.5](https://huggingface.co/IndexTeam/IndexTTS-2.5) | 2026-08-11 | text-to-speech | 20 | 1 | 0 | 16 | other |
| 10 | [ekacare/parrotlet-a-2.5-pro](https://huggingface.co/ekacare/parrotlet-a-2.5-pro) | 2026-08-11 | automatic-speech-recognition | 18 | 1 | 2 | 0 | other |
| 11 | [dots-studio/dots.tts-mf-1step](https://huggingface.co/dots-studio/dots.tts-mf-1step) | 2026-08-11 | text-to-speech | 17 | 1 | 0 | 0 | apache-2.0 |
| 12 | [vanch007/mlx-indextts2-2.5-fp32](https://huggingface.co/vanch007/mlx-indextts2-2.5-fp32) | 2026-08-11 | text-to-speech | 15 | 3 | 0 | 0 | other |
| 13 | [AetherAllan/bufeiyan-gpt-sovits-v2pro](https://huggingface.co/AetherAllan/bufeiyan-gpt-sovits-v2pro) | 2026-08-11 | text-to-speech | 15 | 1 | 0 | 0 | other |
| 14 | [mimba/bluetts-nnh](https://huggingface.co/mimba/bluetts-nnh) | 2026-08-11 | text-to-speech | 15 | 1 | 0 | 0 | cc-by-nc-sa-4.0 |
| 15 | [Panhapich/Khmer-TTS](https://huggingface.co/Panhapich/Khmer-TTS) | 2026-08-11 | text-to-speech | 15 | 1 | 0 | 0 | cc-by-nc-sa-4.0 |
| 16 | [iNLP-Lab/Myna-Hokkien](https://huggingface.co/iNLP-Lab/Myna-Hokkien) | 2026-08-11 | audio-to-audio | 13 | 1 | 2 | 1 | apache-2.0 |
| 17 | [thangylvp/stcc](https://huggingface.co/thangylvp/stcc) | 2026-08-11 | audio-text-to-text | 9 | 1 | 1 | 0 | apache-2.0 |

### Model cards

#### M1. bhushan1729/orpheus-3b-stage3-tagged-checkpoint-296

- **Created / updated**: 2026-08-06 / 2026-08-11
- **Task / library**: text-to-speech / peft
- **Relevance**: 26 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; Audio & Speech Language Models: audio llm; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unsloth/orpheus-3b-0.1-ft
- **Variants in family**: —

#### M2. dots-studio/dots.tts-mf-2steps-stts

- **Created / updated**: 2026-08-10 / 2026-08-11
- **Task / library**: text-to-speech / dots_tts
- **Relevance**: 25 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2606.07080](https://arxiv.org/abs/2606.07080)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M3. dots-studio/dots.tts-mf-2steps

- **Created / updated**: 2026-08-10 / 2026-08-11
- **Task / library**: text-to-speech / dots_tts
- **Relevance**: 25 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2606.07080](https://arxiv.org/abs/2606.07080)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M4. dots-studio/dots.tts-soar

- **Created / updated**: 2026-06-04 / 2026-08-11
- **Task / library**: text-to-speech / dots_tts
- **Relevance**: 24 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; declares license apache-2.0; community likes 90
- **Adoption signals**: downloads=1515 · likes=90 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / dots-studio/dots.tts-base
- **Variants in family**: —

#### M5. dots-studio/dots.tts-base

- **Created / updated**: 2026-06-03 / 2026-08-11
- **Task / library**: text-to-speech / dots_tts
- **Relevance**: 24 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; declares license apache-2.0; community likes 48
- **Adoption signals**: downloads=304 · likes=48 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M6. audio-cpp/audio.cpp-gguf

- **Created / updated**: 2026-07-14 / 2026-08-11
- **Task / library**: text-to-speech / audio.cpp
- **Relevance**: 24 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), automatic speech recognition; declares license other; community likes 46
- **Adoption signals**: downloads=106617 · likes=46 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5, ACE-Step/acestep-v15-base, Aratako/Irodori-TTS-500M-v3, Aratako/Irodori-TTS-600M-v3-VoiceDesign, Aratako/Irodori-TTS-v4-Small
- **Variants in family**: —

#### M7. dots-studio/dots.tts-mf

- **Created / updated**: 2026-06-04 / 2026-08-11
- **Task / library**: text-to-speech / dots_tts
- **Relevance**: 24 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; declares license apache-2.0; community likes 27
- **Adoption signals**: downloads=1557 · likes=27 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / dots-studio/dots.tts-soar
- **Variants in family**: —

#### M8. Prince-1/VibeVoice-Realtime-0.5B-Onnx

- **Created / updated**: 2026-07-26 / 2026-08-11
- **Task / library**: text-to-speech / onnxruntime
- **Relevance**: 24 pts · Speech Generation, Recognition & Dialogue: speech generation, speech synthesis, text-to-speech (pipeline tag); Generative Music & Audio: audio generation; model card links an arXiv paper; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: [arXiv:2508.19205](https://arxiv.org/abs/2508.19205) · [arXiv:2412.08635](https://arxiv.org/abs/2412.08635)
- **Datasets / base models**: unknown / microsoft/VibeVoice-Realtime-0.5B
- **Variants in family**: —

#### M9. IndexTeam/IndexTTS-2.5

- **Created / updated**: 2026-08-10 / 2026-08-11
- **Task / library**: text-to-speech / indextts
- **Relevance**: 20 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; declares license other; community likes 16
- **Adoption signals**: downloads=0 · likes=16 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M10. ekacare/parrotlet-a-2.5-pro

- **Created / updated**: 2026-08-07 / 2026-08-11
- **Task / library**: automatic-speech-recognition / transformers
- **Relevance**: 18 pts · Audio & Speech Language Models: speech llm; Speech Generation, Recognition & Dialogue: automatic speech recognition; declares license other
- **Adoption signals**: downloads=2 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / openai/whisper-large-v3, google/medgemma-4b-it
- **Variants in family**: —

#### M11. dots-studio/dots.tts-mf-1step

- **Created / updated**: 2026-08-10 / 2026-08-11
- **Task / library**: text-to-speech / dots_tts
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2606.07080](https://arxiv.org/abs/2606.07080)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M12. vanch007/mlx-indextts2-2.5-fp32

- **Created / updated**: 2026-08-11 / 2026-08-11
- **Task / library**: text-to-speech / mlx
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / IndexTeam/IndexTTS-2.5
- **Variants in family**: vanch007/mlx-indextts2-2.5-8bit, vanch007/mlx-indextts2-2.5-fp16

#### M13. AetherAllan/bufeiyan-gpt-sovits-v2pro

- **Created / updated**: 2026-08-09 / 2026-08-11
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M14. mimba/bluetts-nnh

- **Created / updated**: 2026-08-10 / 2026-08-11
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / gated
- **Related papers**: —
- **Datasets / base models**: mimba/multivoice-nnh / notmax123/blue-v2
- **Variants in family**: —

#### M15. Panhapich/Khmer-TTS

- **Created / updated**: 2026-07-25 / 2026-08-11
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / fishaudio/openaudio-s1-mini
- **Variants in family**: —

#### M16. iNLP-Lab/Myna-Hokkien

- **Created / updated**: 2026-07-21 / 2026-08-11
- **Task / library**: audio-to-audio / mynahokkien
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=2 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M17. thangylvp/stcc

- **Created / updated**: 2026-08-07 / 2026-08-11
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=1 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3-ASR-0.6B
- **Variants in family**: —

## Research signals

- Speech Generation, Recognition & Dialogue: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [DialectS2S: End-to-End Speech Dialogue Modeling for Low-Resource Chinese Dialects](https://arxiv.org/abs/2608.08067) | 2026-08-08 | 15 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. DialectS2S: End-to-End Speech Dialogue Modeling for Low-Resource Chinese Dialects

- **Authors**: Yiqiao Shu, Tianyu Peng, Yingzhuo Deng, Wen Yang, Jun Lin, Changming Xie, Xinyu Yu, Jiajun Zhang
- **Date / sources**: 2026-08-08 · semantic_scholar
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: speech generation, speech dialogue
- **Links**: [Paper](https://arxiv.org/abs/2608.08067)

Current end-to-end speech dialogue models are primarily optimized for mainstream languages and remain limited in low-resource dialect scenarios due to the scarcity of dialect speech data. Moreover, during dialect adaptation, the semantic representation space of speech dialogue models continuously evolves, while conventional speech supervision remains unchanged, leading to semantic inconsistency between hidden…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
