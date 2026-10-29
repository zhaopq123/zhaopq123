<div align="center">

# 你好，我是 zhaopq 👋

**用 AI 解决真问题** —— 白天跑无人零售设备 / 咖啡机外贸 / 软件定制，业余写 MCP 服务并开源

目标 **FDE（前沿部署工程师）**：把方案从「能演示」推到「客户现场真能用」

[![Profile views](https://komarev.com/ghpvc/?username=zhaopq123&color=blueviolet)](https://github.com/zhaopq123)
[![Email](https://img.shields.io/badge/Email-ethan.zhao.dev%40outlook.com-blue)](mailto:ethan.zhao.dev@outlook.com)
[![Gitee](https://img.shields.io/badge/Gitee-zhaopq-c71d23)](https://gitee.com/zhaopq)

**9 个开源项目** · 6 个 MCP 服务 · 全部 **MIT** · 4 个服务在生产 7×24 跑着

</div>

---

## 🚀 精选项目

<table>
<tr>
<td width="50%" valign="top">

### 🔍 websearch-mcp

**给 AI 的联网搜索服务**

不依赖任何商业搜索 API，不需要申请 Key —— 多引擎聚合 + 内置节点池自运维，一条命令装好就能用。

- 国内 9 引擎直连（1-2 秒）+ 国外引擎经代理
- **权威源优先**：官媒/政府/学术排前，内容农场压后
- **节点池自运维**：自动搜集、多站点可达性抽检、智能更新淘汰
- **代理是增强不是依赖**：代理挂了自动降级直连，抓取失败自动兜底
- 9 个 MCP 工具 + Web 管理面板 · 484 测试

[GitHub](https://github.com/zhaopq123/websearch-mcp) · [Gitee](https://gitee.com/zhaopq/websearch-mcp)

</td>
<td width="50%" valign="top">

### 🎨 mcp-imagegen

**图片 / 视频生成 MCP 服务器**

单上游、自带熔断与并发槽池，产物本地持久化。

- 文生图 / 图生图 / 文生视频 / 图生视频
- **代码生图 / 生视频**（本地渲染，不耗上游额度）
- 服务端代排队 + 智能退避
- 6 工具 · 713 测试

[GitHub](https://github.com/zhaopq123/mcp-imagegen) · [Gitee](https://gitee.com/zhaopq/mcp-imagegen)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🧠 shared-memory-mcp

**给 AI Agent 的共享记忆服务**

让 Agent 跨会话、跨机器记住项目结论 —— Markdown + git 存储，记忆可读、可 diff、可回滚。

- **库 = 权限边界，工作空间 = 项目分类**
- 9 个直觉动词工具（+7 旧名别名）· Web 管理面板
- 会话生命周期防串台 · 两段式读取省 59% token
- 581 测试 · 端到端自检脚本一条命令跑完

[GitHub](https://github.com/zhaopq123/shared-memory-mcp) · [Gitee](https://gitee.com/zhaopq/shared-memory-mcp)

</td>
<td width="50%" valign="top">

### 🖋️ webnovel-mcp

**长篇小说写作助手 MCP**

把「设定 / 伏笔 / 进度」从聊天上下文搬到磁盘：每章先取任务书，写完提交事实增量，随时能体检重放。

- 19 节创作提示词 · 按章装配任务书 + 状态防忘
- 章节提交链 + 伏笔台账 + 人物档案 + 节奏体检
- **九维审查**：一致性 / 信息隔离 / 文风 / AI 味 / 可选外部查重
- **老书可升级**：`doctor reconcile` 登记迁移基线，不丢手工设定
- **附带 WritingMaster 2.0 双套装**：13 命令 · 82 切片 · 29 模板 · 四大赛道（小说·含言情模式 / 剧本 / 剧本杀 / 工具书）· 655 条自测
- 26 工具 · 419 测试 · 零运行时依赖

[GitHub](https://github.com/zhaopq123/webnovel-mcp) · [Gitee](https://gitee.com/zhaopq/webnovel-mcp)

</td>
</tr>
</table>

> **这些不是 demo。** 生产环境常驻 6 个 MCP 服务（共享记忆、联网搜索、图像视频生成、网文写作、内容选题、图表设计），
> 部署在一台 **Android 手机**的 Termux + proot 容器里，runit 守护 7×24 在线 ——
> 都在真实业务里跑着，不在演示环境里。

---

## 📦 全部开源项目

<!-- SYNC:PROJECTS:START -->
| 项目 | 一句话 | 技术点 |
|---|---|---|
| **[phone-control-skill](https://github.com/zhaopq123/phone-control-skill)** | 给 AI Agent 的安卓手机控制技能 | UI 树按文字点击 · act 动作即验证 · batch 变量/条件/循环 · uiautomator2 快路 · Windows OCR 视觉兜底 · 多机并发 · 纯标准库（u2 可选） |
| **[shared-memory-mcp](https://github.com/zhaopq123/shared-memory-mcp)** | 给 AI Agent 的共享记忆服务 | Markdown+git 存储 · 多租户硬隔离 · 会话生命周期 · 9 工具（+7 别名）· 581 测试 |
| **[social-insight-mcp](https://github.com/zhaopq123/social-insight-mcp)** | 多平台内容选题分析 MCP | 10 源热点聚合 · 跨源交叉验证 · 账号定位匹配 |
| **[mcp-imagegen](https://github.com/zhaopq123/mcp-imagegen)** | 图片 / 视频生成 MCP 服务器 | 文生图/图生图 · 文生视频/图生视频 · 代码生图/生视频（本地渲染）· 服务端代排队 · 智能退避 · 6 工具 · 713 测试 |
| **[webnovel-mcp](https://github.com/zhaopq123/webnovel-mcp)** | 长篇网文写作助手 MCP | 任务书 + 章节提交链 + 伏笔台账 · 九维审查 · 断点恢复包 · 老书迁移基线 · 26 工具（含融合的 WritingMaster 13 个）· 19 节提示词 · 419 测试 |
| **[writing-master](https://github.com/zhaopq123/writing-master)** | 写作大师 Skill 套装 | 4 大赛道（长篇·含言情模式 / 剧本 / 剧本杀 / 工具书）· 13 命令 · 82 知识切片 · 29 交付模板 · 655 条自测 |
| **[diagram-design-mcp](https://github.com/zhaopq123/diagram-design-mcp)** | 编辑级图表设计系统 MCP | 45 类图表目录 · 8 工具 · 82 图标库 · 单文件 HTML+SVG 产物 · 扁平 schema |
| **[repo-template](https://github.com/zhaopq123/repo-template)** | 我的开源仓库模板 | README 骨架 · MIT · 通用 .gitignore |
| **[html](https://github.com/zhaopq123/html)** | 单文件 HTML 页面合集 | 零构建 · 零依赖 · 断网可开 · 配置卡 / 检查清单 / 汇报页 |
| **[websearch-mcp](https://github.com/zhaopq123/websearch-mcp)** | 给 AI 的联网搜索服务 | 多引擎直连与代理分流 · 节点池自运维 · 权威源分级 · 代理挂了自动降级直连 · 9 工具 · 484 测试 |

<!-- SYNC:PROJECTS:END -->

> 🇨🇳 以上项目在 **[Gitee](https://gitee.com/zhaopq)** 同步镜像（国内直连）
> ·每个仓库都带安装手册与真机自检脚本，克隆下来就能跑通，不用自己摸索。

---

## 🔭 在做的事

**业务线**

- 🥤 **无人零售设备** —— 咖啡机器人选型、销售与落地
- 🌍 **咖啡机外贸** —— 出口业务，客户覆盖哥伦比亚等地
- 💻 **软件定制开发** —— 从需求到交付
- 🏢 **企业数字化** —— 把纸质流程搬到线上，让数据真正流转

**技术线**

- 🤖 **MCP 服务开发** —— 共享记忆 / 联网搜索 / 图像与视频生成 / 图表设计 / 网文写作，全部开源
- ⚙️ **自托管** —— 生产服务跑在一台 Android 手机上的 Linux 容器里，runit 守护 7×24 在线
- 📝 **内容运营** —— 抖音「小赵聊软件」/ 小红书「小赵无人零售」

---

## 🤝 能一起做的事

- **业务侧 AI 落地** —— 把重复流程接成 Agent / 知识库 / 自动化，从需求到上线我一个人推到底
- **MCP 服务定制与私有部署** —— 上面这些自建服务可以当脚手架，也接受按你的业务改造
- **设备选型与外贸** —— 咖啡机 / 无人零售设备的选型、落地与出口

有具体场景想聊，发邮件或提 Issue 都行。

---

## 🛠 技术栈

| 层面 | 用的东西 |
|---|---|
| 语言 | `Python` `Node.js` `Shell` |
| AI 工程 | `MCP 协议` `FastMCP` `AI Agent 编排` `LLM API 集成` |
| 数据 | `SQLite` `Markdown + git 存储` |
| 部署运维 | `Docker` `runit / systemd` `Termux + proot` `反向代理` |
| 前端与产出 | `HTML/CSS` `HTMX` `SVG 代码渲染` `单文件产物` |

---

## 📮 联系我

- 📧 **ethan.zhao.dev@outlook.com**（优先）
- 📧 zhaopq999@163.com

---

<div align="center">

**擅长把合适的工具接起来、让它真的产出结果。**

相信「能跑起来」比「写得漂亮」更重要 —— 所以我的服务都在真实业务里跑着，不在 demo 里。

<sub>项目表随开源进度更新 · 最近更新 2026-10</sub>

</div>