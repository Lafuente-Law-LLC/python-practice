import pytest
from pal import project_05_protocols


def test_countdown_iteration():

    c = project_05_protocols.Countdown(3)
    result = list(c)

    assert result == [3, 2, 1, 0]


def test_truthiness_protocol():
    c = project_05_protocols.Countdown(1)

    assert bool(c) is True
    next(c)
    assert bool(c) is False


def test_manual_for_loop():
    data = [10, 20, 30]

    result = project_05_protocols.manual_for_loop(data)
    assert result == [10, 20, 30]
