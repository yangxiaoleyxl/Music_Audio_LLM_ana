# Music / Audio Foundation Model Research Radar — 2026-11-22

> Lookback window: 2026-11-15 to 2026-11-22 · New papers: 1 · New models: 15 · relevant papers/models in window: 31/53 · raw papers/models: 114/354

Sources: arxiv=57 · semantic_scholar=57 · huggingface_models=354

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [moonbox-dev/YuE2-3B-MLX](https://huggingface.co/moonbox-dev/YuE2-3B-MLX) | 2026-11-22 | text-to-audio | 44 | 3 | 0 | 0 | cc-by-nc-4.0 |
| 2 | [snkii/Sori-10B-Speech](https://huggingface.co/snkii/Sori-10B-Speech) | 2026-11-22 | audio-text-to-text | 43 | 1 | 102 | 1 | cc-by-nc-sa-4.0 |
| 3 | [jjcoders/suna-v1](https://huggingface.co/jjcoders/suna-v1) | 2026-11-22 | text-to-audio | 42 | 1 | 2299 | 2 | mit |
| 4 | [empiriolabsai/canora-turkish](https://huggingface.co/empiriolabsai/canora-turkish) | 2026-11-22 | text-to-speech | 19 | 6 | 204 | 0 | apache-2.0 |
| 5 | [batteryphil/VAULT-PRIMAL-F5-TTS-337M](https://huggingface.co/batteryphil/VAULT-PRIMAL-F5-TTS-337M) | 2026-11-22 | text-to-speech | 18 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 6 | [batteryphil/VAULT-PRIMAL-VITS-29M](https://huggingface.co/batteryphil/VAULT-PRIMAL-VITS-29M) | 2026-11-22 | text-to-speech | 17 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 7 | [itzune/antzoki-mini-tts-GGUF](https://huggingface.co/itzune/antzoki-mini-tts-GGUF) | 2026-11-22 | text-to-speech | 15 | 1 | 0 | 0 | apache-2.0 |
| 8 | [itzune/antzoki-mini-tts](https://huggingface.co/itzune/antzoki-mini-tts) | 2026-11-22 | text-to-speech | 15 | 1 | 0 | 0 | apache-2.0 |
| 9 | [loom-ai-org/musicgen-small-loom](https://huggingface.co/loom-ai-org/musicgen-small-loom) | 2026-11-22 | text-to-audio | 14 | 1 | 34 | 0 | cc-by-nc-4.0 |
| 10 | [nervous-sloth/rickroller](https://huggingface.co/nervous-sloth/rickroller) | 2026-11-22 | text-to-audio | 14 | 1 | 0 | 0 | cc0-1.0 |
| 11 | [Shadow0482/personaplex-7b-v1-q8](https://huggingface.co/Shadow0482/personaplex-7b-v1-q8) | 2026-11-22 | audio-to-audio | 13 | 2 | 0 | 1 | other |
| 12 | [MoshinAli/auralguard-checkpoints](https://huggingface.co/MoshinAli/auralguard-checkpoints) | 2026-11-22 | audio-classification | 13 | 1 | 0 | 0 | mit |
| 13 | [cdismus4/chimera-jev-full-duplex](https://huggingface.co/cdismus4/chimera-jev-full-duplex) | 2026-11-22 | audio-to-audio | 13 | 1 | 0 | 0 | other |
| 14 | [oluwagbotty/afri-seamless-ft-p8-multi](https://huggingface.co/oluwagbotty/afri-seamless-ft-p8-multi) | 2026-11-22 | automatic-speech-recognition | 10 | 2 | 0 | 0 | cc-by-nc-4.0 |
| 15 | [huybik/hibiki-zero-vi-full-sft](https://huggingface.co/huybik/hibiki-zero-vi-full-sft) | 2026-11-22 | audio-to-audio | 9 | 1 | 0 | 1 | cc-by-nc-sa-4.0 |

### Model cards

#### M1. moonbox-dev/YuE2-3B-MLX

- **Created / updated**: 2026-11-20 / 2026-11-22
- **Task / library**: text-to-audio / mlx
- **Relevance**: 44 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2503.08638](https://arxiv.org/abs/2503.08638) · [arXiv:2609.33757](https://arxiv.org/abs/2609.33757) · [arXiv:2610.05336](https://arxiv.org/abs/2610.05336)
- **Datasets / base models**: unknown / m-a-p/YuE2-3B
- **Variants in family**: moonbox-dev/YuE2-3B-ONNX, moonbox-dev/YuE2-3B-GGUF

#### M2. snkii/Sori-10B-Speech

- **Created / updated**: 2026-11-20 / 2026-11-22
- **Task / library**: audio-text-to-text / transformers
- **Relevance**: 43 pts · Audio & Speech Language Models: audio language model, audio-language model, speech llm; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=102 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.5-9B, Qwen/Qwen3-Omni-30B-A3B-Instruct
- **Variants in family**: —

#### M3. jjcoders/suna-v1

- **Created / updated**: 2026-10-11 / 2026-11-22
- **Task / library**: text-to-audio / diffusers
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license mit
- **Adoption signals**: downloads=2299 · likes=2 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M4. empiriolabsai/canora-turkish

- **Created / updated**: 2026-11-20 / 2026-11-22
- **Task / library**: text-to-speech / kokoro
- **Relevance**: 19 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=204 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / hexgrad/Kokoro-82M
- **Variants in family**: empiriolabsai/canora-dutch, empiriolabsai/canora-polish, empiriolabsai/canora-korean, empiriolabsai/canora-german, empiriolabsai/canora-norwegian

#### M5. batteryphil/VAULT-PRIMAL-F5-TTS-337M

- **Created / updated**: 2026-11-22 / 2026-11-22
- **Task / library**: text-to-speech / safetensors
- **Relevance**: 18 pts · Speech Generation, Recognition & Dialogue: text-to-speech, voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / SWivid/F5-TTS
- **Variants in family**: —

#### M6. batteryphil/VAULT-PRIMAL-VITS-29M

- **Created / updated**: 2026-11-22 / 2026-11-22
- **Task / library**: text-to-speech / transformers
- **Relevance**: 17 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / facebook/mms-tts-eng
- **Variants in family**: —

#### M7. itzune/antzoki-mini-tts-GGUF

- **Created / updated**: 2026-11-22 / 2026-11-22
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / itzune/antzoki-mini-tts
- **Variants in family**: —

#### M8. itzune/antzoki-mini-tts

- **Created / updated**: 2026-11-22 / 2026-11-22
- **Task / library**: text-to-speech / transformers
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: openslr/76 / Edge0/Audio8-TTS-Realistic-Air
- **Variants in family**: —

#### M9. loom-ai-org/musicgen-small-loom

- **Created / updated**: 2026-10-10 / 2026-11-22
- **Task / library**: text-to-audio / loom-py-rt
- **Relevance**: 14 pts · Generative Music & Audio: text-to-audio (pipeline tag), musicgen; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=34 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / facebook/musicgen-small
- **Variants in family**: —

#### M10. nervous-sloth/rickroller

- **Created / updated**: 2026-11-22 / 2026-11-22
- **Task / library**: text-to-audio / unknown
- **Relevance**: 14 pts · Generative Music & Audio: music generation, text-to-audio (pipeline tag); declares license cc0-1.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc0-1.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M11. Shadow0482/personaplex-7b-v1-q8

- **Created / updated**: 2026-11-22 / 2026-11-22
- **Task / library**: audio-to-audio / moshi
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license other
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / nvidia/personaplex-7b-v1
- **Variants in family**: Shadow0482/personaplex-7b-v1-q4

#### M12. MoshinAli/auralguard-checkpoints

- **Created / updated**: 2026-09-04 / 2026-11-22
- **Task / library**: audio-classification / unknown
- **Relevance**: 13 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: asvspoof2019, in-the-wild, wavefake / unknown
- **Variants in family**: —

#### M13. cdismus4/chimera-jev-full-duplex

- **Created / updated**: 2026-11-22 / 2026-11-22
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M14. oluwagbotty/afri-seamless-ft-p8-multi

- **Created / updated**: 2026-11-21 / 2026-11-22
- **Task / library**: automatic-speech-recognition / unknown
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / facebook/seamless-m4t-v2-large
- **Variants in family**: oluwagbotty/afri-seamless-ft-p8

#### M15. huybik/hibiki-zero-vi-full-sft

- **Created / updated**: 2026-07-29 / 2026-11-22
- **Task / library**: audio-to-audio / moshi
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: speech translation; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / kyutai/hibiki-zero-3b-pytorch-bf16
- **Variants in family**: —

## Research signals

- Audio & Speech Language Models: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [Video-Based Automated Seizure Classification Using Multimodal Large Language Models.](https://www.semanticscholar.org/paper/732d04f2434a6412a2dec470236e515c1704414b) | 2026-11-20 | 7 | Audio & Speech Language Models | — |

## Paper cards

### 1. Video-Based Automated Seizure Classification Using Multimodal Large Language Models.

- **Authors**: Li-Na Zhang, Richard Jiang, Tonmoy Monsoor, J. Pasqua, Colin M. McCrimmon, Prateik Sinha, Kartik Sharma, Muayad A. Alzuabi et al.
- **Date / sources**: 2026-11-20 · semantic_scholar
- **Relevance**: 7 pts · Audio & Speech Language Models: audio-language model
- **Links**: [Paper](https://www.semanticscholar.org/paper/732d04f2434a6412a2dec470236e515c1704414b) · [PDF](https://doi.org/10.1002/acn3.70574)

OBJECTIVE Accurately distinguishing between epileptic seizures (ES) and nonepileptic seizures (NES) remains a significant clinical challenge, typically requiring resource-intensive inpatient video-EEG monitoring. We developed a multimodal large language model (MLLM)-based framework for automated extraction of semiological features from seizure videos, followed by classification of events as ES or NES. METHODS We…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
