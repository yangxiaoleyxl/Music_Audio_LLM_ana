# Music / Audio Foundation Model Research Radar — 2026-11-17

> Lookback window: 2026-11-10 to 2026-11-17 · New papers: 18 · New models: 16 · relevant papers/models in window: 47/65 · raw papers/models: 162/336

Sources: arxiv=88 · semantic_scholar=74 · huggingface_models=336

## Hugging Face model signals

> Activity is not research quality; downloads/likes are adoption signals only — model cards, licenses, benchmarks, and linked papers still need manual review.

| # | Model family | Updated | Task | Score | Variants | Downloads | Likes | License |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [sergei-lic/MiniMax-Music3](https://huggingface.co/sergei-lic/MiniMax-Music3) | 2026-11-17 | text-to-audio | 46 | 1 | 15 | 0 | unknown |
| 2 | [prithivMLmods/MiniMax-Music3-GGUF](https://huggingface.co/prithivMLmods/MiniMax-Music3-GGUF) | 2026-11-17 | text-to-audio | 42 | 1 | 0 | 1 | other |
| 3 | [Jakevin/ACE-Step1.5-Qwen3.5-0.8B-GGUF](https://huggingface.co/Jakevin/ACE-Step1.5-Qwen3.5-0.8B-GGUF) | 2026-11-17 | text-to-audio | 42 | 2 | 304 | 0 | apache-2.0 |
| 4 | [Jayanth-MKV/Haru-4B-GGUF](https://huggingface.co/Jayanth-MKV/Haru-4B-GGUF) | 2026-11-17 | audio-to-audio | 32 | 1 | 157 | 0 | apache-2.0 |
| 5 | [Hashim-Bhagad/voiceguard-xlsr-aasist-indic](https://huggingface.co/Hashim-Bhagad/voiceguard-xlsr-aasist-indic) | 2026-11-17 | audio-classification | 27 | 1 | 0 | 1 | cc-by-nc-4.0 |
| 6 | [Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini) | 2026-11-17 | text-to-speech | 26 | 1 | 93909 | 510 | apache-2.0 |
| 7 | [laion/Humaneness-Voice-Large-1.7-Singing-Experimental](https://huggingface.co/laion/Humaneness-Voice-Large-1.7-Singing-Experimental) | 2026-11-17 | text-to-audio | 24 | 2 | 0 | 0 | cc-by-4.0 |
| 8 | [Ikhlas125/sachai-check-urdu-audio-deepfake](https://huggingface.co/Ikhlas125/sachai-check-urdu-audio-deepfake) | 2026-11-17 | audio-classification | 19 | 1 | 0 | 0 | cc-by-nc-4.0 |
| 9 | [Beagledata/Turn-Detection-Jev](https://huggingface.co/Beagledata/Turn-Detection-Jev) | 2026-11-17 | audio-classification | 15 | 1 | 27 | 1 | apache-2.0 |
| 10 | [richardbertok/verbacue-voice](https://huggingface.co/richardbertok/verbacue-voice) | 2026-11-17 | text-to-speech | 15 | 1 | 0 | 0 | other |
| 11 | [Phoonnx/phoonnx-styletts2](https://huggingface.co/Phoonnx/phoonnx-styletts2) | 2026-11-17 | text-to-speech | 15 | 1 | 0 | 0 | other |
| 12 | [ai-coustics/quail-voice-focus](https://huggingface.co/ai-coustics/quail-voice-focus) | 2026-11-17 | audio-to-audio | 13 | 1 | 329177 | 2 | other |
| 13 | [ai-coustics/quail-multi-speaker](https://huggingface.co/ai-coustics/quail-multi-speaker) | 2026-11-17 | audio-to-audio | 13 | 1 | 54 | 1 | other |
| 14 | [ai-coustics/rook-multi-speaker](https://huggingface.co/ai-coustics/rook-multi-speaker) | 2026-11-17 | audio-to-audio | 13 | 1 | 26 | 1 | other |
| 15 | [neurarank/voice-ai-s2s](https://huggingface.co/neurarank/voice-ai-s2s) | 2026-11-17 | audio-to-audio | 13 | 1 | 0 | 0 | apache-2.0 |
| 16 | [litert-community/granite-speech-5.0-2b](https://huggingface.co/litert-community/granite-speech-5.0-2b) | 2026-11-17 | automatic-speech-recognition | 10 | 1 | 254 | 1 | apache-2.0 |

### Model cards

#### M1. sergei-lic/MiniMax-Music3

- **Created / updated**: 2026-11-17 / 2026-11-17
- **Task / library**: text-to-audio / diffusers
- **Relevance**: 46 pts · Generative Music & Audio: text-to-music, text to music, music generation
- **Adoption signals**: downloads=15 · likes=0 · trending=0.0
- **License / access**: unknown / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M2. prithivMLmods/MiniMax-Music3-GGUF

- **Created / updated**: 2026-11-17 / 2026-11-17
- **Task / library**: text-to-audio / diffusers
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license other
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / MiniMaxAI/MiniMax-Music3
- **Variants in family**: —

#### M3. Jakevin/ACE-Step1.5-Qwen3.5-0.8B-GGUF

- **Created / updated**: 2026-11-16 / 2026-11-17
- **Task / library**: text-to-audio / gguf
- **Relevance**: 42 pts · Generative Music & Audio: text-to-music, text to music, music generation; declares license apache-2.0
- **Adoption signals**: downloads=304 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / Qwen/Qwen3.5-0.8B-Base
- **Variants in family**: Jakevin/ACE-Step1.5-Qwen3.5-0.8B-MLX

#### M4. Jayanth-MKV/Haru-4B-GGUF

- **Created / updated**: 2026-11-16 / 2026-11-17
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 32 pts · Speech Generation, Recognition & Dialogue: speech-to-speech, full duplex speech; Generative Music & Audio: audio generation; declares license apache-2.0
- **Adoption signals**: downloads=157 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / higurashi-ai/Haru-4B
- **Variants in family**: —

#### M5. Hashim-Bhagad/voiceguard-xlsr-aasist-indic

- **Created / updated**: 2026-11-17 / 2026-11-17
- **Task / library**: audio-classification / onnx
- **Relevance**: 27 pts · Speech Generation, Recognition & Dialogue: voice cloning; Evaluation, Alignment, Safety & Copyright: audio deepfake; model card links an arXiv paper; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=1 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: [arXiv:2110.01200](https://arxiv.org/abs/2110.01200) · [arXiv:2202.12233](https://arxiv.org/abs/2202.12233)
- **Datasets / base models**: garystafford/deepfake-audio-detection, mueller91/In-The-Wild, ai4bharat/IndicVoices, mueller91/MLAAD / facebook/wav2vec2-xls-r-300m
- **Variants in family**: —

#### M6. Zyphra/ZONOS3-Mini

- **Created / updated**: 2026-11-09 / 2026-11-17
- **Task / library**: text-to-speech / zonos3
- **Relevance**: 26 pts · Speech Generation, Recognition & Dialogue: speech synthesis, text-to-speech (pipeline tag), voice cloning; model card links an arXiv paper; declares license apache-2.0; community likes 510
- **Adoption signals**: downloads=93909 · likes=510 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: [arXiv:2611.16525](https://arxiv.org/abs/2611.16525)
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M7. laion/Humaneness-Voice-Large-1.7-Singing-Experimental

- **Created / updated**: 2026-11-14 / 2026-11-17
- **Task / library**: text-to-audio / unknown
- **Relevance**: 24 pts · Generative Music & Audio: text-to-audio (pipeline tag), singing voice synthesis; Speech Generation, Recognition & Dialogue: text-to-speech; declares license cc-by-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-4.0 / public
- **Related papers**: —
- **Datasets / base models**: laion/german-english-voice-acting-challenges, laion/singing-voice-1k, laion/synthetic-singing-voice / laion/Humaneness-Voice-Large-1.7
- **Variants in family**: laion/Humaneness-Voice-Large-1.7-Acting-LoRA-r128

#### M8. Ikhlas125/sachai-check-urdu-audio-deepfake

- **Created / updated**: 2026-11-17 / 2026-11-17
- **Task / library**: audio-classification / unknown
- **Relevance**: 19 pts · Evaluation, Alignment, Safety & Copyright: audio deepfake; Speech Generation, Recognition & Dialogue: voice cloning; declares license cc-by-nc-4.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: cc-by-nc-4.0 / public
- **Related papers**: —
- **Datasets / base models**: CSALT/deepfake_detection_dataset_urdu / facebook/wav2vec2-xls-r-300m
- **Variants in family**: —

#### M9. Beagledata/Turn-Detection-Jev

- **Created / updated**: 2026-11-12 / 2026-11-17
- **Task / library**: audio-classification / transformers
- **Relevance**: 15 pts · Generative Music & Audio: text-to-audio; declares license apache-2.0
- **Adoption signals**: downloads=27 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: ASLP-lab/Easy-Turn-Trainset, pipecat-ai/smart-turn-data-v3.2-train / Qwen/Qwen3-Omni-30B-A3B-Instruct
- **Variants in family**: —

#### M10. richardbertok/verbacue-voice

- **Created / updated**: 2026-11-13 / 2026-11-17
- **Task / library**: text-to-speech / unknown
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M11. Phoonnx/phoonnx-styletts2

- **Created / updated**: 2026-06-07 / 2026-11-17
- **Task / library**: text-to-speech / phoonnx
- **Relevance**: 15 pts · Speech Generation, Recognition & Dialogue: text-to-speech (pipeline tag), voice cloning; declares license other
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M12. ai-coustics/quail-voice-focus

- **Created / updated**: 2026-10-29 / 2026-11-17
- **Task / library**: audio-to-audio / aic-sdk
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license other
- **Adoption signals**: downloads=329177 · likes=2 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M13. ai-coustics/quail-multi-speaker

- **Created / updated**: 2026-10-29 / 2026-11-17
- **Task / library**: audio-to-audio / aic-sdk
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license other
- **Adoption signals**: downloads=54 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M14. ai-coustics/rook-multi-speaker

- **Created / updated**: 2026-10-29 / 2026-11-17
- **Task / library**: audio-to-audio / aic-sdk
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license other
- **Adoption signals**: downloads=26 · likes=1 · trending=0.0
- **License / access**: other / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M15. neurarank/voice-ai-s2s

- **Created / updated**: 2026-11-17 / 2026-11-17
- **Task / library**: audio-to-audio / unknown
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: speech-to-speech; declares license apache-2.0
- **Adoption signals**: downloads=0 · likes=0 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / unknown
- **Variants in family**: —

#### M16. litert-community/granite-speech-5.0-2b

- **Created / updated**: 2026-11-06 / 2026-11-17
- **Task / library**: automatic-speech-recognition / litert-lm
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: automatic speech recognition (pipeline tag), speech translation; declares license apache-2.0
- **Adoption signals**: downloads=254 · likes=1 · trending=0.0
- **License / access**: apache-2.0 / public
- **Related papers**: —
- **Datasets / base models**: unknown / ibm-granite/granite-speech-5.0-2b
- **Variants in family**: —

## Research signals

- Speech Generation, Recognition & Dialogue: 12 papers
- Audio & Speech Language Models: 5 papers
- Audio Understanding & Reasoning: 3 papers
- Evaluation, Alignment, Safety & Copyright: 1 papers
- Generative Music & Audio: 1 papers

## Quick scan

| # | Paper | Date | Score | Topics | Code |
|---:|---|---|---:|---|---|
| 1 | [Think2Listen: Evidence-Centric Learning For Agentic Audio Understanding With LALMS](https://arxiv.org/abs/2611.21083) | 2026-11-16 | 27 | Audio & Speech Language Models, Audio Understanding & Reasoning | [repo](https://github.com/JinWang79/Think2Listen) |
| 2 | [AudioTrace: File-Level Membership Detection for Audio Large Language Models](https://arxiv.org/abs/2611.21088) | 2026-11-16 | 24 | Audio & Speech Language Models | — |
| 3 | [Progressive Layer-wise Supervision: Deep-to-Shallow Supervision Annealing for Efficient and Robust Speech Deepfake Detection](https://arxiv.org/abs/2611.20630) | 2026-11-16 | 20 | Audio & Speech Language Models, Evaluation, Alignment, Safety & Copyright | — |
| 4 | [Rethinking Post-Training for Expressive Zero-Shot Text-to-Speech](https://arxiv.org/abs/2611.19787) | 2026-11-15 | 17 | Speech Generation, Recognition & Dialogue | — |
| 5 | [Learning from Distribution: Rethinking One-Hot Supervision for ASR and QA in Speech Language Models](https://arxiv.org/abs/2611.20436) | 2026-11-16 | 16 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | — |
| 6 | [Factorized Self-Supervised Speech Tokenization](https://arxiv.org/abs/2611.18898) | 2026-11-13 | 14 | Audio & Speech Language Models, Speech Generation, Recognition & Dialogue | [repo](https://github.com/ubisoft/ubisoft-laforge-facto) |
| 7 | [Beyond Controllability: Speaker Diversity in Instruction-Guided Text-to-Speech](https://arxiv.org/abs/2611.19030) | 2026-11-14 | 13 | Speech Generation, Recognition & Dialogue | [repo](https://github.com/dlion168/ITTS-Speaker-Diversity) |
| 8 | [ProTTS: End-to-End Prominence-aware Natural and Controllable Text-to-Speech via Automatic Word Stress Discovery](https://arxiv.org/abs/2611.19832) | 2026-11-15 | 11 | Speech Generation, Recognition & Dialogue | — |
| 9 | [A Systematic Study of Cross-Token Transfer for Data-Efficient Non-Verbal Text-to-Speech](https://arxiv.org/abs/2611.19145) | 2026-11-14 | 11 | Speech Generation, Recognition & Dialogue | — |
| 10 | [A lightweight natural language conditioning framework for controllable polyphonic music generation](https://www.semanticscholar.org/paper/1c300473b601a7bd96a9d3809e0a66c03ab3e5f1) | 2026-11-17 | 10 | Generative Music & Audio | — |
| 11 | [No-Shot Text-to-Speech: Limitations of Zero-Shot TTS and its Evaluation Methods in Representing Queer and Transgender Voices](https://arxiv.org/abs/2611.20822) | 2026-11-16 | 10 | Speech Generation, Recognition & Dialogue | — |
| 12 | [Auditory-Feedback-Conditioned Flow TTS for Implicit Lombard Adaptation](https://arxiv.org/abs/2611.19260) | 2026-11-14 | 9 | Speech Generation, Recognition & Dialogue | — |
| 13 | [A Speech-LLM Framework for Enrollment-Free Wake-Word-Guided Target-Speaker Recognition in Complex Noisy Scenarios for Seamless Human-Machine Interaction](https://arxiv.org/abs/2611.19844) | 2026-11-15 | 8 | Speech Generation, Recognition & Dialogue | — |
| 14 | [Real-Time French Speech Translation into Four Congolese National Languages Using Whisper and Language-Specific LoRA Adapters for NLLB-200](https://www.semanticscholar.org/paper/40e5b0d122906fa702a9d27ec1c132b5a290ed2b) | 2026-11-13 | 8 | Speech Generation, Recognition & Dialogue | — |
| 15 | [Latency, Speech Recognition and Turn-Taking in Voice Agents for Spanish Phone Negotiation: An Externally Measured Comparison of Pipecat, LiveKit and GPT-Live](https://arxiv.org/abs/2611.19118) | 2026-11-14 | 7 | Speech Generation, Recognition & Dialogue | [repo](https://github.com/AILabFr8tech/voice-negotiation-agents) |
| 16 | [Post-fusion Event-aware Time-Frequency Refinement for Audio Moment Retrieval](https://arxiv.org/abs/2611.20725) | 2026-11-16 | 6 | Audio Understanding & Reasoning | — |
| 17 | [Does the Voice Matter? Evaluating Frustration Detection on Deployed Clinical Voice-Agent Calls](https://arxiv.org/abs/2611.21001) | 2026-11-16 | 6 | Audio Understanding & Reasoning | — |
| 18 | [Where Is Rank-1 DiM Refusal Intervenable in Multimodal LM Derivatives?](https://arxiv.org/abs/2611.19826) | 2026-11-15 | 6 | Speech Generation, Recognition & Dialogue | — |

## Paper cards

### 1. Think2Listen: Evidence-Centric Learning For Agentic Audio Understanding With LALMS

- **Authors**: Jin Wang, Liang Lin, Kaiwen Luo, Weiliu Wang, Yuxuan Li, Zengxin Han, Gan Zhang, Jingtong Wu et al.
- **Date / sources**: 2026-11-16 · arxiv, semantic_scholar
- **Relevance**: 27 pts · Audio Understanding & Reasoning: audio reasoning, audio understanding; Audio & Speech Language Models: audio-language model; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.21083) · [PDF](https://arxiv.org/pdf/2611.21083v1) · [Code 1](https://github.com/JinWang79/Think2Listen)

Recent advances in large audio-language models (LALMs) have broadened audio understanding across speech, sound, and music, with tool-based agents further supporting these tasks by invoking predefined audio tools. However, a persistent gap remains between perceiving acoustic content and using it as evidence for reasoning: recognizing what is audible does not ensure that a model can identify which cues resolve an…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 2. AudioTrace: File-Level Membership Detection for Audio Large Language Models

- **Authors**: Guangzhi Sun, Xiao Zhan, Shuai Wang, Jose Such, Phil Woodland
- **Date / sources**: 2026-11-16 · arxiv, semantic_scholar
- **Relevance**: 24 pts · Audio & Speech Language Models: audio large language model, audio llm; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.21088) · [PDF](https://arxiv.org/pdf/2611.21088v1)

Significant privacy and copyright concerns are raised by the use of publicly available audio recordings to train audio large language models (LLMs), yet effective auditing methods remain limited. Existing membership inference attacks typically assume knowledge of complete training examples, including their associated textual supervision. In practice, however, audio recordings may be paired with privately generated…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 3. Progressive Layer-wise Supervision: Deep-to-Shallow Supervision Annealing for Efficient and Robust Speech Deepfake Detection

- **Authors**: Hoan My Tran, Xin Wang, Xuechen Liu
- **Date / sources**: 2026-11-16 · arxiv, semantic_scholar
- **Relevance**: 20 pts · Evaluation, Alignment, Safety & Copyright: speech deepfake; Audio & Speech Language Models: speech foundation model; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.20630) · [PDF](https://arxiv.org/pdf/2611.20630v1)

Speech foundation models pretrained via self-supervised learning provide powerful representations for deepfake detection, yet we find that standard fine-tuning exploits only the deepest transformer layers-leaving the majority of the network's capacity discriminatively inert. Layer-wise probing of XLS-R-128 reveals that the top two-thirds of the transformer stack contribute negligibly to anti-spoofing performance…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 4. Rethinking Post-Training for Expressive Zero-Shot Text-to-Speech

- **Authors**: Jingbin Hu, Xinfa Zhu, Hao Wang, Wenjie Tian, Kangxiang Xia, Hangrui Hu, Kexin Huang, Jin Xu et al.
- **Date / sources**: 2026-11-15 · arxiv, semantic_scholar
- **Relevance**: 17 pts · Speech Generation, Recognition & Dialogue: text-to-speech, voice cloning; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.19787) · [PDF](https://arxiv.org/pdf/2611.19787v1)

Zero-shot voice cloning typically emphasizes preserving the timbre and prosodic characteristics of a reference speaker. However, in real-world use, speech should adapt its delivery to the target text rather than remain tied to a fixed speaking style. In this work, we formulate this problem as text-adaptive prosody synthesis for zero-shot voice cloning and study how post-training can endow a cloning model with this…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 5. Learning from Distribution: Rethinking One-Hot Supervision for ASR and QA in Speech Language Models

- **Authors**: Yujie Guo, Hongjie Chen, Jiaming Zhou, Jian Kang, Jie Li, Yongxiang Li, Yong Qin
- **Date / sources**: 2026-11-16 · arxiv, semantic_scholar
- **Relevance**: 16 pts · Audio & Speech Language Models: speech language model; Speech Generation, Recognition & Dialogue: automatic speech recognition; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.20436) · [PDF](https://arxiv.org/pdf/2611.20436v1)

Speech language models (SLMs) exhibit strong capabilities in automatic speech recognition (ASR) and general-purpose speech understanding, yet ASR-specific training often degrades spoken question answering (QA) performance. We revisit this conflict from the perspective of task-specific input--output mappings and one-hot supervision. Our findings reveal pronounced task-asymmetric effects: ASR-only training severely…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 6. Factorized Self-Supervised Speech Tokenization

- **Authors**: Benjamin Van Niekerk, Jean-Philippe Letendre, Nicol Visser, Hugo Seute, Herman Kamper, Mirco Ravanelli
- **Date / sources**: 2026-11-13 · arxiv, semantic_scholar
- **Relevance**: 14 pts · Audio & Speech Language Models: spoken language model; Speech Generation, Recognition & Dialogue: text-to-speech; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.18898) · [PDF](https://arxiv.org/pdf/2611.18898v1) · [Code 1](https://github.com/ubisoft/ubisoft-laforge-facto)

Speech tokenizers convert audio into discrete units, enabling language models to process and generate speech. The goal is to learn compact, text-like representations while preserving enough detail to reconstruct a speaker's voice and delivery. We propose Facto: a factorized tokenizer that disentangles time-varying information (content and prosody) from static components (speaker identity and recording conditions).…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 7. Beyond Controllability: Speaker Diversity in Instruction-Guided Text-to-Speech

- **Authors**: Yi-Cheng Lin, Jia-Kai Dong, Kuan-Yu Chen, Szu-Chi Chen, Jian-Jiun Ding, Sung-Feng Huang, Yusuke Hirota, Hung-yi Lee
- **Date / sources**: 2026-11-14 · arxiv, semantic_scholar
- **Relevance**: 13 pts · Speech Generation, Recognition & Dialogue: text-to-speech; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.19030) · [PDF](https://arxiv.org/pdf/2611.19030v1) · [Code 1](https://github.com/dlion168/ITTS-Speaker-Diversity)

Instruction-guided text-to-speech (ITTS) lets users specify voice properties in natural language. Applications from conversational AI character voices to synthetic training data for downstream speech models depend on the system producing many distinct voices when the same broad category is requested repeatedly. No prior work audits whether ITTS outputs are in fact diverse, either compared to real speech or across…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 8. ProTTS: End-to-End Prominence-aware Natural and Controllable Text-to-Speech via Automatic Word Stress Discovery

- **Authors**: Sai Harshitha Aluru, Chiranjeevi Yarra
- **Date / sources**: 2026-11-15 · arxiv, semantic_scholar
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.19832) · [PDF](https://arxiv.org/pdf/2611.19832v1)

Natural speech conveys meaning not only through words, but also through the prominence on a few words. Yet most text-to-speech (TTS) systems remain prominence-unaware, existing prominence-aware TTS require external stress annotations, while unsupervised stress detectors operate in isolation, disconnected from synthesis. This creates a fundamental gap no existing system can automatically discover where stress should…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 9. A Systematic Study of Cross-Token Transfer for Data-Efficient Non-Verbal Text-to-Speech

- **Authors**: Jing Pan, Haibin Wu, Minxue Niu, Florian Metze, Yuzong Liu
- **Date / sources**: 2026-11-14 · arxiv, semantic_scholar
- **Relevance**: 11 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.19145) · [PDF](https://arxiv.org/pdf/2611.19145v1)

Non-verbal vocalizations (NVs), such as laughter and breath, carry affective cues that words alone do not convey. Yet NV data remains scarce because speech annotation pipelines often omit or normalize these events. Existing work has improved NV text-to-speech through model design and data curation, but whether one NV token can help a model learn another has received little systematic study. We investigate this…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 10. A lightweight natural language conditioning framework for controllable polyphonic music generation

- **Authors**: Animesh Mishra, D. Suma
- **Date / sources**: 2026-11-17 · semantic_scholar
- **Relevance**: 10 pts · Generative Music & Audio: music generation
- **Links**: [Paper](https://www.semanticscholar.org/paper/1c300473b601a7bd96a9d3809e0a66c03ab3e5f1)

No abstract

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 11. No-Shot Text-to-Speech: Limitations of Zero-Shot TTS and its Evaluation Methods in Representing Queer and Transgender Voices

- **Authors**: Juliana Francis, Robin Netzorg, Joakim Gustafson, Éva Székely
- **Date / sources**: 2026-11-16 · arxiv
- **Relevance**: 10 pts · Speech Generation, Recognition & Dialogue: text-to-speech
- **Links**: [Paper](https://arxiv.org/abs/2611.20822) · [PDF](https://arxiv.org/pdf/2611.20822v1)

Gender expansive voices remain underrepresented in speech datasets, which could cause challenges with generalizability in zero-shot Text-To-Speech (TTS) systems. We evaluate six zero-shot TTS models on two datasets: one containing non gender expansive voices (N-GE) and one with gender expansive (GE) voices from self-identified speakers. Human ratings found that 2 of the 6 models synthesize less similar GE voices…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 12. Auditory-Feedback-Conditioned Flow TTS for Implicit Lombard Adaptation

- **Authors**: Yunya Wang, Satoshi Nakamura
- **Date / sources**: 2026-11-14 · arxiv, semantic_scholar
- **Relevance**: 9 pts · Speech Generation, Recognition & Dialogue: text-to-speech, automatic speech recognition; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.19260) · [PDF](https://arxiv.org/pdf/2611.19260v1)

Conventional text-to-speech (TTS) systems can lose intelligibility in noise environments because they cannot adapt to environmental changes. However, humans tend to increase their vocal efforts in noisy environments, a phenomenon known as the Lombard effect. Building on an auditory-feedback Lombard TTS, we investigate whether a pretrained Flow-based TTS can learn acoustic adaptation directly from auditory feedback…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 13. A Speech-LLM Framework for Enrollment-Free Wake-Word-Guided Target-Speaker Recognition in Complex Noisy Scenarios for Seamless Human-Machine Interaction

- **Authors**: Yuxiang Mei, Dongxing Xu, Yanhua Long
- **Date / sources**: 2026-11-15 · arxiv, semantic_scholar
- **Relevance**: 8 pts · Speech Generation, Recognition & Dialogue: speech synthesis, automatic speech recognition; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.19844) · [PDF](https://arxiv.org/pdf/2611.19844v1)

Target-speaker automatic speech recognition (TS-ASR) is essential for reliable human-machine interaction in complex acoustic environments, where overlapping speech and background noise make it difficult to identify and recognize the intended speaker. Existing approaches typically rely on speaker enrollment or cascaded processing pipelines, limiting their flexibility in practical applications. To address these…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 14. Real-Time French Speech Translation into Four Congolese National Languages Using Whisper and Language-Specific LoRA Adapters for NLLB-200

- **Authors**: Jean-Christophe B. Wizamo, S. Kasereka
- **Date / sources**: 2026-11-13 · semantic_scholar
- **Relevance**: 8 pts · Speech Generation, Recognition & Dialogue: speech translation
- **Links**: [Paper](https://www.semanticscholar.org/paper/40e5b0d122906fa702a9d27ec1c132b5a290ed2b) · [PDF](https://www.ijisrt.com/assets/upload/files/IJISRT26NOV245.pdf)

French is the sole official language of the Democratic Republic of the Congo, yet much of the population communicates daily in Lingala, Swahili, Tshiluba or Kikongo. This paper presents a cascaded system that transcribes spoken French with Whisper and translates it with NLLB-200-distilled-600M, specialized by one Low-Rank Adaptation (LoRA) adapter per target language on a shared frozen base model.

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 15. Latency, Speech Recognition and Turn-Taking in Voice Agents for Spanish Phone Negotiation: An Externally Measured Comparison of Pipecat, LiveKit and GPT-Live

- **Authors**: Jovan Popoca Moran, Eduardo de Avila-Armenta, Raúl Alejandro Aquino-Ibarra, Jorge Octavio Nicolás-Díaz, Umberto Leon-Dominguez
- **Date / sources**: 2026-11-14 · arxiv, semantic_scholar
- **Relevance**: 7 pts · Speech Generation, Recognition & Dialogue: speech synthesis; has open-source code link; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.19118) · [PDF](https://arxiv.org/pdf/2611.19118v1) · [Code 1](https://github.com/AILabFr8tech/voice-negotiation-agents)

A voice agent that negotiates by phone must answer quickly, understand spoken amounts and cope with a caller who talks over it. We compared three architectures for such an agent, negotiating freight rates in Spanish: two cascades (speech recognition, language model and speech synthesis) orchestrated by Pipecat and by LiveKit Agents, and GPT-Live, an OpenAI speech model that listens and speaks without separate…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 16. Post-fusion Event-aware Time-Frequency Refinement for Audio Moment Retrieval

- **Authors**: Feiyang Xiao, Li'ang Luo, Kejia Zhang, Qiaoxi Zhu, Guangjun He, Pengming Feng, Jian Guan
- **Date / sources**: 2026-11-16 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Audio Understanding & Reasoning: audio-text; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.20725) · [PDF](https://arxiv.org/pdf/2611.20725v1)

Audio Moment Retrieval (AMR) aims to locate the temporal segment within a long audio recording that semantically corresponds to a natural-language query. This task is particularly challenging because query-related audio events are often sparsely distributed and embedded in complex acoustic environments, where background sounds and acoustically similar events can easily obscure the target moments. Existing methods…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 17. Does the Voice Matter? Evaluating Frustration Detection on Deployed Clinical Voice-Agent Calls

- **Authors**: Annika Michael, Zachary Ellis, Yuxiang Zhou, Samuel Thio, Yajie Vera He, Spencer Hazel, Jared Joselowitz
- **Date / sources**: 2026-11-16 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Audio Understanding & Reasoning: audio-text; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.21001) · [PDF](https://arxiv.org/pdf/2611.21001v1)

Autonomous voice agents now conduct routine clinical follow-up calls, so some automated triage is unavoidable. A patient becoming frustrated is one thing that triage should catch. These systems typically read only the transcript the speech-to-text stage produces, not the voice, and whether that is enough is largely untested on real clinical speech. We study per-turn frustration detection on real patient calls from a…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_

### 18. Where Is Rank-1 DiM Refusal Intervenable in Multimodal LM Derivatives?

- **Authors**: Chansu Han, Seok-Hwan Choi, Takeshi Takahashi
- **Date / sources**: 2026-11-15 · arxiv, semantic_scholar
- **Relevance**: 6 pts · Speech Generation, Recognition & Dialogue: text-to-speech; found in multiple academic sources
- **Links**: [Paper](https://arxiv.org/abs/2611.19826) · [PDF](https://arxiv.org/pdf/2611.19826v1)

Open-weight model hubs now ship not only chat checkpoints but a long tail of derivatives---fine-tunes, safety guards, vision--language models (VLMs), audio wrappers, and generative heads---yet residual-stream safety audits still often intervene at a single site, usually the text decoder $T$. We ask a localization question under one shared mean / rank-1 difference-in-means (DiM) extract$=$intervene protocol, with…

**Reading notes** (method / data / metrics / reproducibility / transferability): _TODO_
