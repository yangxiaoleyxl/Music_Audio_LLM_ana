# 音乐/音频大模型研究雷达

面向音乐、音频与语音大模型研究的每日增量监控管道。它会从学术数据源发现新论文、从 Hugging Face Hub 发现新模型与模型更新，按研究主题分别打分，用 SQLite 记录已见条目，并输出适合每天快速阅读的 Markdown 与机器可读 JSON 日报。

## 直接运行

不需要安装第三方依赖：

```bash
cd audio-llm-radar
./scripts/run_daily.sh
```

输出位于：

- `reports/latest.md`：最新一期日报
- `reports/YYYY-MM-DD.md`：归档日报
- `reports/YYYY-MM-DD.json`：供后续仪表盘、LLM 总结或 Zotero 导入使用
- `data/radar.db`：增量去重状态

首次运行会把回看窗口内的相关论文都视为新增。再次运行时只输出新出现的论文。需要重看整个窗口时：

```bash
./scripts/run_daily.sh --include-seen
```

需要验证某一天或临时扩大窗口时：

```bash
./scripts/run_daily.sh --date 2026-08-09 --days 14 --include-seen --no-write-state
```

## 当前监控范围

主题配置在 `config/topics.json`，默认覆盖：

1. 音频/语音语言模型
2. 音乐基础模型与表征
3. 生成式音乐与音频
4. 音频理解与推理
5. 语音生成、识别与对话
6. 评测、对齐、安全与版权

每个短语都有权重：标题命中按两倍权重计分，摘要命中按一倍计分；跨两个主题的论文会累加前两个主题分数，含 GitHub 代码链接或被多个来源收录会小幅加分。`minimum_score` 控制进入日报的阈值。

## 数据源设计

| 来源 | 默认 | 作用 | 凭据 |
|---|---:|---|---|
| arXiv | 开 | 最快发现预印本，是每日主入口 | 无 |
| Semantic Scholar | 开 | 补元数据并发现跨领域论文 | API key 可选但推荐 |
| OpenAlex | 关 | 补充期刊、会议与开放获取信息 | 当前需 API key |
| Hugging Face Models | 开 | 发现最新/更新模型、采用信号与可复现资产 | token 可选 |

复制环境变量模板后可提高限额：

```bash
cp .env.example .env
```

单一来源失败不会中断整期日报；错误会同时出现在终端与日报顶部，避免静默漏报。数据源命中只负责“召回”，最终仍由统一的本地主题打分过滤。

## 自动每天运行

### GitHub Actions（推荐）

项目自带 `.github/workflows/daily-radar.yml`，每天 11:30 UTC 运行，并把日报和 SQLite 状态提交回仓库。也支持手动触发。

把整个 `audio-llm-radar` 目录作为仓库根目录推到 GitHub；如果它只是大仓库的子目录，需要把 workflow 中的命令和 `git add` 路径加上此前缀。可在仓库 Secrets 中添加：

- `SEMANTIC_SCHOLAR_API_KEY`
- `OPENALEX_API_KEY`（只有开启 OpenAlex 时需要）
- `OPENALEX_EMAIL`
- `HF_TOKEN`（公开模型无需 token，配置后限额更稳）

## 为什么监控 Hugging Face 合理

合理，但它补充的是“工程与采用信号”，不能代替论文检索：

- **更靠近可复现性**：权重、模型卡、许可证、数据集、基座模型和 demo 往往比正式论文更早公开。
- **能捕捉论文外进展**：checkpoint 更新、微调版本、量化版本和社区复现不一定产生新论文。
- **采用信号可量化**：downloads、likes、trending score 可帮助发现社区关注，但会受到发布时间、机构影响力和刷量影响。
- **元数据质量不齐**：不少模型卡缺少许可证、评测或论文链接；因此日报将模型与论文分栏，绝不把平台热度当成学术质量。

实现上并发按音频任务标签拉取最近更新的模型，再用 8 路限时并发读取有限数量的模型卡做主题评分。`last_modified` 用于发现更新，`created_at` 用于区分新发布与旧模型维护；同一 repo 只有更新时间变化时才会再次进入增量日报。同一作者基于同一 base model 发布的量化、语言或格式变体会聚合成一个模型家族，日报仍保留变体清单。可在 `sources.huggingface_models.pipeline_tags` 调整任务，在 `max_readmes` 控制 API 请求量。

### 本地 cron

先手工执行一次确认路径，再运行 `crontab -e` 加入：

```cron
30 7 * * * cd /absolute/path/to/audio-llm-radar && ./scripts/run_daily.sh >> data/cron.log 2>&1
```

cron 使用机器本地时区。笔记本睡眠时不会执行，长期监控更适合 GitHub Actions 或服务器。

## 从“论文列表”变成研究工作流

日报每篇论文都预留了“方法/数据/指标/可复现性/可迁移点”阅读记录。建议每周做一次三层筛选：

- **P0：立即复现**——与当前问题直接相关、代码和数据可用、指标可比较。
- **P1：进入 related work**——方法或结论重要，但短期不复现。
- **P2：趋势信号**——暂时不读全文，只记录研究方向、团队与任务变化。

JSON 日报保留完整摘要、主题分数、匹配原因和代码链接，后续可以接任意 LLM 做中文结构化总结、实验建议、与自己的论文草稿对比；基础抓取层不绑定某家模型服务，便于复现和控制费用。

## 已有开源方案与取舍

不想维护代码时，可直接试用/部署：

- [AutoLLM/ArxivDigest](https://github.com/AutoLLM/ArxivDigest)：用 LLM 评相关度，可通过 GitHub Actions 和邮件分发。
- [customize-arxiv-daily](https://github.com/JoeLeelyf/customize-arxiv-daily)：LLM 总结、推荐与邮件链路较完整。
- [ADD-arxiv-daily](https://github.com/changjinhan/ADD-arxiv-daily)：音频 deepfake 方向的垂直示例，结构简单。
- [Paper-List-DAILY](https://github.com/islinxu/Paper-List-DAILY)：多主题 Markdown/GitHub Pages 的自动更新范式。
- [arXivDigest 服务](https://arxivdigest.org/)：托管的个性化邮件摘要。

本项目更适合作为可控的研究基础设施：主题与分数透明、数据保存在本地、默认不向 LLM 上传摘要，并可逐步接入 Zotero、邮件/企业微信通知、引用图谱与实验追踪。

## 测试

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## 下一步增强建议

1. 接 LLM 生成“贡献/方法/数据/结果/局限/可迁移实验”六字段摘要，并缓存到 SQLite。
2. 加入关注作者、实验室、会议和引用追踪，避免只靠关键词。
3. 用你的已读/收藏标注训练一个轻量排序器，替换固定权重。
4. 接 Zotero Better BibTeX 或 Zotero Web API，自动进入待读 collection。
5. 每周聚合主题增速、常用数据集、指标与代码开放率，为选题和投稿窗口提供证据。
