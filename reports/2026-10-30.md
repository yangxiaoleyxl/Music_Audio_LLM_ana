# Music / Audio Foundation Model Research Radar — 2026-10-30

> Lookback window: 2026-10-23 to 2026-10-30 · New papers: 5 · New models: 5 · relevant papers/models in window: 36/84 · raw papers/models: 150/358

Sources: arxiv=93 · semantic_scholar=57 · huggingface_models=358

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [OpenLLM-France/Luciole-8B-Audio-1.0](https://huggingface.co/OpenLLM-France/Luciole-8B-Audio-1.0) | 2026-10-30 | audio-text-to-text | 57 | 1 | 1011 | 8 | apache-2.0 |
| 2 | [aididian/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/aididian/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) | 2026-10-30 | automatic-speech-recognition | 40 | 1 | 0 | 0 | other |
| 3 | [remsky/kokoro-inno-clone-tuner](https://huggingface.co/remsky/kokoro-inno-clone-tuner) | 2026-10-30 | text-to-speech | 16 | 1 | 1319424 | 34 | apache-2.0 |
| 4 | [kuris1213/kurisu-v2proplus](https://huggingface.co/kuris1213/kurisu-v2proplus) | 2026-10-30 | text-to-speech | 15 | 1 | 0 | 0 | other |
| 5 | [SpeechAntiSpoofingBenchmarks/XLS-R-1B-AntiDeepfake-NDA](https://huggingface.co/SpeechAntiSpoofingBenchmarks/XLS-R-1B-AntiDeepfake-NDA) | 2026-10-29 | audio-classification | 15 | 1 | 27 | 1 | cc-by-nc-sa-4.0 |

### Model cards

#### M1. OpenLLM-France/Luciole-8B-Audio-1.0

- **Created / updated**: 2026-09-18 / 2026-10-30
- **Task / library**: audio-text-to-text / nemo
- **Relevance**: 57 pts · Audio & Speech Language Models: audio language model, audio-language model, audio llm; Speech Generation, Recognition & Dialogue: automatic speech recognition, speech translation; Audio Understanding & Reasoning: audio understanding, audio-text (pipeline tag); Music Foundation Models & Representations: music understanding
- **Adoption signals**: downloads=1011 · likes=8 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2410.12109](https://arxiv.org/abs/2410.12109)
- **Datasets / base models**: OpenLLM-France/Luciole-Audio-Training-Dataset / OpenLLM-France/Luciole-8B-Instruct-1.1, nvidia/parakeet-tdt-0.6b-v3
- **Variants in family**: —

#### M2. aididian/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B

- **Created / updated**: 2026-10-30 / 2026-10-30
- **Task / library**: automatic-speech-recognition / nemo
- **Relevance**: 40 pts · Audio Understanding & Reasoning: audio reasoning, audio question answering, audio understanding; Speech Generation, Recognition & Dialogue: automatic speech recognition, speech translation; Audio & Speech Language Models: speech llm; model card links an arXiv paper
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: [arXiv:2310.09424](https://arxiv.org/abs/2310.09424)
- **Datasets / base models**: nvidia/Granary-v2 / nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16
- **Variants in family**: —

#### M3. remsky/kokoro-inno-clone-tuner

- **Created / updated**: 2026-08-31 / 2026-10-30
- **Task / library**: text-to-speech / unknown
- **Relevance**: 16 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license apache-2.0; community likes 34
- **Adoption signals**: downloads=1319424 · likes=34 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: parler-tts/libritts_r_filtered, facebook/voxpopuli, amphion/Emilia-Dataset / hexgrad/Kokoro-82M
- **Variants in family**: —

#### M4. kuris1213/kurisu-v2proplus

- **Created / updated**: 2026-10-30 / 2026-10-30
- **Task / library**: text-to-speech / tensorrt
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M5. SpeechAntiSpoofingBenchmarks/XLS-R-1B-AntiDeepfake-NDA

- **Created / updated**: 2026-06-09 / 2026-10-29
- **Task / library**: audio-classification / unknown
- **Relevance**: 15 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; model card links an arXiv paper; declares license cc-by-nc-sa-4.0
- **Adoption signals**: downloads=27 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-sa-4.0 / public
- **Related papers**: [arXiv:2506.21090](https://arxiv.org/abs/2506.21090)
- **Datasets / base models**: unknown / nii-yamagishilab/xls-r-1b-anti-deepfake-nda
- **Variants in family**: —

## Research signals

- Speech Generation, Recognition & Dialogue: 4 papers
- Audio Understanding & Reasoning: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [Danger Detection Through Audio Captioning and Classification Fusion](https://www.semanticscholar.org/paper/249faf77a738461b2424b258877977b42df1af3a) | 2026-10-28 | 10 | Audio Understanding & Reasoning | — |
| 2 | [A Generative Artificial Intelligence-Based Mechanism for Mobile Conversational Interaction in Japanese Language Learning](https://www.semanticscholar.org/paper/c3e2cb14c29ae58df4c744491c3377c848115042) | 2026-10-27 | 7 | Speech Generation, Recognition & Dialogue | — |
| 3 | [DO NATURAL AO ARTIFICIAL: A ASCENSÃO DA CLONAGEM DE VOZ E O FUTURO DA AUTENTICIDADE VOCAL](https://www.semanticscholar.org/paper/601446fed4960310ceb6bcc2635776e34f2e7481) | 2026-10-28 | 6 | Speech Generation, Recognition & Dialogue | — |
| 4 | [Assesment of Multilingual Automatic Speech Recognition for Swahili, Kikuyu and Kalenjin Languages](https://www.semanticscholar.org/paper/366aab546c1842bd75235170ca57bb533d4c3a7e) | 2026-10-28 | 6 | Speech Generation, Recognition & Dialogue | — |
| 5 | [Demystifying Artificial Intelligence (AI) in Health care: Is AI Friend or Foe?](https://www.semanticscholar.org/paper/d2f39a703b3b101ef6c2e3cce688d327d9bd0984) | 2026-10-27 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. Danger Detection Through Audio Captioning and Classification Fusion

- **Authors**: Maria-Christina Stampa, Marina-Eirini Stamatiadou, Charalampos Dimoulas
- **Date / sources**: 2026-10-28 · semantic_scholar
- **Relevance**: 10 pts · Audio Understanding & Reasoning: audio captioning
- **Links**: [Paper](https://www.semanticscholar.org/paper/249faf77a738461b2424b258877977b42df1af3a) · [PDF](https://doi.org/10.3390/electronics15214985)

Sound is inherently ambiguous, which makes certainty critical in danger recognition, where false alarms and missed detection both carry real consequences. The definition of danger adopted here extends beyond ISO 7731:2003, which covers only intentionally designed alarm signals, to naturally occurring dangerous events such as glass breaking, gunshots, and human distress sounds, following the acoustic surveillance…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. A Generative Artificial Intelligence-Based Mechanism for Mobile Conversational Interaction in Japanese Language Learning

- **Authors**: Xi-Ling Liu, Wei Liu
- **Date / sources**: 2026-10-27 · semantic_scholar
- **Relevance**: 7 pts · Speech Generation, Recognition & Dialogue: speech synthesis, automatic speech recognition
- **Links**: [Paper](https://www.semanticscholar.org/paper/c3e2cb14c29ae58df4c744491c3377c848115042) · [PDF](https://online-journals.org/index.php/i-jim/article/download/63476/17473)

Japanese language learning has long been constrained by acquisition difficulties arising from linguistic distance and by the limited availability of authentic opportunities for conversational interaction. Although mobile learning technologies offer considerable potential to alleviate these constraints, existing tools remain largely focused on vocabulary acquisition and grammar practice, while the dynamic progression…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. DO NATURAL AO ARTIFICIAL: A ASCENSÃO DA CLONAGEM DE VOZ E O FUTURO DA AUTENTICIDADE VOCAL

- **Authors**: Guilherme Salim de Barros, Jonathan Gazzola, Carlos Caetano de Almeida
- **Date / sources**: 2026-10-28 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/601446fed4960310ceb6bcc2635776e34f2e7481) · [PDF](https://doi.org/10.51891/rease.v12i10.30843)

This article aims to analyses voice cloning techniques through an exploratory study of the multilingual zero-shot XTTS-v2 model in the context of Brazilian Portuguese. Thirty synthetic samples were produced based on three reference conditions of approximately 8, 14, and 28 seconds, and subsequently compared with human recordings using acoustic-prosodic descriptors. The reference condition of 28 s showed the lowest…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Assesment of Multilingual Automatic Speech Recognition for Swahili, Kikuyu and Kalenjin Languages

- **Authors**: Joseph Muguro, Ciira Maina, Faith Chege, Fancy Cherotich Koech
- **Date / sources**: 2026-10-28 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition
- **Links**: [Paper](https://www.semanticscholar.org/paper/366aab546c1842bd75235170ca57bb533d4c3a7e) · [PDF](https://stieconference.dkut.ac.ke/10th-stie-proceedings/tutkn5/tutkn5.pdf)

Language barriers continue to limit equitable access to digital and AI-assisted healthcare services, particularly for speakers of indigenous and low-resource languages. While Automatic Speech Recognition (ASR) has achieved significant progress for high-resource languages, its performance remains insufficiently explored for many Kenyan local languages due to limited and inconsistent speech datasets. This study…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Demystifying Artificial Intelligence (AI) in Health care: Is AI Friend or Foe?

- **Authors**: Stefany H. Almaden
- **Date / sources**: 2026-10-27 · semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: voice cloning
- **Links**: [Paper](https://www.semanticscholar.org/paper/d2f39a703b3b101ef6c2e3cce688d327d9bd0984)

ABSTRACT The literature review is saturated with positive tones about the use of AI not only in health care but also in all aspects of our daily lives as well. The positivity range is extensive, ranging from increased accuracy, efficiency, productivity, profitability to creativity, equity, and advancement. Yet, the public is circumspect with continual exposure to news about cybersecurity threats or attacks, identity…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
