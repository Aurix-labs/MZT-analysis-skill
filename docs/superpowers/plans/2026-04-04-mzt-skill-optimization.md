# MZT Skill 优化实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 实施 MZT skill 的 6 项改进，解决形式主义、调查研究缺失、矛盾转化分析不足等问题

**Architecture:** 采用依赖优先策略，先更新方法论文件，再重构 SKILL.md，最后验证

**Tech Stack:** Markdown 文件编辑，无代码依赖

---

## 文件结构

| 文件 | 改动类型 | 说明 |
|------|----------|------|
| `mzt/methodologies/01-contradiction-analysis.md` | 修改 | 新增"矛盾转化条件"章节 |
| `mzt/methodologies/05-class-stance-analysis.md` | 修改 | 删除旧章节，新增"适用边界"章节 |
| `mzt/SKILL.md` | 重构 | 扩展报告章节、新增多个指南章节 |

---

## Task 1: 更新矛盾分析法文件（P0）

**Files:**
- Modify: `mzt/methodologies/01-contradiction-analysis.md`

- [ ] **Step 1: 在"步骤三"之后插入新的"步骤四"章节**

**插入位置**: 在第 62 行（步骤三结束）之后，第 64 行（原步骤四）之前

**要插入的内容**:

```markdown
### 步骤四：分析矛盾转化条件

矛盾双方在一定条件下会相互转化，这是辩证法的精髓。

**必须回答的问题**：

1. **转化方向**：矛盾可能向哪个方向转化？
2. **转化条件**：转化需要什么条件？
3. **当前进度**：哪些条件已经具备？哪些还在形成中？
4. **临界点**：转化的临界点在哪里？
5. **推动力量**：哪些因素在推动转化？
6. **阻碍力量**：哪些因素在阻碍转化？

**转化条件分析模板**：

| 转化方向 | 关键条件 | 当前进度 | 预计时间 |
|----------|----------|----------|----------|
| 方向A | 条件1、条件2、条件3 | 条件1已具备 | ? |
| 方向B | 条件1、条件2、条件3 | 条件1初步形成 | ? |

**经典引用**：

> 矛盾的主要和非主要的方面互相转化着，事物的性质也就随着起变化。

**应用示例**：

以中美博弈为例：

| 转化方向 | 关键条件 | 当前进度 |
|----------|----------|----------|
| 美国由强转弱 | 1.内部矛盾激化 2.霸权成本透支 3.盟友体系松动 | 条件1发展中，条件2已显现，条件3初步迹象 |
| 中国由弱变强 | 1.科技自立自强 2.内循环畅通 3.国际支持扩大 | 条件1进行中，条件2初步建立，条件3稳步推进 |

```

- [ ] **Step 2: 重命名原"步骤四"为"步骤五"**

将第 64 行的 `### 步骤四：寻找解决方案` 改为 `### 步骤五：寻找解决方案`

- [ ] **Step 3: 验证文件结构**

确保文件结构为:
- 步骤一：识别矛盾
- 步骤二：区分主次
- 步骤三：分析矛盾的主要方面
- 步骤四：分析矛盾转化条件（新增）
- 步骤五：寻找解决方案（原步骤四）

- [ ] **Step 4: 提交更改**

```bash
git add mzt/methodologies/01-contradiction-analysis.md
git commit -m "feat(mzt): add contradiction transformation analysis step

- Add new Step 4: Analyze contradiction transformation conditions
- Rename original Step 4 to Step 5
- Include template and example for transformation analysis

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 2: 更新阶级立场分析法文件（P2）

**Files:**
- Modify: `mzt/methodologies/05-class-stance-analysis.md`

- [ ] **Step 1: 删除原有的"适用场景"章节**

删除第 16-23 行的内容（从 `### 适用场景` 到 `- 项目推进，需要争取支持` 及其下空行）:

```markdown
### 适用场景

- 利益冲突分析，需要识别各方立场
- 谈判博弈，需要了解对方诉求
- 市场竞争，需要分析竞争格局
- 团队管理，需要协调各方利益
- 项目推进，需要争取支持

```

- [ ] **Step 2: 在"详细指导"之后插入"适用边界"章节**

**插入位置**: 在第 149 行（"与其他方法论的配合"章节最后一行）之后，第 151 行（分隔线 `---`）之前

**要插入的内容**:

```markdown
---

## 适用边界

### 适用场景

- 社会矛盾分析
- 利益集团博弈
- 历史事件分析
- 资源分配冲突

### 需要变通的场景

| 场景 | 变通方式 |
|------|----------|
| **科技发展** | 不用传统"阶级"框架，改用"利益相关方"分析，注意内部分化 |
| **国际关系** | 国家利益可能超越阶级利益，需综合考虑 |
| **生态问题** | 全人类共同利益可能超越阶级分歧 |

### 不适用场景

- 纯技术问题（如代码优化）
- 自然科学问题
- 个人心理健康问题

### 科技发展的特殊处理

分析科技发展问题时，"阶级立场"需要变通：

**变通方式**：将"阶级"替换为"利益相关方类型"，并注意内部的复杂分化。

**示例：AI发展的利益相关方分析**

| 利益相关方 | 内部分化 | 不同立场 |
|------------|----------|----------|
| 科技公司 | 大模型厂商 vs 应用厂商 | 对监管态度不同 |
| 劳动者 | 高技能 vs 低技能 | 对AI态度不同 |
| 国家 | AI领先国 vs 落后国 | 对治理态度不同 |

```

- [ ] **Step 3: 验证文件结构**

确保:
- 删除了原有的"适用场景"章节
- 新增的"适用边界"章节位于"详细指导"之后、"经典语录"之前

- [ ] **Step 4: 提交更改**

```bash
git add mzt/methodologies/05-class-stance-analysis.md
git commit -m "feat(mzt): add applicability boundaries for class stance analysis

- Remove original '适用场景' section (lines 16-23)
- Add comprehensive '适用边界' section after '详细指导'
- Include变通 scenarios, 不适用 scenarios, and AI example

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 3: 重构 SKILL.md - 报告章节结构（P0）

**Files:**
- Modify: `mzt/SKILL.md`

- [ ] **Step 1: 扩展"结构化报告章节"**

将原有的 5 个章节扩展为 7 个章节。

**找到** (约第 65-73 行):
```markdown
### 结构化报告章节

当用户使用 `/mzt` 显式调用时，输出包含以下章节：

1. **问题定义** — 明确要解决的核心问题
2. **矛盾分析** — 主要矛盾、次要矛盾、矛盾的主要方面
3. **客观条件** — 当前环境和约束条件
4. **解决方案** — 基于分析提出的方案
5. **实践检验** — 如何验证和迭代方案
```

**替换为**:
```markdown
### 结构化报告章节

当用户使用 `/mzt` 显式调用时，输出包含以下章节：

1. **问题定义** — 明确要解决的核心问题（收敛、精准）
2. **事实依据** — 数据来源、调研过程、信息可靠性（强制要求）
3. **矛盾分析** — 主要矛盾、次要矛盾、矛盾的主要方面、转化条件
4. **客观条件** — 当前环境和约束条件
5. **解决方案** — 基于分析提出的方案
6. **实践检验** — 如何验证和迭代方案
7. **批判性反思** — 自我质疑、局限性、改进方向（强制要求）

#### 事实依据章节模板

```markdown
## 二、事实依据

### 数据来源

| 来源类型 | 具体来源 | 链接/出处 |
|----------|----------|----------|
| 官方数据 | ? | ? |
| 研究报告 | ? | ? |
| 新闻报道 | ? | ? |
| 专家观点 | ? | ? |

### 可靠性评估

- [ ] 数据是否来自权威渠道？
- [ ] 是否存在利益相关方影响？
- [ ] 是否需要交叉验证？

### 信息缺口

- 哪些关键信息尚未获取？
- 如何弥补这些缺口？
```

#### 批判性反思章节模板

```markdown
## 七、批判性反思

### 核心假设
- 本报告的核心假设是什么？
- 这些假设是否经得起检验？

### 可能的反驳
- 有没有其他可能的解释？
- 反对者会怎么反驳我的结论？

### 局限性
- 本报告最大的局限是什么？
- 什么情况下本报告的结论会失效？

### 改进方向
- 还需要补充哪些信息？
- 分析还可以从哪些角度深化？
```
```

- [ ] **Step 2: 提交更改**

```bash
git add mzt/SKILL.md
git commit -m "feat(mzt): expand report sections from 5 to 7

- Add '事实依据' as mandatory section 2
- Add '批判性反思' as mandatory section 7
- Include templates for both new sections

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 4: 重构 SKILL.md - 方法论选择指南（P1）

**Files:**
- Modify: `mzt/SKILL.md`

- [ ] **Step 1: 在"方法论间的辩证关系"章节之后插入新章节**

**插入位置**: 在第 177 行（方法论组合使用表格结束）之后

**要插入的内容**:

```markdown

---

## 方法论选择指南

### 选择原则

1. **宁精勿多**：一个报告聚焦 2-3 个核心方法论
2. **问题导向**：根据问题类型选择方法论
3. **逻辑递进**：方法论之间要有逻辑关系

### 问题类型与方法论选择矩阵

| 问题类型 | 必选方法论 | 可选方法论 | 不推荐/需谨慎 |
|----------|------------|------------|---------------|
| **历史事件** | 矛盾分析+发展辩证 | 阶级立场、群众路线 | - |
| **国际博弈** | 矛盾分析+战略辩证 | 统一战线、独立自主 | 阶级立场（需变通） |
| **科技发展** | 矛盾分析+发展辩证 | 群众路线、实事求是 | 阶级立场（需变通） |
| **社会问题** | 矛盾分析+阶级立场 | 群众路线、独立自主 | - |
| **职业决策** | 矛盾分析+独立自主 | 发展辩证、实事求是 | 阶级立场 |
| **组织变革** | 矛盾分析+群众路线 | 思想纠偏、组织纪律 | 战略辩证 |

### 方法论组合逻辑

方法论不是孤立使用的，它们之间应该形成逻辑链条：

**示例 1：历史事件分析**
```
调查研究法 → 获取事实
    ↓
矛盾分析法 → 识别核心矛盾
    ↓
阶级立场分析法 → 分析各方利益
    ↓
发展辩证法 → 判断历史走向
```

**示例 2：国际博弈分析**
```
实事求是法 → 认清客观形势
    ↓
矛盾分析法 → 找到主要矛盾
    ↓
战略辩证法 → 判断强弱转化
    ↓
独立自主法 + 统一战线法 → 制定策略
```
```

- [ ] **Step 2: 提交更改**

```bash
git add mzt/SKILL.md
git commit -m "feat(mzt): add methodology selection guide

- Add selection principles (宁精勿多, 问题导向, 逻辑递进)
- Add problem-type to methodology selection matrix
- Add methodology combination logic with examples

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 5: 重构 SKILL.md - 经典引用规范（P2）

**Files:**
- Modify: `mzt/SKILL.md`

- [ ] **Step 1: 在"方法论选择指南"章节之后、"注意事项"章节之前插入新章节**

**插入位置**: 在 Task 4 插入的内容之后，"注意事项"章节之前

**要插入的内容**:

```markdown

---

## 经典引用规范

### 引用原则

1. **引用是为了说明，不是为了装饰**
2. **引用后必须有展开分析**
3. **引用要嵌入论证逻辑**

### 错误示例

```markdown
> 星星之火，可以燎原。

（引用后无分析，直接进入下一节）
```

### 正确示例

```markdown
商鞅变法从一国实践开始，最终推动了历史发展——这正是"星星之火，可以燎原"的生动体现。变法虽然始于秦国一隅，但它代表的新兴地主阶级利益顺应历史潮流，最终促成了中国从奴隶社会向封建社会的转型。

具体而言：
1. **起点虽小**：变法始于落后的秦国，被视为"蛮夷"之地
2. **方向正确**：代表新兴生产力的发展要求
3. **逐步扩展**：秦国的成功为统一六国奠定基础
4. **最终燎原**：推动了中国社会形态的整体转型
```

### 引用展开模板

引用经典语录后，应该回答：

1. 这句话在本案例中具体指什么？
2. 为什么这个案例可以印证这句话？
3. 具体表现在哪些方面？
```

- [ ] **Step 2: 提交更改**

```bash
git add mzt/SKILL.md
git commit -m "feat(mzt): add classic citation guidelines

- Add citation principles
- Add wrong vs correct examples
- Add citation expansion template

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 6: 验证与测试

**Files:**
- All modified files

- [ ] **Step 1: 验证文件修改**

检查以下内容:
- [ ] `01-contradiction-analysis.md` 有 5 个步骤（原 4 个 + 新增 1 个）
- [ ] `05-class-stance-analysis.md` 删除了旧的"适用场景"，新增了"适用边界"
- [ ] `SKILL.md` 报告章节从 5 个扩展为 7 个
- [ ] `SKILL.md` 新增了"方法论选择指南"章节
- [ ] `SKILL.md` 新增了"经典引用规范"章节

- [ ] **Step 2: 验证交叉引用**

确保 SKILL.md 中对方法论文件的链接仍然有效。

- [ ] **Step 3: 创建总结提交**

```bash
git add -A
git commit -m "feat(mzt): complete MZT skill optimization

Implements all 6 improvements from improvement-plan.md:
- P0: Add contradiction transformation analysis
- P0: Add mandatory '事实依据' section
- P1: Add mandatory '批判性反思' section
- P1: Add methodology selection guide with priority matrix
- P2: Add applicability boundaries for class stance analysis
- P2: Add classic citation guidelines

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## 验收清单

- [ ] 所有 3 个文件已完成修改
- [ ] SKILL.md 报告章节从 5 个扩展为 7 个
- [ ] 新增章节模板完整、可用
- [ ] 交叉引用正确、格式一致
- [ ] 所有提交信息符合规范
