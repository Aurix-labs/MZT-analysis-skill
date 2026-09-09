# README 配图与引文说明

## 配图

调查研究与星火两幅插画以革命年代宣传画、木刻与书刊的视觉语言进行当代创作，使用内置 imagegen 生成于 2026 年 9 月 9 日。人物活动场景为主题性插画，图中文字为新设计的书写与排印；不是历史照片、史料扫描或毛泽东手迹。

| 文件 | 画面与用途 |
| :--- | :--- |
| [investigation-quote.png](investigation-quote.png) | 倾听乡亲意见、记录材料；调查研究引文配图 |
| [spark-quote.png](spark-quote.png) | 油灯、书卷、田野与红旗；星火引文题图 |
| [mao-flag.png](mao-flag.png) | 用户提供的原始红旗剪影，保持原文件，用作开篇主图 |

调查研究与星火两张图使用统一的朱红、米黄、墨黑配色和纸张、木刻纹理。用户提供的搜索结果截图仅用于理解风格方向，未作为历史图片来源或进行拼贴。

## 引文

| 引文 | 仓库原文与日期 | 语境 |
| :--- | :--- | :--- |
| 没有调查，没有发言权。 | [《反对本本主义》](../../毛泽东选集/第一卷-第二次国内革命战争时期/反对本本主义.md)，1930 年 5 月 | 原文第一节标题；独立展示时补句号。下文要求调查问题的现实情况与历史情况。 |
| 你要知道梨子的滋味，你就得变革梨子，亲口吃一吃。 | [《实践论》](../../毛泽东选集/第一卷-第二次国内革命战争时期/实践论.md)，1937 年 7 月 | 说明实践与认识的关系。同段也承认间接经验的作用，并非要求每件事都亲身经历。 |
| 星星之火，可以燎原。 | [《星星之火，可以燎原》](../../毛泽东选集/第一卷-第二次国内革命战争时期/星星之火可以燎原.md)，1930 年 1 月 5 日 | 毛泽东在文中明确称其为“中国的一句老话”。文章结合当时的社会关系和革命形势分析发展条件，不是任何微小开端都会成功的保证。 |

英文 README 的短引文均为本项目译文（project translations），未标作官方英译。图中的中文原文在英文页面保留。

## 生成提示词

以下为内置 imagegen 使用的最终提示词。未调用 API / CLI 备用模式。

### 调查研究

```text
Use case: stylized-concept.
Asset type: a wide illustrated quotation panel inside a GitHub README about Mao Zedong Thought as guidance for AI judgment.
Original mid-20th-century Chinese revolutionary woodcut and letterpress poster aesthetic. Landscape 3:1 about 1800x600. Full-bleed cream rice-paper texture, vermilion red, deep ink-black linework, sparse ochre. A finely drawn period scene occupies the left 45 percent: Mao Zedong seated at a plain wooden table taking notes and listening attentively to a rural woman and an older farmer, notebook and loose survey sheets on table, simple rural courtyard beyond. Equal dignified natural seated conversation, focus on attentive investigation, neither a rally nor a battle. Careful anatomy and hands; do not claim depiction of a specific real meeting.
On the right a large visually striking original Chinese brush-lettered quotation, perfectly legible, two balanced lines in dark red:
"没有调查，"
"没有发言权。"
Below it a small black printed line: "《反对本本主义》 · 1930"
An understated red double-line printed border may frame the full composition. Strong vintage printed-book illustration quality with lively tactile hatching, not a modern corporate card. Text and figures should fill their space confidently with safe margins, remain clear when viewed at 900px width. No fake handwriting signature, no other text, no watermark, no weapon, no modern electronics. This is a contemporary newly generated homage to historical print design, not a historic document.
```

### 星火题图

```text
Use case: stylized-concept.
Asset type: wide concluding quotation illustration for a GitHub README, part of an original visual series inspired by mid-20th-century Chinese revolutionary woodcuts and printed book covers.
Landscape 3:1 about 1800x600, full-bleed textured warm cream paper, rich deep vermilion and ink-black engraved linework, small muted-gold highlights. Make a confident vivid graphic composition, not a plain text rectangle.
Left 62 percent: enormous beautifully composed original brush lettering, carefully readable in two lines, exact Chinese text:
"星星之火，"
"可以燎原。"
Underneath in small typeset text exactly: "《星星之火，可以燎原》 · 1930"
Right 38 percent: a bright small oil lamp beside an open study book on a simple wooden desk, with layered bold red flag folds and a rhythmic engraved pattern of cultivated fields and a sunrise in the background. A few small silhouettes of people reading and discussing at the lower edge, grounded in the historical print idiom. Symbolic spark of study and practical understanding, not an actual forest fire. Rich red background shapes and cream light visually balance the dark brush calligraphy. Safe margins around every letter. Cohesive with a Mao woodcut hero cover and a rural-investigation vignette elsewhere in the page. No imitation of a real person's handwriting, no signatures, no other text, no watermark, no QR code, no weapons, no electronics. This is a new illustration and graphic treatment, not a scan of a historical artifact.
```
