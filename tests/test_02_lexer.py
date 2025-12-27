import pytest
from pal.project_02_lexer import tokenize_indentation


def test_standard_nesting():
    code = """
if True:
    x = 1
    if False:
        y = 2
"""
    # Expect: INDENT (for x=1), INDENT (for y=2), DEDENT, DEDENT
    assert tokenize_indentation(
        code) == ["INDENT", "INDENT", "DEDENT", "DEDENT"]


def test_parenthesis_trap():
    code = """
x = (
    1,
    2
)
"""
    # Implicit line joining: The indentation inside () is ignored.
    assert tokenize_indentation(code) == []


def test_invalid_dedent():
    code = """
if True:
    x = 1
  y = 2  # Error: indents to 4, then dedents to 2 (0 is expected)
"""
    with pytest.raises(IndentationError):
        tokenize_indentation(code)
