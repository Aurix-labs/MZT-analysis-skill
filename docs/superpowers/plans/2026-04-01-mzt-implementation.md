# MZT 实现计划

## 概述

基于设计文档 `docs/superpowers/specs/2026-04-01-mzt-design.md`，实现毛泽东思想辩证分析 Skill。

## 任务列表

| # | 任务 | 依赖 | 状态 |
|---|------|------|------|
| 1 | 创建项目基础结构 | - | pending |
| 2 | 编写 SKILL.md 核心文件 | #1 | pending |
| 3 | 编写核心哲学层方法论（4个） | #1 | pending |
| 4 | 编写分析诊断层方法论（4个） | #1 | pending |
| 5 | 编写策略执行层方法论（8个） | #1 | pending |
| 6 | 编写 README.md | #2-5 | pending |
| 7 | 提交并发布 | #6 | pending |

## 详细步骤

### 任务 1: 创建项目基础结构

**目标**: 创建项目目录结构

**步骤**:
1. 创建 `methodologies/` 目录
2. 创建空的占位文件

**产出**:
```
mzt/
├── docs/
│   └── superpowers/
│       ├── specs/
│       │   └── 2026-04-01-mzt-design.md (已存在)
│       └── plans/
│           └── 2026-04-01-mzt-implementation.md (本文件)
├── methodologies/
│   └── .gitkeep
└── .git/ (已存在)
```

---

### 任务 2: 编写 SKILL.md 核心文件

**目标**: 创建遵循 Agent Skills 规范的核心 skill 文件

**规范要求**:
- YAML frontmatter 包含 `name` 和 `description`
- 包含指令定义
- 包含方法论索引（引用 methodologies/ 目录）
- 包含使用流程说明

**产出**: `SKILL.md`

---

### 任务 3: 编写核心哲学层方法论（4个）

**目标**: 编写核心哲学层的 4 个方法论文件

**文件列表**:
1. `methodologies/01-contradiction-analysis.md` - 矛盾分析法
2. `methodologies/02-seek-truth-from-facts.md` - 实事求是法
3. `methodologies/03-practice-cycle.md` - 认识循环法
4. `methodologies/04-development-dialectics.md` - 发展辩证法

**每个文件结构**:
```markdown
# [方法论名称]

## 核心原则
## 分析框架
## 应用示例
## 详细指导
## 经典语录
```

**字数要求**: 每个 1000-1500 字

---

### 任务 4: 编写分析诊断层方法论（4个）

**目标**: 编写分析诊断层的 4 个方法论文件

**文件列表**:
1. `methodologies/05-class-stance-analysis.md` - 阶级立场分析法
2. `methodologies/06-investigation-research.md` - 调查研究法
3. `methodologies/07-thought-correction.md` - 思想纠偏法
4. `methodologies/08-contradiction-classification.md` - 矛盾分类处理法

---

### 任务 5: 编写策略执行层方法论（8个）

**目标**: 编写策略执行层的 8 个方法论文件

**文件列表**:
1. `methodologies/09-strategic-dialectics.md` - 战略辩证法
2. `methodologies/10-flexible-strategy.md` - 灵活战略法
3. `methodologies/11-focus-breakthrough.md` - 聚焦突破法
4. `methodologies/12-overall-coordination.md` - 统筹兼顾法
5. `methodologies/13-mass-line.md` - 群众路线法
6. `methodologies/14-organizational-discipline.md` - 组织纪律法
7. `methodologies/15-persistence.md` - 持之以恒法
8. `methodologies/16-purpose-orientation.md` - 宗旨导向法

---

### 任务 6: 编写 README.md

**目标**: 创建项目说明文档

**内容**:
- 项目简介
- 安装方式（npx skills add）
- 使用说明（指令列表）
- 方法论概览
- 参考资源

---

### 任务 7: 提交并发布

**目标**: 提交所有文件到 Git，准备发布

**步骤**:
1. Git add 所有新文件
2. Git commit
3. 确认文件结构正确

---

## 验收标准

- [ ] 项目结构完整
- [ ] SKILL.md 符合 Agent Skills 规范
- [ ] 16 个方法论文件内容完整
- [ ] README.md 清晰说明安装和使用
- [ ] 所有文件已提交到 Git

---

## 风险与缓解

| 风险 | 缓解措施 |
|------|----------|
| 方法论内容深度不足 | 参考毛选原文，确保理论准确性 |
| Agent Skills 规范变更 | 查阅最新规范文档 |
| 跨平台兼容性问题 | 使用 Skills CLI 测试安装 |
