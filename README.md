<p align="center">
  <img src="assets/readme/mao-flag.png" alt="红旗与毛泽东黑白剪影" width="280">
</p>

<h1 align="center">MZT · 毛泽东思想与方法</h1>

<p align="center">
  以毛泽东思想的立场、观点和方法，帮助用户检验固有认识、看清问题并选择行动。<br>
  <strong>从实际出发，在实践中检验。</strong>
</p>

<p align="center">
  <strong>中文</strong> · <a href="README_EN.md">English</a>
</p>

<p align="center">
  <a href="#快速开始">快速开始</a> ·
  <a href="#思想内核">思想内核</a> ·
  <a href="#放到一个具体问题里">实际例子</a>
</p>

<p align="center">
  <strong>23</strong> 个方法论参考 &nbsp; / &nbsp;
  按任务自然表达
</p>

---

MZT 将毛泽东思想中的**立场、观点与方法**整理为 AI 可以运用的方法论，帮助用户跳出主观假定和固有思维：检验问题前提，查清事情的来龙去脉，在具体关系中理解矛盾，调查主张背后的利益联系，并让新证据和实践结果修正判断。

客观分析要求对用户、相关各方及 AI 自己采用一致的证据标准，同时讲明价值取舍。用户原判断有依据，就明确支持；需要决策时，结合目标、资源、成本和风险比较可行路径，提出当前条件下最合适的方案。

它关心的是有没有看清原先忽略的东西，并据此作出更好的决定。答案的篇幅和形式由任务决定：可以是一句判断、一张表、一段代码，也可以是充分展开的论证。技能不规定回答栏目、方法配额或固定的内部步骤。

## 快速开始

使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装，按提示选择使用的 Agent：

```bash
npx skills add Aurix-labs/MZT-analysis-skill --skill mzt
```

<details>
<summary><strong>全局安装，或使用本地修改版</strong></summary>

全局安装到指定 Agent：

```bash
# Codex
npx skills add Aurix-labs/MZT-analysis-skill --skill mzt -g -a codex

# Claude Code
npx skills add Aurix-labs/MZT-analysis-skill --skill mzt -g -a claude-code
```

在仓库根目录安装本地版本：

```bash
npx skills add ./mzt --skill mzt
```

远程命令安装仓库已发布的内容；本地修改不会自动更新远程仓库或已经复制安装的副本。更多安装选项见 [Skills CLI 文档](https://github.com/vercel-labs/skills#install-a-skill)。

</details>

安装后，在 Agent 中提出具体问题：

```text
/mzt 分析这份政策草案引发的争论。

/mzt 这项规则调整会让谁受益，成本又由谁承担？

/mzt 团队交付越来越慢，应该从哪里着手？
```

| 调用 | 含义 |
| :--- | :--- |
| `/mzt [问题]` | 将相关思想用于当前任务 |
| `/mzt on` | 在当前会话持续运用相关思想 |
| `/mzt off` | 停止持续引导，之后仍可单次调用 |

`on/off` 是由宿主 Agent 理解的会话约定，新会话不继承状态。它不是后台开关，也不会修改模型权重；具体调用入口以宿主支持的方式为准。

## 思想内核

<p align="center">
  <img src="assets/readme/investigation-quote.png" alt="没有调查，没有发言权。木刻风插画：毛泽东在桌前听取乡亲意见、记录调查材料" width="100%">
</p>

<p align="center">
  <strong>“没有调查，没有发言权。”</strong><br>
  ——毛泽东，<a href="毛泽东选集/第一卷-第二次国内革命战争时期/反对本本主义.md">《反对本本主义》</a>，1930 年
</p>

这些思想可以相互联系、往返运用。形成判断所必需的调查和证据始终不能省略。

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>调查研究</h3>
      <p>追查现实问题、历史背景、原始主张和关键后续。辨明争议对象是否在传播中被改写。</p>
      <a href="mzt/methodologies/06-investigation-research.md">从事情的来龙去脉开始 →</a>
    </td>
    <td width="50%" valign="top">
      <h3>实事求是</h3>
      <p>区分事实、推断与假设。让材料约束解释，也让不利于原有判断的证据进入分析。</p>
      <a href="mzt/methodologies/02-seek-truth-from-facts.md">让认识服从实际 →</a>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h3>矛盾分析</h3>
      <p>理解相互依存与制约，辨别决定当前局面的关系，分清主要矛盾与矛盾的主要方面。</p>
      <a href="mzt/methodologies/01-contradiction-analysis.md">找到牵动全局的关系 →</a>
    </td>
    <td valign="top">
      <h3>立场与利益</h3>
      <p>主动调查经济地位、组织联系和资源依赖。分清自我代言、制度效果与个人动机。</p>
      <a href="mzt/methodologies/05-class-stance-analysis.md">把主张放回物质关系 →</a>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h3>群众路线</h3>
      <p>看见“普通人”内部不同的处境，让实际参与者的经验检验方案的机会、负担和后果。</p>
      <a href="mzt/methodologies/13-mass-line.md">从受影响者的处境出发 →</a>
    </td>
    <td valign="top">
      <h3>发展与实践</h3>
      <p>考察条件怎样变化，行动怎样改变关系，并依据实际结果修正认识和下一步选择。</p>
      <a href="mzt/methodologies/03-practice-cycle.md">让判断接受实践检验 →</a>
    </td>
  </tr>
</table>

完整指导见 [SKILL.md](mzt/SKILL.md)；需要深入某个问题时，查阅 [23 个方法论索引](mzt/methodologies/INDEX.md)。

## 放到一个具体问题里

**一场关于“暂停数字化采购”的争论，起因可能是公共服务预算如何压减。**

以一个虚构的图书馆案例为例：图书馆准备缩短乡镇分馆开放时间。一位读者提出先暂缓新增数字系统采购，对手却批评他让乡镇居民失去数字服务。

查阅预算草案和完整发言后，会发现新增系统与既有目录查询、网上续借属于不同项目。读者明确主张保留后者。此时，仅讨论“数字化有没有价值”，就漏掉了真正需要比较的采购与开放服务。

进一步的判断要落到具体处境：哪些人依赖晚间和周末开放，新增功能解决什么需求，节支估算是否成立，后续安排实际改变了什么。材料改变了，就要调整判断；不能把暂缓采购写成长期效果已经得到验证。

[阅读完整案例](mzt/evals/fixtures/15-library/index.md) · [更多思考示意](mzt/references/thought-in-use.md)

这些例子展示思想怎样改变判断，不提供需要照搬的答案。

> **你要知道梨子的滋味，你就得变革梨子，亲口吃一吃。**<br>
> ——毛泽东，[《实践论》](毛泽东选集/第一卷-第二次国内革命战争时期/实践论.md)，1937 年

## 继续阅读与参与

<details>
<summary><strong>项目目录</strong></summary>

| 路径 | 内容 |
| :--- | :--- |
| [mzt/SKILL.md](mzt/SKILL.md) | 技能入口与调用约定 |
| [mzt/methodologies/](mzt/methodologies/) | 23 篇方法论参考及索引 |
| [mzt/references/](mzt/references/) | 证据、对话、引用和应用说明 |
| [mzt/configs/](mzt/configs/) | 可选阅读线索与案例记录说明 |
| [mzt/cases/](mzt/cases/) | 按用户请求整理的案例索引 |
| [毛泽东选集/](毛泽东选集/) | 思想来源与原文学习资料 |
| [assets/readme/](assets/readme/) | README 图片资源 |

</details>

欢迎通过 [Issue](https://github.com/Aurix-labs/MZT-analysis-skill/issues) 提供具体失败案例：原始任务、可取得的材料、AI 的实际回答，以及判断在哪一步偏离了事实。改进应落实到判断质量，而非增加术语或报告长度。

方法来自毛泽东思想，现代应用需要结合具体条件。保留历史语境，核对引用，不以经典权威替代事实，也不把历史敌友身份直接套给现代个人与组织。

[毛泽东选集在线版](https://www.marxists.org/chinese/maozedong/index.htm) · [Agent Skills 规范](https://agentskills.io) · [引用与表达说明](mzt/references/style-and-mindset.md) · [配图与引文说明](assets/readme/ARTWORK.md)

---

<p align="center">
  <img src="assets/readme/spark-quote.png" alt="星星之火，可以燎原。木刻风题图：油灯、书卷、红旗与田野" width="100%">
</p>
