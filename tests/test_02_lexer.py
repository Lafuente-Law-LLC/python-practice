import pytest
from pal.project_02_lexer import tokenize_indentation


def test_basic_nesting():
    source = """
if True:
    pass
"""
    tokens = tokenize_indentation(source)
    assert tokens == ["INDENT", "DEDENT"]
