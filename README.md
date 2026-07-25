<p align="center">
  <img src="assets/readme/hero.svg" alt="lab-report-autopilot：从作业要求到真实操作、截图和 DOCX 报告" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0b1220" alt="MIT License"></a>
  <a href="https://github.com/Fldicoahkiin/lab-report-autopilot/commits/main"><img src="https://img.shields.io/github/last-commit/Fldicoahkiin/lab-report-autopilot?color=0284c7" alt="Last commit"></a>
  <a href="#支持的课程"><img src="https://img.shields.io/badge/课程包-8-0284c7" alt="8 个课程包"></a>
</p>

`lab-report-autopilot` 是一个给 Codex 使用的实验报告 Skill。它会先读作业要求和 DOCX 模板，再检查当前电脑、运行实验、保留真实结果，最后写入模板并逐页检查。

它适合计算机相关课程的实验、实训和专业实践。重点不在多写几段话，而在于报告里的命令、截图、字段和值确实来自同一次操作。

## 安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装到 Codex：

```bash
npx skills add Fldicoahkiin/lab-report-autopilot -g -a codex
```

也可以手动安装：

```bash
git clone https://github.com/Fldicoahkiin/lab-report-autopilot.git \
  ~/.codex/skills/lab-report-autopilot
```

图片检查脚本使用 Pillow：

```bash
python3 -m pip install -r \
  ~/.codex/skills/lab-report-autopilot/requirements.txt
```

## 调用

把作业要求、学校模板和参考报告交给 Codex，然后说明要实际完成实验：

```text
Use $lab-report-autopilot to complete this packet-analysis assignment
from the supplied DOCX template. Run the experiment, capture the actual
results, and return the checked DOCX.
```

也可以直接用中文：

```text
使用 $lab-report-autopilot 完成这份数据库实验。按学校模板排版，
实际运行 SQL，截取查询和结果，最后交付检查过的 DOCX。
```

## 它会做什么

| 顺序 | Codex 实际做的事 |
| --- | --- |
| 1 | 区分学校模板、参考报告、反例、任务材料和涉密材料 |
| 2 | 检查 macOS、Windows、Kali、Parallels 以及已安装的软件 |
| 3 | 运行命令、代码或图形软件，记录画面中出现的真实值 |
| 4 | 只截与操作和结论有关的画面，保留原始文件 |
| 5 | 按模板写入 DOCX，检查字体、行距、图片、表格、页码和文件名 |

需要 Windows 专属界面但电脑里没有可用的 Windows 环境时，Skill 会说明缺少什么，不会用生成图片代替运行结果。

## 匿名实操示例

下面的示例来自一次本机 HTTP 抓包：启动临时服务，经回环接口访问 `/status.json`，用 Wireshark 核对第 5 帧请求和第 9 帧响应，再把截图放入匿名 DOCX。抓包共 14 帧，返回 `200 OK` 和 `application/json`。

<p align="center">
  <img src="assets/readme/report-proof.png" alt="匿名抓包报告的请求与响应页面" width="100%">
</p>

示例只用于展示完成方式，不含姓名、学校、学号、客户信息或生产环境数据。

## 支持的课程

| 课程包 | 可处理的内容 |
| --- | --- |
| `packet-analysis` | Wireshark、tshark、ARP、ICMP、TCP、DNS、HTTP、PCAP |
| `routing-switching` | VLAN、路由、交换、ACL、NAT、拓扑和连通性检查 |
| `security-operations` | 告警复核、异常外联、终端检查、误报判断、本地靶场 |
| `databases` | SQL、表结构、增删改查、连接查询、视图、过程和结果网格 |
| `programming` | C/C++、Python、Java、数据结构、算法、编译和运行结果 |
| `data-visualization` | 数据来源、清洗、绘图代码、图表和结果说明 |
| `web-development` | HTML、CSS、JavaScript、响应式页面、控制台和网络请求 |
| `computer-architecture` | 电路、CPU、寄存器、存储器、汇编和仿真波形 |

每个课程包单独保存该类实验常见的软件、操作步骤、截图内容和检查项。一次任务通常只读取一个课程包，不把无关课程要求带进报告。

## macOS、Windows 和虚拟机

- macOS 能完成的任务直接使用本机终端和应用。
- Linux 网络或安全工具可以放在已有的 Kali 虚拟机里运行。
- Windows 命令、窗口或厂商软件必须在 Windows 环境中完成。
- 报告只写最后采用的环境和步骤；无关的权限修复、试错过程留在工作记录中。

## 专业实践与涉密材料

真实工作材料可以帮助确定实践方向，但客户名称、内部地址、资产编号、告警详情、人员信息和原始截图不能进入公开报告。

需要演示相似工作时，应在本地隔离环境重新搭建普通场景，截图来自这次操作，并明确写成“本地复现”。不能把复现结果写成生产环境处置记录。

## 不会做的事

- 不生成或借用软件运行截图。
- 不把未执行的命令、代码或查询写成成功。
- 不对未授权主机做扫描、爆破或漏洞利用。
- 不替用户填写教师签名、成绩和审核意见。
- 不用仓库的通用草稿覆盖学校提供的 DOCX 模板。
- 不为了凑篇幅添加无关理论、调试记录或资料来源。

<details>
<summary>脚本与目录</summary>

```text
lab-report-autopilot/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── readme/
│   └── templates/
├── references/
│   ├── disciplines.md
│   ├── discipline-*.md
│   ├── environment-playbook.md
│   ├── evidence-and-screenshots.md
│   ├── confidential-work.md
│   ├── writing-and-code.md
│   └── docx-qa.md
├── scripts/
│   ├── init_report.py
│   ├── probe_environment.py
│   └── evidence_manifest.py
└── tests/
```

建立一个报告工作区：

```bash
python3 ~/.codex/skills/lab-report-autopilot/scripts/init_report.py \
  work/arp-report \
  --kind lab \
  --discipline packet-analysis \
  --title "ARP 协议抓包与字段分析"
```

检查当前环境：

```bash
python3 ~/.codex/skills/lab-report-autopilot/scripts/probe_environment.py --json
```

检查截图尺寸和重复文件：

```bash
python3 ~/.codex/skills/lab-report-autopilot/scripts/evidence_manifest.py \
  work/arp-report/evidence/original \
  --output work/arp-report/evidence-manifest.json
```

运行测试：

```bash
python3 -m unittest discover -s tests
```

</details>

## 许可

[MIT](LICENSE) · Copyright 2026 Flacier
