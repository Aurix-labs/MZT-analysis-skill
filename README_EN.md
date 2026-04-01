# MZT - Mao Zedong Thought Dialectical Analysis Skill

An AI Agent skill based on Mao Zedong Thought methodology, enhancing dialectical thinking and decision-making capabilities.

[中文文档](README.md)

## Installation

Install using [Skills CLI](https://github.com/vercel-labs/skills):

```bash
# Install to current project
npx skills add your-github/mzt

# Global install for Claude Code
npx skills add your-github/mzt -g -a claude-code

# Global install for Cursor
npx skills add your-github/mzt -g -a cursor

# Install to all supported agents
npx skills add your-github/mzt -g --all
```

## Usage

### Commands

| Command | Description |
|---------|-------------|
| `/mzt` | Explicit analysis — Enter guided dialogue, output structured report |
| `/mzt-on` | Enable dialectical thinking mode — Agent automatically applies dialectical methods |
| `/mzt-off` | Disable dialectical thinking mode — Restore default thinking |

### Example

**Explicit invocation**:
```
User: /mzt I'm considering whether to join a startup company

Agent: Let me help you analyze this career decision...

[Enter guided dialogue, collect information, output structured report]
```

**Enable dialectical thinking mode**:
```
User: /mzt-on

Agent: Dialectical thinking mode enabled. I will apply Mao Zedong Thought methodologies in my reasoning process.
```

## Methodology System

MZT contains 16 methodologies organized in three layers:

### Foundation Layer

| Methodology | Core Principle | Use Case |
|-------------|----------------|----------|
| Contradiction Analysis | Primary vs secondary contradictions | Problem decomposition, prioritization |
| Seek Truth from Facts | Start from reality, oppose subjectivism | Diagnosis, evaluation |
| Practice Cycle | Perception → Reasoning → Practice testing | Validation, iteration |
| Development Dialectics | Small-to-large transformation, long-term vision | Trend assessment, potential evaluation |

### Diagnosis Layer

| Methodology | Core Principle | Use Case |
|-------------|----------------|----------|
| Class Stance Analysis | Interests determine positions | Stakeholder analysis, negotiation |
| Investigation Research | No investigation, no right to speak | Information gathering, diagnosis |
| Thought Correction | Identify → Analyze → Correct | Problem diagnosis, team building |
| Contradiction Classification | Enemy vs internal contradictions | Conflict resolution, classification |

### Execution Layer

| Methodology | Core Principle | Use Case |
|-------------|----------------|----------|
| Strategic Dialectics | Strong-weak transformation, protracted war | Long-term planning, competitive strategy |
| Flexible Strategy | Preserve self, defeat enemy | Resource-constrained scenarios |
| Focus Breakthrough | Concentrate resources, key breakthrough | Resource allocation, prioritization |
| Overall Coordination | Balance ten major relationships | System design, resource balancing |
| Mass Line | From the masses, to the masses | Requirement analysis, user research |
| Organizational Discipline | Principles over personal relations | Team collaboration, culture building |
| Persistence | Firm belief, sustained effort | Long-term goals, difficult tasks |
| Purpose Orientation | Fundamental purpose, value guidance | Mission, vision, meaning |

## Structured Report Sections

When explicitly invoked (`/mzt`), the output includes:

1. **Problem Definition** — Core issue to be resolved
2. **Contradiction Analysis** — Primary and secondary contradictions
3. **Objective Conditions** — Current environment and constraints
4. **Solutions** — Proposed solutions based on analysis
5. **Practice Verification** — How to validate and iterate solutions

## Supported Agents

Through Skills CLI, MZT supports 44+ AI agents including:

- Claude Code
- Cursor
- OpenClaw
- Codex
- Windsurf
- Cline
- Goose
- And more

## References

- [Selected Works of Mao Zedong](https://www.marxists.org/chinese/maozedong/index.htm)
- [Agent Skills Specification](https://agentskills.io)
- [Skills CLI](https://github.com/vercel-labs/skills)

## License

MIT
