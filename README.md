<!-- 主线：把环境、操作、截图和结论连成可核对的证据链 | 钩子类型：真实工作流 | 平台：GitHub README | 语气 1.5 · 钩子 3 -->

# lab-report-autopilot

从作业要求和 DOCX 模板开始，完成环境检查、真实操作、截图取证、内容撰写和逐页验收。给需要交实验、实训或专业实践报告的人用。

实验报告通常不缺一段能读的正文。麻烦的是另一件事：文字说成功了，截图里却看不到结果；作业要求 Windows，实际操作来自 macOS；代码能运行，贴进报告的版本又不一样。`lab-report-autopilot` 把这些容易断开的地方放进同一条流程。

```mermaid
flowchart LR
    A["要求与模板"] --> B["专业路由"]
    B --> C["环境检查"]
    C --> D["实际操作"]
    D --> E["截图与原始结果"]
    E --> F["报告草稿"]
    F --> G["DOCX 组装"]
    G --> H["逐页检查"]
    H --> I["最终报告"]
```

## 它怎么工作

| 阶段 | 实际动作 |
| --- | --- |
| 任务拆解 | 区分学校模板、正面参考、反例、任务材料和涉密工作材料 |
| 专业路由 | 只加载本次实验需要的专业规则，不把所有课程知识塞进一个提示词 |
| 环境选择 | macOS 能原生完成就直接用；不兼容时检查现有 Parallels、Kali 或 Windows 虚拟机 |
| 实操取证 | 先列证据计划，再运行命令、代码或软件；每个结论对应真实截图或输出 |
| 内容撰写 | 按“目的 → 操作 → 证据 → 观察 → 分析”写步骤，代码只保留作业需要的部分 |
| 文档验收 | 保留学校 DOCX 版式，渲染后逐页检查截图、表格、字体、页码和空白页 |

自动化到缺少环境或证据为止。需要 Windows 专属界面但没有 Windows 环境时，它会停下来说明缺什么，不会补一张看似合理的图。

## Quick Start

```bash
git clone git@github.com:Fldicoahkiin/lab-report-autopilot.git ~/.codex/skills/lab-report-autopilot
python ~/.codex/skills/lab-report-autopilot/scripts/probe_environment.py --json
```

在 Codex 中调用：

```text
Use $lab-report-autopilot to complete this packet-analysis experiment,
capture real evidence, and produce a verified DOCX report.
```

也可以先建立报告工作区：

```bash
python scripts/init_report.py work/arp-report \
  --kind lab \
  --discipline packet-analysis \
  --title "ARP 协议抓包与字段分析"
```

生成的目录里有报告草稿、证据计划、原始截图、处理副本、笔记、源码和最终输出位置。

## 已有专业包

| 专业包 | 当前覆盖 |
| --- | --- |
| `packet-analysis` | Wireshark、tshark、ARP、ICMP、TCP、DNS、HTTP、PCAP |
| `routing-switching` | VLAN、路由、交换、ACL、NAT、拓扑和连通性验证 |
| `security-operations` | 告警复核、异常外联、终端检查、误报判断、本地靶场 |
| `databases` | SQL、表结构、CRUD、连接查询、视图、过程和结果网格 |
| `programming` | C/C++、Python、Java、数据结构、算法和编译运行证据 |
| `data-visualization` | 数据来源、清洗、图表选择、绘图代码和图表解读 |
| `web-development` | HTML、CSS、JavaScript、响应式页面、控制台和网络请求 |
| `computer-architecture` | 电路、CPU、寄存器、存储器、汇编和仿真波形 |

抓包包会明确区分 capture filter 和 display filter，要求记录接口、帧号、字段和值，并保留原始 `.pcapng`。数据库包要求查询文本、结果网格和行数同屏可查。不同课程不再共用一份模糊的“截图如下”规则。

## 涉密工作怎么处理

真实工作材料只用来确定实践方向，不直接进入报告仓库。

例如，原工作涉及异常外联核查、终端告警或弱口令整改时，报告会在本地隔离环境重新搭建同类流程。截图来自这次本地操作，并在正文里标为“本地复现”；客户名称、内部地址、资产编号、告警详情、人员信息和原始截图不会被复制。

## 仓库结构

```text
lab-report-autopilot/
├── SKILL.md
├── agents/openai.yaml
├── assets/templates/
│   ├── lab-report.md
│   └── professional-practice.md
├── references/
│   ├── disciplines.md
│   ├── discipline-*.md
│   ├── environment-playbook.md
│   ├── evidence-and-screenshots.md
│   ├── confidential-work.md
│   ├── writing-and-code.md
│   └── docx-qa.md
└── scripts/
    ├── init_report.py
    ├── probe_environment.py
    └── evidence_manifest.py
```

## 边界

- 不生成或借用软件运行截图充当证据。
- 不把本地复现写成生产环境操作。
- 不对未授权主机做扫描、爆破或漏洞利用。
- 不替用户填写教师签名、成绩和审核意见。
- 学校提供的 DOCX 模板优先于仓库里的通用草稿模板。
