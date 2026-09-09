"""检查可机械测量的输出契约；不把脚本单测当作技能行为评测。"""

import pytest

from check_objective import check_output


def test_reports_codepoints_and_nonempty_lines_without_quality_verdict():
    result = check_output("你好\n\nworld", "practice")
    assert result == {
        "schema_version": 2,
        "character_count": 9,
        "nonempty_line_count": 2,
        "constraints": {},
    }


def test_keywords_and_plausible_citations_do_not_become_semantic_scores():
    result = check_output("主要矛盾是甲乙冲突。可证伪：明天见。来源：某权威报告。", "cognition")
    assert set(result) == {
        "schema_version", "character_count", "nonempty_line_count", "constraints"
    }
    assert result["constraints"] == {}


def test_legacy_problem_type_does_not_impose_an_output_shape():
    text = "请确认这次操作的目标环境。"
    assert check_output(text, "cognition") == check_output(text, "practice")


def test_explicit_character_limit_is_inclusive():
    result = check_output("四个字符", constraints={"max_characters": 4})
    assert result["constraints"]["max_characters"] == {
        "expected": 4, "observed": 4, "satisfied": True
    }


def test_character_limit_includes_whitespace_and_punctuation():
    result = check_output("答。\n", constraints={"max_characters": 2})
    assert result["constraints"]["max_characters"] == {
        "expected": 2, "observed": 3, "satisfied": False
    }


def test_explicit_line_constraint_ignores_blank_lines():
    result = check_output("第一行\n  \n第二行\n", constraints={"exact_nonempty_lines": 1})
    assert result["constraints"]["exact_nonempty_lines"] == {
        "expected": 1, "observed": 2, "satisfied": False
    }


def test_empty_output_is_measured_without_claiming_quality():
    result = check_output("", constraints={"max_characters": 0, "exact_nonempty_lines": 0})
    assert result["character_count"] == result["nonempty_line_count"] == 0
    assert all(item["satisfied"] for item in result["constraints"].values())


def test_unknown_constraints_are_not_silently_reported_as_passed():
    with pytest.raises(ValueError, match="Unsupported constraint"):
        check_output("回答", constraints={"factually_correct": True})


@pytest.mark.parametrize("limit", [-1, 1.5, True, "100"])
def test_limits_require_nonnegative_integers(limit):
    with pytest.raises(ValueError, match="nonnegative integer"):
        check_output("回答", constraints={"max_characters": limit})
