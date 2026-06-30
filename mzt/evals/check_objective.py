"""MZT 输出客观指标检查。真实测量，不为通过测试硬编码任何样例答案。"""
import re

_MAIN_CONTRADICTION = re.compile(r"主要矛盾[是为：:]\s*\S+|主要矛盾.{0,30}?(冲突|矛盾|权衡|对立)")
_FALSIFIABLE = re.compile(r"(可验证假设|可证伪|验证方法)[：:].*\S")
_GATE = re.compile(r"(确认方向正确|等待您回复|请确认|方向正确吗|您可以说.直接分析)")
# 可疑/占位来源样式：保守统计，避免误伤真实引用
_FAB_SOURCE = [
    re.compile(r"http://example\.com"),
    re.compile(r"来源[：:]\s*[?？]"),
    re.compile(r"某(权威|知名|相关)?(报告|机构|研究|媒体)"),
    re.compile(r"\[?待补充\]?|占位"),
]


def check_output(text: str, problem_type: str) -> dict:
    names_main = bool(_MAIN_CONTRADICTION.search(text))
    has_hyp = bool(_FALSIFIABLE.search(text))
    fab = sum(len(p.findall(text)) for p in _FAB_SOURCE)
    if problem_type == "cognition":
        avoided_gate = not bool(_GATE.search(text))
    else:
        avoided_gate = None
    return {
        "names_main_contradiction": names_main,
        "has_falsifiable_hypothesis": has_hyp,
        "fabricated_sources": fab,
        "avoided_unneeded_gate": avoided_gate,
    }
