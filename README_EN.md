<p align="center">
  <img src="assets/readme/mao-flag.png" alt="A red flag and a black-and-white silhouette of Mao Zedong" width="280">
</p>

<h1 align="center">MZT</h1>

<p align="center">
  <strong>Mao Zedong Thought · Dialectical Thinking Skill</strong><br>
  Help AI start from concrete facts and make judgments that can be tested.
</p>

<p align="center">
  <a href="README.md">中文</a> · <strong>English</strong>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#core-ideas">Core ideas</a> ·
  <a href="#a-concrete-example">In practice</a> ·
  <a href="#evaluating-mzt">Evaluation</a>
</p>

<p align="center">
  <strong>23</strong> method references &nbsp; / &nbsp;
  <strong>17</strong> evaluation scenarios &nbsp; / &nbsp;
  Expression shaped by the task
</p>

---

> **No investigation, no right to speak.**<br>
> —[Oppose Book Worship](毛泽东选集/第一卷-第二次国内革命战争时期/反对本本主义.md)

MZT draws on the **standpoints, perspectives, and methods** of Mao Zedong Thought to guide an AI agent's judgment: investigate how events unfolded, understand contradictions through concrete relationships, examine the interests behind proposals, and revise conclusions in response to new evidence and practical results.

What matters is whether the agent understands the actual problem and can support its choices. The task determines the answer's length and form: a sentence, a table, a piece of code, or a detailed argument. The skill prescribes no answer sections, method quotas, or fixed internal steps.

## Quick start

Install with [Skills CLI](https://github.com/vercel-labs/skills), then follow the prompts to select your agent:

```bash
npx skills add Aurix-labs/MZT-analysis-skill --skill mzt
```

<details>
<summary><strong>Install globally or use a locally edited version</strong></summary>

Install globally for a specific agent:

```bash
# Codex
npx skills add Aurix-labs/MZT-analysis-skill --skill mzt -g -a codex

# Claude Code
npx skills add Aurix-labs/MZT-analysis-skill --skill mzt -g -a claude-code
```

Install the local version from the repository root:

```bash
npx skills add ./mzt --skill mzt
```

The remote commands install content published to the repository. Local edits do not automatically update the remote repository or copies already installed elsewhere. See the [Skills CLI documentation](https://github.com/vercel-labs/skills#install-a-skill) for more options.

</details>

After installation, give your agent a concrete question:

```text
/mzt Analyze the dispute prompted by this draft policy.

/mzt Who benefits from this rule change, and who bears the costs?

/mzt Our team's delivery is getting slower. Where should we start?
```

| Invocation | Meaning |
| :--- | :--- |
| `/mzt [question]` | Apply relevant ideas to the current task |
| `/mzt on` | Continue applying relevant ideas throughout this conversation |
| `/mzt off` | Stop continuous guidance; one-off invocation remains available |

The host agent interprets `on/off` as a convention within the current conversation. New conversations do not inherit that state. It is not a background switch and does not change model weights; the exact invocation interface depends on the host.

## Core ideas

These ideas are connected and can be revisited as understanding develops. The investigation and evidence needed to support a judgment remain essential.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Investigation</h3>
      <p>Trace the underlying problem, historical context, original claims, and relevant later developments. Check whether retelling has changed the issue under dispute.</p>
      <a href="mzt/methodologies/06-investigation-research.md">Understand how the issue arose →</a>
    </td>
    <td width="50%" valign="top">
      <h3>Seek truth from facts</h3>
      <p>Distinguish facts, inferences, and assumptions. Let evidence constrain the explanation, including evidence that challenges the initial judgment.</p>
      <a href="mzt/methodologies/02-seek-truth-from-facts.md">Ground understanding in reality →</a>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h3>Contradiction analysis</h3>
      <p>Examine mutual dependence and constraint. Identify decisive relationships and distinguish the principal contradiction from the principal aspect within a contradiction.</p>
      <a href="mzt/methodologies/01-contradiction-analysis.md">Find what shapes the wider situation →</a>
    </td>
    <td valign="top">
      <h3>Standpoints and interests</h3>
      <p>Investigate economic position, organizational ties, and resource dependence. Distinguish claims to represent others from institutional effects and personal motives.</p>
      <a href="mzt/methodologies/05-class-stance-analysis.md">Place claims in their material context →</a>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h3>The mass line</h3>
      <p>Recognize different circumstances within “ordinary people.” Draw on participants' experience to assess a proposal's opportunities, burdens, and consequences.</p>
      <a href="mzt/methodologies/13-mass-line.md">Start with the people affected →</a>
    </td>
    <td valign="top">
      <h3>Development and practice</h3>
      <p>Examine how conditions change and how actions reshape relationships. Use actual results to revise understanding and subsequent choices.</p>
      <a href="mzt/methodologies/03-practice-cycle.md">Test judgments through practice →</a>
    </td>
  </tr>
</table>

Read [SKILL.md](mzt/SKILL.md) for the full guidance, or consult the [23-method reference index](mzt/methodologies/INDEX.md) when a particular question needs closer examination.

## A concrete example

**A dispute over “pausing digital procurement” may begin with a decision about how to cut a public-service budget.**

In a fictional evaluation scenario, a library plans to shorten opening hours at its township branches. A reader proposes postponing a new digital-system purchase instead. A critic accuses the reader of depriving township residents of digital services.

Reading the budget proposal and the complete statement reveals that the new system is a different project from the existing catalogue search and online renewal services. The reader explicitly wants to preserve those services. Discussing only whether digital technology has value would miss the actual comparison between procurement and branch opening hours.

Further judgment depends on concrete circumstances: who relies on evening and weekend access, what needs the new features address, whether the savings estimates hold up, and what later arrangements have actually changed. New evidence should change the judgment where relevant. A temporary procurement pause is not proof of long-term results.

[Read the full scenario](mzt/evals/fixtures/15-library/index.md) · [More examples of the ideas in use](mzt/references/thought-in-use.md)

These examples illustrate how the ideas can change a judgment. They are not answers to reproduce.

## Evaluating MZT

**Look at what the agent investigated, what supports its judgment, and whether changed evidence changes its conclusions.**

The current set contains **17 scenarios**, including **3 multi-turn tasks**. They cover event investigation, interest analysis, organizational decisions, historical explanations, code, tables, brief answers, and conversation commands.

| What to evaluate | Observable behavior |
| :--- | :--- |
| Active investigation | Reads available background and original materials to recover the problem omitted from a dispute fragment |
| Identifying the issue | Distinguishes original claims, other people's retellings, and predicted consequences |
| Analyzing interests | Uses verified economic ties and effects on different groups, addressing real conflicts without attributing motives through rumors |
| Revising judgment | Accepts later clarification and counterevidence, updates affected conclusions, and retains what still holds |
| Serving the task | Completes simple tasks directly, explains complex ones adequately, and respects the user's requested format |

Coverage does not mean every scenario has passed, nor does it demonstrate reliable capability gains. Automated scripts measure only specified text properties and format constraints. Facts, causal explanations, and sources require review against the available material. Evaluation neither requests nor scores hidden chains of thought.

[Evaluation scenarios](mzt/evals/evals.json) · [Rubric and evaluation protocol](mzt/evals/rubric.md)

## Further reading and contributions

<details>
<summary><strong>Repository structure</strong></summary>

| Path | Contents |
| :--- | :--- |
| [mzt/SKILL.md](mzt/SKILL.md) | Skill entrypoint and invocation conventions |
| [mzt/methodologies/](mzt/methodologies/) | 23 method references and their index |
| [mzt/references/](mzt/references/) | Guidance on evidence, dialogue, citation, and application |
| [mzt/configs/](mzt/configs/) | Optional reading suggestions and case-recording guidance |
| [mzt/cases/](mzt/cases/) | Index of cases recorded at the user's request |
| [mzt/evals/](mzt/evals/) | Scenarios, fictional source materials, review criteria, and measurement scripts |
| [毛泽东选集/](毛泽东选集/) | Original source and study materials |
| [assets/readme/](assets/readme/) | README images |

</details>

Concrete failure cases are welcome through [Issues](https://github.com/Aurix-labs/MZT-analysis-skill/issues): include the original task, available materials, the agent's actual response, and where its judgment departed from the facts. Improvements should address judgment quality, rather than add terminology or lengthen reports.

The methods originate in Mao Zedong Thought; modern applications must account for their specific circumstances. Preserve historical context, verify quotations, and avoid treating classical authority as a substitute for evidence or assigning historical friend-or-enemy categories directly to modern people and organizations.

[Selected Works of Mao Zedong online](https://www.marxists.org/chinese/maozedong/index.htm) · [Agent Skills specification](https://agentskills.io) · [Citation and expression guidance](mzt/references/style-and-mindset.md)

---

<p align="center">
  <strong>Start from reality. Test through practice.</strong><br>
  MZT · MIT
</p>
