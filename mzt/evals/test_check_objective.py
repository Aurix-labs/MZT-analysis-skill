from check_objective import check_output


def test_names_main_contradiction_detected():
    text = "## 矛盾分析\n本问题的主要矛盾是个人成长与平台稳定之间的冲突。"
    assert check_output(text, "practice")["names_main_contradiction"] is True


def test_main_contradiction_heading_only_not_counted():
    text = "## 主要矛盾\n（此处为空）"
    assert check_output(text, "practice")["names_main_contradiction"] is False


def test_falsifiable_hypothesis_detected():
    text = "可验证假设：若三个月内拿到两个 offer，则市场需求成立。验证方法：投递并统计。"
    assert check_output(text, "practice")["has_falsifiable_hypothesis"] is True


def test_fabricated_source_counted():
    text = "数据来源：某权威报告。链接：http://example.com"
    assert check_output(text, "cognition")["fabricated_sources"] >= 1


def test_cognition_avoids_gate():
    text = "秦统一六国的根本原因是……（直接展开分析，无停等）"
    assert check_output(text, "cognition")["avoided_unneeded_gate"] is True


def test_cognition_gate_present_flagged():
    text = "请确认方向正确后我再继续，等待您回复。"
    assert check_output(text, "cognition")["avoided_unneeded_gate"] is False


def test_non_cognition_gate_field_is_none():
    assert check_output("任意文本", "practice")["avoided_unneeded_gate"] is None
