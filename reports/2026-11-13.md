# Music / Audio Foundation Model Research Radar — 2026-11-13

> Lookback window: 2026-11-06 to 2026-11-13 · New papers: 10 · New models: 30 · relevant papers/models in window: 65/59 · raw papers/models: 179/319

Sources: arxiv=92 · semantic_scholar=87 · huggingface_models=319

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [moonbox-dev/HeartMuLa-oss-3B-MLX](https://huggingface.co/moonbox-dev/HeartMuLa-oss-3B-MLX) | 2026-11-13 | text-to-audio | 59 | 1 | 0 | 0 | apache-2.0 |
| 2 | [OpenLLM-France/Luciole-8B-Audio-1.0](https://huggingface.co/OpenLLM-France/Luciole-8B-Audio-1.0) | 2026-11-13 | audio-text-to-text | 57 | 1 | 1095 | 9 | apache-2.0 |
| 3 | [OpenLLM-France/Luciole-1B-Audio-1.0](https://huggingface.co/OpenLLM-France/Luciole-1B-Audio-1.0) | 2026-11-13 | audio-text-to-text | 57 | 1 | 252 | 6 | apache-2.0 |
| 4 | [OpenLLM-France/Luciole-23B-Audio-1.0](https://huggingface.co/OpenLLM-France/Luciole-23B-Audio-1.0) | 2026-11-13 | audio-text-to-text | 57 | 1 | 215 | 6 | apache-2.0 |
| 5 | [goldhub/Ruach_Studio_Models_v2](https://huggingface.co/goldhub/Ruach_Studio_Models_v2) | 2026-11-13 | text-to-audio | 44 | 3 | 17088 | 18 | other |
| 6 | [jjcoders/suna-v1](https://huggingface.co/jjcoders/suna-v1) | 2026-11-13 | text-to-audio | 42 | 1 | 2543 | 2 | mit |
| 7 | [arpanpathak/staleynet-checkpoints](https://huggingface.co/arpanpathak/staleynet-checkpoints) | 2026-11-13 | text-to-audio | 42 | 1 | 0 | 2 | cc-by-sa-4.0 |
| 8 | [goldhub/YuE2-3B-Ruach_Studio-IRA-Merge](https://huggingface.co/goldhub/YuE2-3B-Ruach_Studio-IRA-Merge) | 2026-11-13 | text-to-audio | 37 | 1 | 4360 | 5 | cc-by-nc-4.0 |
| 9 | [TuneJury/tunejury](https://huggingface.co/TuneJury/tunejury) | 2026-11-13 | audio-classification | 36 | 1 | 939 | 1 | cc-by-nc-4.0 |
| 10 | [xix3r/voxix-granite-speech-4.1-2b-gguf](https://huggingface.co/xix3r/voxix-granite-speech-4.1-2b-gguf) | 2026-11-13 | automatic-speech-recognition | 31 | 1 | 0 | 0 | apache-2.0 |
| 11 | [higurashi-ai/Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B) | 2026-11-13 | audio-to-audio | 28 | 1 | 165 | 136 | apache-2.0 |
| 12 | [botp/Haru-4B](https://huggingface.co/botp/Haru-4B) | 2026-11-13 | audio-to-audio | 27 | 1 | 0 | 0 | apache-2.0 |
| 13 | [Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini) | 2026-11-13 | text-to-speech | 26 | 1 | 13068 | 277 | apache-2.0 |
| 14 | [Zyphra/ZONOS3-Mini-hf](https://huggingface.co/Zyphra/ZONOS3-Mini-hf) | 2026-11-13 | text-to-speech | 25 | 1 | 118 | 3 | apache-2.0 |
| 15 | [nphearum/PsarAI-Speech-GGUF](https://huggingface.co/nphearum/PsarAI-Speech-GGUF) | 2026-11-13 | text-to-speech | 19 | 1 | 133 | 0 | cc-by-nc-sa-4.0 |
| 16 | [Tree-AI-lab/kouman-tts-bau-waxal-full](https://huggingface.co/Tree-AI-lab/kouman-tts-bau-waxal-full) | 2026-11-13 | text-to-speech | 17 | 1 | 379 | 2 | apache-2.0 |
| 17 | [nphearum/PsarAI-S2S-GGUF](https://huggingface.co/nphearum/PsarAI-S2S-GGUF) | 2026-11-13 | audio-to-audio | 17 | 1 | 297 | 0 | cc-by-nc-4.0 |
| 18 | [Neurobrix/Voxtral-Mini-3B-2507-nbx](https://huggingface.co/Neurobrix/Voxtral-Mini-3B-2507-nbx) | 2026-11-13 | audio-text-to-text | 17 | 1 | 0 | 0 | apache-2.0 |
| 19 | [atraq/OmniVoice](https://huggingface.co/atraq/OmniVoice) | 2026-11-13 | text-to-speech | 16 | 1 | 0 | 0 | unknown |
| 20 | [MuntasirElagami/sudanese-chatterbox](https://huggingface.co/MuntasirElagami/sudanese-chatterbox) | 2026-11-13 | text-to-speech | 15 | 1 | 0 | 0 | mit |
| 21 | [Symmetris-labs/tts-mms](https://huggingface.co/Symmetris-labs/tts-mms) | 2026-11-13 | text-to-speech | 13 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 22 | [DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed42](https://huggingface.co/DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed42) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |
| 23 | [DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed240](https://huggingface.co/DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed240) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |
| 24 | [DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed2](https://huggingface.co/DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed2) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |
| 25 | [DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed2](https://huggingface.co/DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed2) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |
| 26 | [DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed240](https://huggingface.co/DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed240) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |
| 27 | [DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed42](https://huggingface.co/DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed42) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |
| 28 | [DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed42](https://huggingface.co/DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed42) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |
| 29 | [DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed240](https://huggingface.co/DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed240) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |
| 30 | [DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed2](https://huggingface.co/DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed2) | 2026-11-13 | audio-classification | 12 | 1 | 0 | 0 | unknown |

### Model cards

#### M1. moonbox-dev/HeartMuLa-oss-3B-MLX

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: text-to-audio / mlx
- **Relevance**: 59 pts · Generative Music & Audio: text-to-music, text to music, music generation; Music Foundation Models & Representations: music foundation model, music language model; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2601.10547](https://arxiv.org/abs/2601.10547)
- **Datasets / base models**: unknown / HeartMuLa/HeartMuLa-oss-3B
- **Variants in family**: —

#### M2. OpenLLM-France/Luciole-8B-Audio-1.0

- **Created / updated**: 2026-09-18 / 2026-11-13
- **Task / library**: audio-text-to-text / nemo
- **Relevance**: 57 pts · Audio & Speech Language Models: audio language model, audio-language model, audio llm; Speech Generation, Recognition & Dialogue: automatic speech recognition, speech translation; Audio Understanding & Reasoning: audio understanding, audio-text (pipeline tag); Music Foundation Models & Representations: music understanding
- **Adoption signals**: downloads=1095 · likes=9 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2410.12109](https://arxiv.org/abs/2410.12109)
- **Datasets / base models**: OpenLLM-France/Luciole-Audio-Training-Dataset / OpenLLM-France/Luciole-8B-Instruct-1.1, nvidia/parakeet-tdt-0.6b-v3
- **Variants in family**: —

#### M3. OpenLLM-France/Luciole-1B-Audio-1.0

- **Created / updated**: 2026-09-18 / 2026-11-13
- **Task / library**: audio-text-to-text / nemo
- **Relevance**: 57 pts · Audio & Speech Language Models: audio language model, audio-language model, audio llm; Speech Generation, Recognition & Dialogue: automatic speech recognition, speech translation; Audio Understanding & Reasoning: audio understanding, audio-text (pipeline tag); Music Foundation Models & Representations: music understanding
- **Adoption signals**: downloads=252 · likes=6 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2410.12109](https://arxiv.org/abs/2410.12109)
- **Datasets / base models**: OpenLLM-France/Luciole-Audio-Training-Dataset / OpenLLM-France/Luciole-1B-Instruct-1.1, nvidia/parakeet-tdt-0.6b-v3
- **Variants in family**: —

#### M4. OpenLLM-France/Luciole-23B-Audio-1.0

- **Created / updated**: 2026-09-18 / 2026-11-13
- **Task / library**: audio-text-to-text / nemo
- **Relevance**: 57 pts · Audio & Speech Language Models: audio language model, audio-language model, audio llm; Speech Generation, Recognition & Dialogue: automatic speech recognition, speech translation; Audio Understanding & Reasoning: audio understanding, audio-text (pipeline tag); Music Foundation Models & Representations: music understanding
- **Adoption signals**: downloads=215 · likes=6 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2410.12109](https://arxiv.org/abs/2410.12109)
- **Datasets / base models**: OpenLLM-France/Luciole-Audio-Training-Dataset / OpenLLM-France/Luciole-23B-Instruct-1.1, nvidia/parakeet-tdt-0.6b-v3
- **Variants in family**: —

#### M5. goldhub/Ruach_Studio_Models_v2

- **Created / updated**: 2026-10-04 / 2026-11-13
- **Task / library**: text-to-audio / ggml
- **Relevance**: 44 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license other
- **Adoption signals**: downloads=17088 · likes=18 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2503.08638](https://arxiv.org/abs/2503.08638)
- **Datasets / base models**: unknown / m-a-p/YuE2-3B
- **Variants in family**: goldhub/YuE2-RS-Finetunes, goldhub/Ruach_Studio_LoRAs

#### M6. jjcoders/suna-v1

- **Created / updated**: 2026-10-11 / 2026-11-13
- **Task / library**: text-to-audio / diffusers
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license mit
- **Adoption signals**: downloads=2543 · likes=2 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M7. arpanpathak/staleynet-checkpoints

- **Created / updated**: 2026-11-04 / 2026-11-13
- **Task / library**: text-to-audio / unknown
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license cc-by-sa-4.0
- **Adoption signals**: downloads=0 · likes=2 · trending=0.0
- **License / access**: cc-by-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M8. goldhub/YuE2-3B-Ruach_Studio-IRA-Merge

- **Created / updated**: 2026-10-16 / 2026-11-13
- **Task / library**: text-to-audio / unknown
- **Relevance**: 37 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=4360 · likes=5 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / m-a-p/YuE2-3B, Mothersuperior/YuE2-instrumental-cot-full-loras, Mothersuperior/yue2-mothersuperior-realaudio-tokenizer-v4, monsterovich/yue2-steps-from-hell, monsterovich/yue2-industrial-rock-lora
- **Variants in family**: —

#### M9. TuneJury/tunejury

- **Created / updated**: 2026-06-16 / 2026-11-13
- **Task / library**: audio-classification / tunejury
- **Relevance**: 36 pts · Generative Music & Audio: text-to-music, text to music, music generation; model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=939 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2606.17006](https://arxiv.org/abs/2606.17006)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M10. xix3r/voxix-granite-speech-4.1-2b-gguf

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: automatic-speech-recognition / transcribe.cpp
- **Relevance**: 31 pts · Audio & Speech Language Models: audio llm, speech llm; Speech Generation, Recognition & Dialogue: automatic speech recognition, speech translation; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2310.02943](https://arxiv.org/abs/2310.02943) · [arXiv:2505.08699](https://arxiv.org/abs/2505.08699) · [arXiv:2603.11243](https://arxiv.org/abs/2603.11243) · [arXiv:2604.12398](https://arxiv.org/abs/2604.12398) · [arXiv:2604.22817](https://arxiv.org/abs/2604.22817) · [arXiv:2604.11269](https://arxiv.org/abs/2604.11269) · [arXiv:2603.08397](https://arxiv.org/abs/2603.08397)
- **Datasets / base models**: unknown / ibm-granite/granite-speech-4.1-2b
- **Variants in family**: —

#### M11. higurashi-ai/Haru-4B

- **Created / updated**: 2026-11-12 / 2026-11-13
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 28 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0; community likes 136
- **Adoption signals**: downloads=165 · likes=136 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M12. botp/Haru-4B

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M13. Zyphra/ZONOS3-Mini

- **Created / updated**: 2026-11-09 / 2026-11-13
- **Task / library**: text-to-speech / zonos3
- **Relevance**: 26 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license apache-2.0; community likes 277
- **Adoption signals**: downloads=13068 · likes=277 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2611.16525](https://arxiv.org/abs/2611.16525)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M14. Zyphra/ZONOS3-Mini-hf

- **Created / updated**: 2026-11-11 / 2026-11-13
- **Task / library**: text-to-speech / transformers
- **Relevance**: 25 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license apache-2.0
- **Adoption signals**: downloads=118 · likes=3 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2611.16525](https://arxiv.org/abs/2611.16525)
- **Datasets / base models**: unknown / Zyphra/ZONOS3-Mini
- **Variants in family**: —

#### M15. nphearum/PsarAI-Speech-GGUF

- **Created / updated**: 2026-10-30 / 2026-11-13
- **Task / library**: text-to-speech / unknown
- **Relevance**: 19 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=133 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M16. Tree-AI-lab/kouman-tts-bau-waxal-full

- **Created / updated**: 2026-11-12 / 2026-11-13
- **Task / library**: text-to-speech / transformers
- **Relevance**: 17 pts · Generative Music & Audio: text-to-audio; Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=379 · likes=2 · trending=0.0
- **License / access**: apache-2.0 / gated
- **Related papers**: —
- **Datasets / base models**: google/WaxalNLP / unknown
- **Variants in family**: —

#### M17. nphearum/PsarAI-S2S-GGUF

- **Created / updated**: 2026-10-27 / 2026-11-13
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech, automatic speech recognition; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=297 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / nphearum/PsarAI-S2S
- **Variants in family**: —

#### M18. Neurobrix/Voxtral-Mini-3B-2507-nbx

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-text-to-text / neurobrix
- **Relevance**: 17 pts · Audio & Speech Language Models: audio llm; Audio Understanding & Reasoning: audio-text (pipeline tag); declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / gated
- **Related papers**: —
- **Datasets / base models**: unknown / mistralai/Voxtral-Mini-3B-2507
- **Variants in family**: —

#### M19. atraq/OmniVoice

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: text-to-speech / omnivoice
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: [arXiv:2604.00688](https://arxiv.org/abs/2604.00688)
- **Datasets / base models**: unknown / Qwen/Qwen3-0.6B
- **Variants in family**: —

#### M20. MuntasirElagami/sudanese-chatterbox

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: text-to-speech / chatterbox
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license mit
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: mit / public
- **Related papers**: —
- **Datasets / base models**: MuntasirElagami/sudanese-arabic-speech / oddadmix/lahgtna-chatterbox-v1
- **Variants in family**: —

#### M21. Symmetris-labs/tts-mms

- **Created / updated**: 2026-09-07 / 2026-11-13
- **Task / library**: text-to-speech / unknown
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag); model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2305.13516](https://arxiv.org/abs/2305.13516)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M22. DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed42

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/EmoFake / unknown
- **Variants in family**: —

#### M23. DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed240

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/EmoFake / unknown
- **Variants in family**: —

#### M24. DeepFense/EmoFake_Wav2Vec2_MLP_NoAug_Seed2

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/EmoFake / unknown
- **Variants in family**: —

#### M25. DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed2

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/EmoFake / unknown
- **Variants in family**: —

#### M26. DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed240

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/EmoFake / unknown
- **Variants in family**: —

#### M27. DeepFense/EmoFake_Wav2Vec2_AASIST_NoAug_Seed42

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/EmoFake / unknown
- **Variants in family**: —

#### M28. DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed42

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/AffectDF / unknown
- **Variants in family**: —

#### M29. DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed240

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/AffectDF / unknown
- **Variants in family**: —

#### M30. DeepFense/AffectDF_Wav2Vec2_MLP_NoAug_Seed2

- **Created / updated**: 2026-11-13 / 2026-11-13
- **Task / library**: audio-classification / pytorch
- **Relevance**: 12 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: DeepFense/AffectDF / unknown
- **Variants in family**: —

## Research signals

- Audio & Speech Language Models: 6 papers
- Audio Understanding & Reasoning: 2 papers
- Speech Generation, Recognition & Dialogue: 2 papers
- Music Foundation Models & Representations: 1 papers
- Generative Music & Audio: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [MusicRWKV: A Multimodal RWKV Framework for Music Representation Learning](https://arxiv.org/abs/2611.16718) | 2026-11-12 | 25 | Music Foundation Models & Representations | — |
| 2 | [Harmony: Bridging Audio Understanding and Editing through Agentic Collaboration](https://arxiv.org/abs/2611.14724) | 2026-11-10 | 17 | Audio & Speech Language Models, Audio Understanding & Reasoning | — |
| 3 | [Right Answers, Inconsistent Evidence: Source-Level Counterfactual Auditing of Large Audio-Language Models](https://arxiv.org/abs/2611.15463) | 2026-11-11 | 16 | Audio & Speech Language Models | [repo](https://github.com/yikise/TRACE) |
| 4 | [Can Music Generation Models Tap Along? Evaluating Generative Approaches to Beat Tracking](https://arxiv.org/abs/2611.14971) | 2026-11-11 | 15 | Generative Music & Audio | — |
| 5 | [Speech Tokenizers are Vulnerable: Transferable Semantic Attack and Robust Tokenizer](https://arxiv.org/abs/2611.14929) | 2026-11-11 | 10 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 6 | [RSE-TTS: Compact Text-to-Speech through Shared Text-Aware Reference Encoding and Generation](https://arxiv.org/abs/2611.15464) | 2026-11-11 | 10 | Speech Generation, Recognition & Dialogue | — |
| 7 | [CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction](https://arxiv.org/abs/2611.15101) | 2026-11-11 | 10 | Audio Understanding & Reasoning | — |
| 8 | [Structured Speaker Conditioning for Diarization-Guided Target-Speaker ASR](https://arxiv.org/abs/2611.16371) | 2026-11-12 | 7 | Audio & Speech Language Models | — |
| 9 | [JEV-VAD: Efficient Semantic Endpointing via Task-First Conditioning and Decoder-Prefix Pruning](https://arxiv.org/abs/2611.15362) | 2026-11-11 | 7 | Audio & Speech Language Models | — |
| 10 | [DeALR: Decoupled Audio-Latent Optimization with Acoustic Backtracking for Test-Time Reasoning](https://arxiv.org/abs/2611.15439) | 2026-11-11 | 7 | Audio & Speech Language Models | — |

## Paper cards

### 1. MusicRWKV: A Multimodal RWKV Framework for Music Representation Learning

- **Authors**: Terry Tan
- **Date / sources**: 2026-11-12 · arxiv
- **Relevance**: 25 pts · Music Foundation Models & Representations: music foundation model, music representation learning, music understanding
- **Links**: [Paper](https://arxiv.org/abs/2611.16718) · [PDF](https://arxiv.org/pdf/2611.16718v1)

Recent music foundation models have achieved remarkable progress in music representation learning, yet most existing approaches rely on Transformer architectures whose quadratic attention complexity introduces substantial computational and memory overhead when modeling long-duration music recordings. In this work, we propose MusicRWKV, a multimodal music representation learning framework built upon the RWKV…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. Harmony: Bridging Audio Understanding and Editing through Agentic Collaboration

- **Authors**: Zhongyi Tong, Yapeng Tian
- **Date / sources**: 2026-11-10 · arxiv
- **Relevance**: 17 pts · Audio Understanding & Reasoning: audio understanding; Audio & Speech Language Models: audio-language model
- **Links**: [Paper](https://arxiv.org/abs/2611.14724) · [PDF](https://arxiv.org/pdf/2611.14724v1)

Natural-language audio editing requires connecting a user's intent to specific sounds and time regions while preserving surrounding content. Complex requests make this connection demanding: an edit may select one occurrence, depend on a temporal relation, or modify a source that overlaps with other sounds. We introduce Harmony, an agentic framework that bridges audio understanding and editing through collaboration…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. Right Answers, Inconsistent Evidence: Source-Level Counterfactual Auditing of Large Audio-Language Models

- **Authors**: Yi Zhang, Yi Li, Hongwei Du
- **Date / sources**: 2026-11-11 · arxiv
- **Relevance**: 16 pts · Audio & Speech Language Models: audio-language model; has open-source code link
- **Links**: [Paper](https://arxiv.org/abs/2611.15463) · [PDF](https://arxiv.org/pdf/2611.15463v1) · [Code 1](https://github.com/yikise/TRACE)

A large audio-language model (LALM) can answer "is a cat present?" about a mixture correctly, and its confidence can drop when the cat is removed, yet this does not show that it can tell the cat's presence from its absence. We introduce TRACE. It deletes the queried source and each rival in turn and asks whether every view still containing that sound outscores the view with it removed. Across 8 LALMs and 3,456…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Can Music Generation Models Tap Along? Evaluating Generative Approaches to Beat Tracking

- **Authors**: Kun Fang, Ziyu Wang, Ichiro Fujinaga
- **Date / sources**: 2026-11-11 · arxiv
- **Relevance**: 15 pts · Generative Music & Audio: music generation, musicgen
- **Links**: [Paper](https://arxiv.org/abs/2611.14971) · [PDF](https://arxiv.org/pdf/2611.14971v1)

Existing studies have shown that music generative models can generate synchronized tracks that play alongside an input song. Can we extend this capability to develop a generative approach to beat tracking? To answer this question, we equip a pretrained MusicGen model with an audio-conditioning adapter to generate percussion tracks synchronized with the input music, from which we extract the beat positions. We train…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Speech Tokenizers are Vulnerable: Transferable Semantic Attack and Robust Tokenizer

- **Authors**: Zhisheng Zhang, Yifan Mi, Yixuan Zhou, Haiyun Li, Shengbo Cai, Dongfu Song, Ziang Xu, Jie Hao et al.
- **Date / sources**: 2026-11-11 · arxiv
- **Relevance**: 10 pts · Audio & Speech Language Models: audio-language model; Speech Generation, Recognition & Dialogue: automatic speech recognition
- **Links**: [Paper](https://arxiv.org/abs/2611.14929) · [PDF](https://arxiv.org/pdf/2611.14929v1)

Speech tokenizers serve as speech front ends, encoding input speech signals into representations for downstream models, such as automatic speech recognition (ASR) systems and large audio-language models (LALMs). In this paper, we find that speech tokenizers are fragile at the semantic level: small perturbations can disrupt their semantic encoding process and consequently cause severe degradation in downstream ASR…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. RSE-TTS: Compact Text-to-Speech through Shared Text-Aware Reference Encoding and Generation

- **Authors**: Ming Ma, Mingjie Chen, Yuanzhong Zheng, Hengyao Bao, Hailin Yu, Shijing Yu, Hao Qiu, Gongfan Cao et al.
- **Date / sources**: 2026-11-11 · arxiv
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: text-to-speech
- **Links**: [Paper](https://arxiv.org/abs/2611.15464) · [PDF](https://arxiv.org/pdf/2611.15464v1)

Can a speech generator also serve as an effective voice encoder? We show that a pretrained autoregressive text-to-speech (TTS) backbone can be repurposed for reference compression, improving speaker similarity in subsequent synthesis. Jointly encoding reference speech and its transcript further strengthens this capability. Controlled ablations and activation interventions trace the text benefit through intermediate…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction

- **Authors**: Pengyang Shi, Jinlu Zhang, Chunze Lin, Yizhou Wang, Li Yi
- **Date / sources**: 2026-11-11 · arxiv
- **Relevance**: 10 pts · Audio Understanding & Reasoning: audio-text
- **Links**: [Paper](https://arxiv.org/abs/2611.15101) · [PDF](https://arxiv.org/pdf/2611.15101v1)

Generating whole-body gestures that are simultaneously rhythmically synchronized with speech audio and semantically aligned with text descriptions is a fundamental challenge in embodied AI and social robotics. We tackle this Audio-Text-to-Motion (AT2M) problem by composing two independently-trained diffusion models at inference time and refine bias in joint inference by modeling the copula score $s_I$. A rigorous…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. Structured Speaker Conditioning for Diarization-Guided Target-Speaker ASR

- **Authors**: Ruoyu Wang, Shutong Niu, Jun Du, Weixin Zhu, Yannan Wang
- **Date / sources**: 2026-11-12 · arxiv
- **Relevance**: 7 pts · Audio & Speech Language Models: audio foundation model
- **Links**: [Paper](https://arxiv.org/abs/2611.16371) · [PDF](https://arxiv.org/pdf/2611.16371v1)

We propose structured speaker conditioning (SSC) for diarization-guided target-speaker recognition. SSC combines local activity structure with session-level acoustic identity to construct identity-consistent target conditions that control the acoustic encoder. Target-centric relational encoding (TCRE) retains per-speaker activity histories and factorized second- and third-order relations, capturing overlap and turn…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. JEV-VAD: Efficient Semantic Endpointing via Task-First Conditioning and Decoder-Prefix Pruning

- **Authors**: Jintao Liang, Nan Li, Longbiao Wang, Tubin Huang, Min Xu
- **Date / sources**: 2026-11-11 · arxiv
- **Relevance**: 7 pts · Audio & Speech Language Models: audio-language model
- **Links**: [Paper](https://arxiv.org/abs/2611.15362) · [PDF](https://arxiv.org/pdf/2611.15362v1)

Semantic endpointing must distinguish a completed turn from a temporary pause, yet its binary output does not require the full generation pathway of an audio-language model. We propose JEV-VAD, an ASR-free framework that combines task-first conditioning, a scalar endpoint readout, and decoder-prefix pruning. The question and completion criteria are placed before audio tokens, allowing causal decoder attention to…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. DeALR: Decoupled Audio-Latent Optimization with Acoustic Backtracking for Test-Time Reasoning

- **Authors**: Haoyu He, Yan Rong, Li Liu
- **Date / sources**: 2026-11-11 · arxiv
- **Relevance**: 7 pts · Audio & Speech Language Models: audio-language model
- **Links**: [Paper](https://arxiv.org/abs/2611.15439) · [PDF](https://arxiv.org/pdf/2611.15439v1)

Large audio-language models (LALMs) typically encode audio once and conduct subsequent multi-step reasoning in a language-dominated space, weakening access to fine-grained acoustic evidence. Although recent multimodal approaches have explored re-engaging perceptual inputs during reasoning, whether a frozen LALM can actively revisit crucial acoustic evidence in the latent space at test time remains underexplored. To…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
