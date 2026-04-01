# MZT - Mao Zedong Thought Dialectical Analysis Skill

An AI Agent skill based on Mao Zedong Thought methodology, enhancing dialectical thinking and decision-making capabilities.

[中文文档](README.md)

## Installation

Install using [Skills CLI](https://github.com/vercel-labs/skills):

```bash
# Install to current project
npx skills add Aurix-labs/MZT

# Global install for Claude Code
npx skills add Aurix-labs/MZT -g -a claude-code

# Global install for Cursor
npx skills add Aurix-labs/MZT -g -a cursor

# Install to all supported agents
npx skills add Aurix-labs/MZT -g --all
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

## Classic Quotes from Mao Zedong

### On Contradiction Analysis

> In the course of developing a complex thing, many contradictions exist, and one of them is necessarily the principal contradiction, whose existence and development determine the existence and development of other contradictions.

> Of the two contradictory aspects, one must be principal and the other secondary.

> Qualitatively different contradictions can only be resolved by qualitatively different methods.

### On Seeking Truth from Facts

> "Facts" are all the things that exist objectively, "truth" means the internal relations of objective things, and "to seek" means to study.

> No investigation, no right to speak.

> All conclusions are born at the end of the investigation, not at its beginning.

### On Practice and Knowledge

> Through practice, discover truth, and through practice, verify and develop truth.

> Practice, knowledge, practice again, knowledge again—this form repeats itself in endless cycles, and with each cycle, the content of practice and knowledge rises to a higher level.

### On Development Strategy

> A single spark can start a prairie fire.

> It is like a ship far out at sea whose masthead can already be seen from the shore; it is like the morning sun in the east whose shimmering rays are visible from a high mountain top; it is like a child about to be born moving restlessly in its mother's womb.

> The object of war is not simply to annihilate the enemy but to preserve oneself while annihilating the enemy.

### On Mass Line

> What is a true iron wall? It is the masses, the millions upon millions who genuinely support the revolution.

> From the masses, to the masses.

> All the practical problems of the masses are problems we should pay attention to.

### On Stance Analysis

> Who are our enemies? Who are our friends? This is a question of the first importance for the revolution.

> A revolutionary party is the guide of the masses, and no revolution ever fails when the party leads correctly.

### On Working Methods

> The method of concentrating superior forces and destroying the enemy one by one must be applied not only in the disposition of campaigns but also in the disposition of battles.

> We must be determined, fear no sacrifice, surmount every difficulty, and win victory.

### On Purpose and Belief

> Our Communist Party and the Eighth Route and New Fourth Armies led by our Party are revolutionary armies. They are entirely for the liberation of the people and work thoroughly for the interests of the people.

> To die for the people's interests is weightier than Mount Tai; to die for the fascists and for the exploiters and oppressors of the people is lighter than a feather.

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
