import pytest
from pal.project_01_binding import ObjectAuditor


def test_mutable_alias():
    x = [1, 2, 3]
    y = x
    out = ObjectAuditor().audit(x, y)

    assert out["is_alias"] is True
    assert out["is_equal"] is True
    assert out["type_a"] is list
    assert out["type_b"] is list


def test_distinct_but_equal_lists():

    a = [1, 2, 3]
    b = [1, 2, 3]

    out = ObjectAuditor().audit(a, b)
    assert out["is_alias"] is False
    assert out["is_equal"] is True


def test_mutation_side_effect_on_alias():

    x = [1, 2, 3]
    y = x
    x.append(4)

    assert len(y) == 4
