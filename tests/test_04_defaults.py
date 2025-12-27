import pytest
from pal import project_04_defaults


def test_mutable_default_trap():
    log1 = project_04_defaults.spy_log("Entry 1")
    assert log1 == ["Entry 1"]

    log2 = project_04_defaults.spy_log("Entry 2")

    assert log2 == ["Entry 1", "Entry 2"]

    assert log1 is log2


def test_default_identity_stability():
    defaults_before = project_04_defaults.inspect_defaults(
        project_04_defaults.spy_log)

    default_list_before = defaults_before[0]

    project_04_defaults.spy_log("Entry 3")

    defaults_after = project_04_defaults.inspect_defaults(
        project_04_defaults.spy_log)
    default_list_after = defaults_after[0]

    assert default_list_before is default_list_after


def test_sentinel_fix():

    clean1 = project_04_defaults.clean_log("Fresh 1")
    assert clean1 == ["Fresh 1"]

    clean2 = project_04_defaults.clean_log("Fresh 2")

    assert clean2 == ["Fresh 2"]

    assert clean1 is not clean2
