# Music / Audio Foundation Model Research Radar — 2026-11-24

> Lookback window: 2026-11-17 to 2026-11-24 · New papers: 9 · New models: 30 · relevant papers/models in window: 24/62 · raw papers/models: 83/350

Sources: arxiv=43 · semantic_scholar=40 · huggingface_models=350

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [snkii/Sori-10B-Speech](https://huggingface.co/snkii/Sori-10B-Speech) | 2026-11-23 | audio-text-to-text | 43 | 1 | 142 | 1 | cc-by-nc-sa-4.0 |
| 2 | [jjcoders/suna-v1](https://huggingface.co/jjcoders/suna-v1) | 2026-11-23 | text-to-audio | 42 | 1 | 2392 | 2 | mit |
| 3 | [adventists-ai/Sophon-Realtime-4B-Flash](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Flash) | 2026-11-23 | audio-to-audio | 34 | 1 | 846 | 21 | apache-2.0 |
| 4 | [adventists-ai/Sophon-Realtime-32B-Tag](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag) | 2026-11-23 | audio-to-audio | 34 | 1 | 1226 | 16 | apache-2.0 |
| 5 | [adventists-ai/Sophon-Realtime-32B-Flash](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash) | 2026-11-23 | audio-to-audio | 34 | 2 | 1156 | 14 | apache-2.0 |
| 6 | [adventists-ai/Sophon-Realtime-32B-E2E](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-E2E) | 2026-11-23 | audio-to-audio | 33 | 1 | 387 | 7 | apache-2.0 |
| 7 | [adventists-ai/Sophon-Realtime-32B-Flash-4bit-MLX](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Flash-4bit-MLX) | 2026-11-23 | audio-to-audio | 33 | 2 | 445 | 2 | apache-2.0 |
| 8 | [adventists-ai/Sophon-Realtime-4B-E2E](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-E2E) | 2026-11-23 | audio-to-audio | 33 | 1 | 77 | 2 | apache-2.0 |
| 9 | [adventists-ai/Sophon-Realtime-4B-Flash-MLX](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Flash-MLX) | 2026-11-23 | audio-to-audio | 33 | 1 | 207 | 0 | apache-2.0 |
| 10 | [adventists-ai/Sophon-Realtime-4B-Tag-W4](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Tag-W4) | 2026-11-23 | audio-to-audio | 33 | 1 | 166 | 0 | apache-2.0 |
| 11 | [adventists-ai/Sophon-Realtime-4B-Tag](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Tag) | 2026-11-23 | audio-to-audio | 33 | 1 | 117 | 0 | apache-2.0 |
| 12 | [adventists-ai/Sophon-Realtime-v1](https://huggingface.co/adventists-ai/Sophon-Realtime-v1) | 2026-11-24 | audio-to-audio | 30 | 1 | 0 | 259 | apache-2.0 |
| 13 | [Evan-Lin/Crossfeed-Unison](https://huggingface.co/Evan-Lin/Crossfeed-Unison) | 2026-11-24 | text-to-speech | 27 | 1 | 0 | 0 | other |
| 14 | [StudioYebisu-ship-it/Drama-3-Japanese-speech-cpp-gguf](https://huggingface.co/StudioYebisu-ship-it/Drama-3-Japanese-speech-cpp-gguf) | 2026-11-24 | text-to-speech | 25 | 1 | 0 | 9 | other |
| 15 | [zhaoyx39/S3-S2ST-4B-Offline](https://huggingface.co/zhaoyx39/S3-S2ST-4B-Offline) | 2026-11-23 | audio-to-audio | 22 | 1 | 8 | 1 | unknown |
| 16 | [zhaoyx39/S3-S2ST-4B-Streaming](https://huggingface.co/zhaoyx39/S3-S2ST-4B-Streaming) | 2026-11-23 | audio-to-audio | 22 | 1 | 6 | 1 | unknown |
| 17 | [empiriolabsai/canora-dutch](https://huggingface.co/empiriolabsai/canora-dutch) | 2026-11-23 | text-to-speech | 19 | 9 | 349 | 1 | apache-2.0 |
| 18 | [Serkali-sudo/Pocket-TTS-LiteRT-FP16](https://huggingface.co/Serkali-sudo/Pocket-TTS-LiteRT-FP16) | 2026-11-23 | text-to-speech | 18 | 1 | 772 | 0 | unknown |
| 19 | [batteryphil/VAULT-PRIMAL-VITS-29M](https://huggingface.co/batteryphil/VAULT-PRIMAL-VITS-29M) | 2026-11-23 | text-to-speech | 17 | 1 | 19 | 0 | cc-by-nc-4.0 |
| 20 | [blaze-voice-ai/vienue-v3-turbo-enhanced](https://huggingface.co/blaze-voice-ai/vienue-v3-turbo-enhanced) | 2026-11-23 | text-to-speech | 16 | 1 | 127 | 13 | apache-2.0 |
| 21 | [Mikhailo/mova-tts](https://huggingface.co/Mikhailo/mova-tts) | 2026-11-23 | text-to-speech | 15 | 1 | 253 | 0 | apache-2.0 |
| 22 | [Lysandra999/Senik-Voice-Expressive-0.5B](https://huggingface.co/Lysandra999/Senik-Voice-Expressive-0.5B) | 2026-11-23 | text-to-speech | 15 | 1 | 28 | 0 | mit |
| 23 | [batteryphil/VAULT-PRIMAL-F5-TTS-337M](https://huggingface.co/batteryphil/VAULT-PRIMAL-F5-TTS-337M) | 2026-11-23 | text-to-speech | 15 | 1 | 21 | 0 | cc-by-nc-4.0 |
| 24 | [NikitHamal/sakhiya-pro-v1](https://huggingface.co/NikitHamal/sakhiya-pro-v1) | 2026-11-23 | text-to-speech | 15 | 1 | 0 | 0 | other |
| 25 | [Lucasgitguy-co/LvW-Ming-TTS-0.5B-MLX-4bit](https://huggingface.co/Lucasgitguy-co/LvW-Ming-TTS-0.5B-MLX-4bit) | 2026-11-23 | text-to-speech | 15 | 3 | 0 | 0 | mit |
| 26 | [Lucasgitguy-co/LvW-Ming-TTS-0.5B](https://huggingface.co/Lucasgitguy-co/LvW-Ming-TTS-0.5B) | 2026-11-23 | text-to-speech | 15 | 1 | 0 | 0 | mit |
| 27 | [Maximilian228/Geode-ACE-Step-1.5](https://huggingface.co/Maximilian228/Geode-ACE-Step-1.5) | 2026-11-23 | text-to-audio | 14 | 1 | 0 | 0 | mit |
| 28 | [MoshinAli/auralguard-checkpoints](https://huggingface.co/MoshinAli/auralguard-checkpoints) | 2026-11-23 | audio-classification | 13 | 1 | 0 | 0 | mit |
| 29 | [groxaxo/Haru-4B-MLX-oQ5-Selective](https://huggingface.co/groxaxo/Haru-4B-MLX-oQ5-Selective) | 2026-11-23 | audio-to-audio | 13 | 1 | 0 | 0 | apache-2.0 |
| 30 | [KaleComputer/kale-tts-1-nano](https://huggingface.co/KaleComputer/kale-tts-1-nano) | 2026-11-23 | text-to-speech | 12 | 2 | 579 | 25 | apache-2.0 |

### Model cards

#### M1. snkii/Sori-10B-Speech

- **Created / updated**: 2026-11-20 / 2026-11-23
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 43 pts · Audio & Speech Language Models: audio language model, audio-language model, speech llm; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=142 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.5-9B, Qwen/Qwen3-Omni-30B-A3B-Instruct
- **Variants in family**: —

#### M2. jjcoders/suna-v1

- **Created / updated**: 2026-10-11 / 2026-11-23
- **Task / library**: text-to-audio / diffusers
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license mit
- **Adoption signals**: downloads=2392 · likes=2 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M3. adventists-ai/Sophon-Realtime-4B-Flash

- **Created / updated**: 2026-11-16 / 2026-11-23
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 34 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0; community likes 21
- **Adoption signals**: downloads=846 · likes=21 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M4. adventists-ai/Sophon-Realtime-32B-Tag

- **Created / updated**: 2026-10-29 / 2026-11-23
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 34 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0; community likes 16
- **Adoption signals**: downloads=1226 · likes=16 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M5. adventists-ai/Sophon-Realtime-32B-Flash

- **Created / updated**: 2026-11-07 / 2026-11-23
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 34 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0; community likes 14
- **Adoption signals**: downloads=1156 · likes=14 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: adventists-ai/Sophon-Realtime-32B-Flash-BF16

#### M6. adventists-ai/Sophon-Realtime-32B-E2E

- **Created / updated**: 2026-11-08 / 2026-11-23
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=387 · likes=7 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M7. adventists-ai/Sophon-Realtime-32B-Flash-4bit-MLX

- **Created / updated**: 2026-11-12 / 2026-11-23
- **Task / library**: audio-to-audio / mlx
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=445 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / adventists-ai/Sophon-Realtime-32B-Flash
- **Variants in family**: adventists-ai/Sophon-Realtime-32B-Flash-4bit

#### M8. adventists-ai/Sophon-Realtime-4B-E2E

- **Created / updated**: 2026-11-16 / 2026-11-23
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=77 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M9. adventists-ai/Sophon-Realtime-4B-Flash-MLX

- **Created / updated**: 2026-11-18 / 2026-11-23
- **Task / library**: audio-to-audio / mlx
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=207 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / adventists-ai/Sophon-Realtime-4B-Flash
- **Variants in family**: —

#### M10. adventists-ai/Sophon-Realtime-4B-Tag-W4

- **Created / updated**: 2026-11-18 / 2026-11-23
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=166 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / adventists-ai/Sophon-Realtime-4B-Tag
- **Variants in family**: —

#### M11. adventists-ai/Sophon-Realtime-4B-Tag

- **Created / updated**: 2026-11-16 / 2026-11-23
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 33 pts · Speech Generation, Recognition & Dialogue: voice cloning, speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=117 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M12. adventists-ai/Sophon-Realtime-v1

- **Created / updated**: 2026-11-07 / 2026-11-24
- **Task / library**: audio-to-audio / vllm
- **Relevance**: 30 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; model card links an arXiv paper; declares license apache-2.0; community likes 259
- **Adoption signals**: downloads=0 · likes=259 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2609.21967](https://arxiv.org/abs/2609.21967)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M13. Evan-Lin/Crossfeed-Unison

- **Created / updated**: 2026-11-24 / 2026-11-24
- **Task / library**: text-to-speech / unknown
- **Relevance**: 27 pts · Generative Music & Audio: text-to-audio; Audio Understanding & Reasoning: audio-text; model card links an arXiv paper; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag)
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2605.31530](https://arxiv.org/abs/2605.31530) · [arXiv:2503.20215](https://arxiv.org/abs/2503.20215)
- **Datasets / base models**: unknown / Qwen/Qwen2.5-Omni-7B, jac22/UNISON
- **Variants in family**: —

#### M14. StudioYebisu-ship-it/Drama-3-Japanese-speech-cpp-gguf

- **Created / updated**: 2026-11-23 / 2026-11-24
- **Task / library**: text-to-speech / speech.cpp
- **Relevance**: 25 pts · Speech Generation, Recognition & Dialogue: speech generation, text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=0 · likes=9 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / Aratako/Drama-3-Japanese
- **Variants in family**: —

#### M15. zhaoyx39/S3-S2ST-4B-Offline

- **Created / updated**: 2026-11-23 / 2026-11-23
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 22 pts · Speech Generation, Recognition & Dialogue: speech translation, speech-to-speech; model card links an arXiv paper
- **Adoption signals**: downloads=8 · likes=1 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: [arXiv:2610.36777](https://arxiv.org/abs/2610.36777)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M16. zhaoyx39/S3-S2ST-4B-Streaming

- **Created / updated**: 2026-11-23 / 2026-11-23
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 22 pts · Speech Generation, Recognition & Dialogue: speech translation, speech-to-speech; model card links an arXiv paper
- **Adoption signals**: downloads=6 · likes=1 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: [arXiv:2610.36777](https://arxiv.org/abs/2610.36777)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M17. empiriolabsai/canora-dutch

- **Created / updated**: 2026-11-20 / 2026-11-23
- **Task / library**: text-to-speech / kokoro
- **Relevance**: 19 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=349 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / hexgrad/Kokoro-82M
- **Variants in family**: empiriolabsai/canora-turkish, empiriolabsai/canora-korean, empiriolabsai/canora-polish, empiriolabsai/canora-german, empiriolabsai/canora-norwegian, empiriolabsai/canora-russian, empiriolabsai/canora-french, empiriolabsai/canora-spanish

#### M18. Serkali-sudo/Pocket-TTS-LiteRT-FP16

- **Created / updated**: 2026-11-19 / 2026-11-23
- **Task / library**: text-to-speech / pocket-tts
- **Relevance**: 18 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning
- **Adoption signals**: downloads=772 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M19. batteryphil/VAULT-PRIMAL-VITS-29M

- **Created / updated**: 2026-11-22 / 2026-11-23
- **Task / library**: text-to-speech / transformers
- **Relevance**: 17 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=19 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / facebook/mms-tts-eng
- **Variants in family**: —

#### M20. blaze-voice-ai/vienue-v3-turbo-enhanced

- **Created / updated**: 2026-10-16 / 2026-11-23
- **Task / library**: text-to-speech / unknown
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0; community likes 13
- **Adoption signals**: downloads=127 · likes=13 · trending=0.0
- **License / access**: apache-2.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / pnnbao-ump/VieNeu-TTS-v3-Turbo
- **Variants in family**: —

#### M21. Mikhailo/mova-tts

- **Created / updated**: 2026-11-21 / 2026-11-23
- **Task / library**: text-to-speech / mova-tts
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=253 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / neuphonic/neutts-air
- **Variants in family**: —

#### M22. Lysandra999/Senik-Voice-Expressive-0.5B

- **Created / updated**: 2026-11-22 / 2026-11-23
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license mit
- **Adoption signals**: downloads=28 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M23. batteryphil/VAULT-PRIMAL-F5-TTS-337M

- **Created / updated**: 2026-11-22 / 2026-11-23
- **Task / library**: text-to-speech / safetensors
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=21 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / SWivid/F5-TTS
- **Variants in family**: —

#### M24. NikitHamal/sakhiya-pro-v1

- **Created / updated**: 2026-11-23 / 2026-11-23
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / k2-fsa/OmniVoice
- **Variants in family**: —

#### M25. Lucasgitguy-co/LvW-Ming-TTS-0.5B-MLX-4bit

- **Created / updated**: 2026-11-23 / 2026-11-23
- **Task / library**: text-to-speech / mlx-audio
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / Lucasgitguy-co/LvW-Ming-TTS-0.5B
- **Variants in family**: Lucasgitguy-co/LvW-Ming-TTS-0.5B-MLX-8bit, Lucasgitguy-co/LvW-Ming-TTS-0.5B-MLX-bf16

#### M26. Lucasgitguy-co/LvW-Ming-TTS-0.5B

- **Created / updated**: 2026-11-23 / 2026-11-23
- **Task / library**: text-to-speech / transformers
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / inclusionAI/Ming-3.0-tts-0.5B
- **Variants in family**: —

#### M27. Maximilian228/Geode-ACE-Step-1.5

- **Created / updated**: 2026-11-21 / 2026-11-23
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / ACE-Step/Ace-Step1.5, ACE-Step/acestep-v15-sft, ACE-Step/acestep-5Hz-lm-1.7B, Qwen/Qwen3-Embedding-0.6B
- **Variants in family**: —

#### M28. MoshinAli/auralguard-checkpoints

- **Created / updated**: 2026-09-04 / 2026-11-23
- **Task / library**: audio-classification / pytorch
- **Relevance**: 13 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: asvspoof2019, in-the-wild, wavefake / unknown
- **Variants in family**: —

#### M29. groxaxo/Haru-4B-MLX-oQ5-Selective

- **Created / updated**: 2026-11-23 / 2026-11-23
- **Task / library**: audio-to-audio / mlx
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / higurashi-ai/Haru-4B
- **Variants in family**: —

#### M30. KaleComputer/kale-tts-1-nano

- **Created / updated**: 2026-11-16 / 2026-11-23
- **Task / library**: text-to-speech / onnx
- **Relevance**: 12 pts · Speech Generation, Recognition & Dialogue: text-to-speech; declares license apache-2.0; community likes 19
- **Adoption signals**: downloads=579 · likes=25 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: KaleComputer/kale-tts-1-data / KaleComputer/kale-tts-1-base
- **Variants in family**: KaleComputer/kale-tts-1-tiny

## Research signals

- Speech Generation, Recognition & Dialogue: 8 papers
- Audio & Speech Language Models: 3 papers
- Evaluation, Alignment, Safety & Copyright: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [Neural Defend Ranks #1 in Global Audio Deepfake Detection Benchmark - ARCAS on the Podonos Independent Leaderboard](https://arxiv.org/abs/2611.27215) | 2026-11-20 | 18 | Speech Generation, Recognition & Dialogue, Evaluation, Alignment, Safety & Copyright | — |
| 2 | [Windchime: an Audiovisual Installation with Audio-Language Model implementations](https://arxiv.org/abs/2611.26759) | 2026-11-19 | 18 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 3 | [SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech](https://arxiv.org/abs/2611.27810) | 2026-11-20 | 13 | Audio & Speech Language Models | — |
| 4 | [Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection](https://arxiv.org/abs/2611.27784) | 2026-11-20 | 12 | Speech Generation, Recognition & Dialogue | — |
| 5 | [Granary-v2: Scalable Multilingual Speech Data Curation for Predictable and Controllable Model Outputs](https://arxiv.org/abs/2611.28248) | 2026-11-20 | 11 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 6 | [Preserving Prosody in Speaker Anonymization](https://arxiv.org/abs/2611.28290) | 2026-11-20 | 9 | Speech Generation, Recognition & Dialogue | — |
| 7 | [PromptTTSD: Controllable Text to Spoken Dialogue Synthesis with Open-Ended Text Descriptions](https://arxiv.org/abs/2611.27601) | 2026-11-20 | 7 | Speech Generation, Recognition & Dialogue | — |
| 8 | [EAF-TTS: Rethinking Codec-Latent Coordinates for Flow TTS](https://arxiv.org/abs/2611.27214) | 2026-11-20 | 6 | Speech Generation, Recognition & Dialogue | — |
| 9 | [A Nepali-Accented English Evaluation Dataset for Automatic Speech Recognition](https://arxiv.org/abs/2611.28263) | 2026-11-20 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. Neural Defend Ranks #1 in Global Audio Deepfake Detection Benchmark - ARCAS on the Podonos Independent Leaderboard

- **Authors**: Sivashankar Selvarajan, Piyush Verma, Sumit Singh
- **Date / sources**: 2026-11-20 · arxiv, semantic_scholar
- **Relevance**: 18 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.27215) · [PDF](https://arxiv.org/pdf/2611.27215v1)

Commercial detectors of AI-generated audio are usually promoted with results on internal test sets that buyers cannot inspect. Independent benchmarks with private labels give a more reliable comparison. We report the results of Neural Defend's ARCAS foundation models on the Podonos audio deepfake detection benchmark, an independent leaderboard that scores commercial detection APIs and open-source detectors on one…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. Windchime: an Audiovisual Installation with Audio-Language Model implementations

- **Authors**: Trent Eriksen, Celeste Betancur Gutierrez
- **Date / sources**: 2026-11-19 · arxiv, semantic_scholar
- **Relevance**: 18 pts · Audio & Speech Language Models: audio-language model; Speech Generation, Recognition & Dialogue: automatic speech recognition; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.26759) · [PDF](https://arxiv.org/pdf/2611.26759v1)

Windchime is an audiovisual installation in which spoken language retrieves music and interactive animations from an artist authored corpus. A local Automatic Speech Recognition (ASR) model transcribes each prompt while an audio-language model (ALM) embeds it and retrieval over 406 audio stems returns a soundscape with live coded Strudel fragments that layer into audio output. Simultaneously each spoken input…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech

- **Authors**: Côme Hosxe, Rachid Riad, Quentin Spinat
- **Date / sources**: 2026-11-20 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Audio & Speech Language Models: audio language model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.27810) · [PDF](https://arxiv.org/pdf/2611.27810v1)

Audio language models (ALMs) can answer clinical questions from speech, outperforming baselines built on handcrafted acoustic features. Reasoning ALMs generate a chain of thought that refers to properties of the speaker's voice before predicting. Each statement the model makes about the voice needs to be checked against clinicians' perceptual ratings of the same recording. On clinical speech, existing evaluations…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection

- **Authors**: Sivashankar Selvarajan, Piyush Verma, Sumit Kumar, Sharayu N. Deshmukh
- **Date / sources**: 2026-11-20 · arxiv, semantic_scholar
- **Relevance**: 12 pts · Speech Generation, Recognition & Dialogue: text-to-speech, voice cloning; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.27784) · [PDF](https://arxiv.org/pdf/2611.27784v1)

Voice cloning now needs only seconds of audio, and detectors tuned to one dataset often fail when the generator, channel, or language changes. We introduce ARCAS 290M, Neural Defend's foundation model for detecting AI-generated audio. A single frozen production model, with no benchmark-specific fine-tuning, generalizes across text-to-speech, voice-conversion, and codec-language-model generators, telephone and…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Granary-v2: Scalable Multilingual Speech Data Curation for Predictable and Controllable Model Outputs

- **Authors**: Nithin Rao Koluguri, Meline Mkrtchyan, Nune Tadevosyan, Aaftab V, Sushmitha Deva, Fan Qian, Davit Karamyan, Kunal Dhawan et al.
- **Date / sources**: 2026-11-20 · arxiv
- **Relevance**: 11 pts · Audio & Speech Language Models: speech-language model; Speech Generation, Recognition & Dialogue: speech translation
- **Links**: [Paper](https://arxiv.org/abs/2611.28248) · [PDF](https://arxiv.org/pdf/2611.28248v1)

Speech-language models that follow instructions need training data that connects the same recording to different output forms and tasks. We present Granary-v2, a multilingual speech dataset and reusable curation system that provides a data foundation for these models. Granary-v2 extends Granary-v1 with aligned transcript variants and instruction-target pairs for multi-task speech-language training. Language coverage…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. Preserving Prosody in Speaker Anonymization

- **Authors**: Kevin Everson, Mari Ostendorf
- **Date / sources**: 2026-11-20 · arxiv
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: speech generation, speech synthesis
- **Links**: [Paper](https://arxiv.org/abs/2611.28290) · [PDF](https://arxiv.org/pdf/2611.28290v1)

Effective prosody modeling is essential in natural speech generation applications, but complications arise in speaker anonymization, since speaker attributes are present in acoustic correlates of prosody. Our work aims to improve previous reported tradeoffs between effective speaker obfuscation and preservation of prosodic content. To this end, we integrate an existing pretrained privacy-preserving prosody encoder…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. PromptTTSD: Controllable Text to Spoken Dialogue Synthesis with Open-Ended Text Descriptions

- **Authors**: Sulong Yang, Zhi Zeng, Xiupeng Wu, Juewen Hu, Pring Wong, Shuwu Zhang, Shuo Chen
- **Date / sources**: 2026-11-20 · arxiv, semantic_scholar
- **Relevance**: 7 pts · Speech Generation, Recognition & Dialogue: voice cloning; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.27601) · [PDF](https://arxiv.org/pdf/2611.27601v1)

Spoken dialogue synthesis aims to generate multi-turn conversational speech from dialogue scripts while maintaining speaker consistency and contextual appropriateness. However, existing models largely lack fine-grained controllability, which is critical for capturing the dynamic, context-dependent style shifts in natural conversations. While prompt-based TTS has enabled such control for single-speaker speech,…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. EAF-TTS: Rethinking Codec-Latent Coordinates for Flow TTS

- **Authors**: Yumiao Li, Haoxiang Jie, Xinbei Li, Yaoyuan Yan, Yue Qu
- **Date / sources**: 2026-11-20 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.27214) · [PDF](https://arxiv.org/pdf/2611.27214v1)

Latent text-to-speech (TTS) systems generate codec latents decoded by a frozen decoder, but good reconstruction does not ensure geometry suitable for Flow generation from isotropic Gaussian noise. We present Embedded Acoustic Flow TTS (EAF-TTS), an acoustic-latent adaptation of ELF with phone- and duration-conditioned generation, shared-network terminal correction, and frozen WaveVAE decoding. EAF-TTS supports a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. A Nepali-Accented English Evaluation Dataset for Automatic Speech Recognition

- **Authors**: Santosh Dahal, Kiran Chandra Dahal
- **Date / sources**: 2026-11-20 · arxiv
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition
- **Links**: [Paper](https://arxiv.org/abs/2611.28263) · [PDF](https://arxiv.org/pdf/2611.28263v1)

Automatic speech recognition (ASR) systems perform strongly on native-English benchmarks, yet their accuracy degrades sharply when the input speech comes from under represented non-native accents. Nepali-accented English is particularly under-served: existing resources either focus on native Nepali speech, cover broader multi-accent settings without dedicated Nepali evaluation, or provide only limited Nepali-accent…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
