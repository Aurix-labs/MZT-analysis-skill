"""测量可见输出的尺寸和题目明确给出的限制，不判断思考或事实质量。

返回结构为 v2。保留旧的 problem_type 参数以便迁移调用；它不参与测量。
字符数是 Python len(text)，含空白和标点，不是 token 数或中文词数。
"""


def check_output(text: str, problem_type=None, *, constraints=None) -> dict:
    """constraints 仅接受 max_characters 和 exact_nonempty_lines。

    调用方只能传入用户明确要求的限制；未指定时不施加长度或格式目标。
    返回的 satisfied 只表示该项可机械检查的限制是否满足。
    """
    character_count = len(text)
    nonempty_line_count = sum(bool(line.strip()) for line in text.splitlines())
    checks = {}
    for name, expected in (constraints or {}).items():
        if name not in {"max_characters", "exact_nonempty_lines"}:
            raise ValueError(f"Unsupported constraint: {name}")
        if type(expected) is not int or expected < 0:
            raise ValueError(f"{name} must be a nonnegative integer")
        observed = character_count if name == "max_characters" else nonempty_line_count
        satisfied = observed <= expected if name == "max_characters" else observed == expected
        checks[name] = {"expected": expected, "observed": observed, "satisfied": satisfied}
    return {
        "schema_version": 2,
        "character_count": character_count,
        "nonempty_line_count": nonempty_line_count,
        "constraints": checks,
    }
