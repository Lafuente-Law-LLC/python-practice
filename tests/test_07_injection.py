import sys
import pytest
from pal import project_07_injection


def setup_function():
    if "my_ghost" in sys.modules:
        del sys.modules["my_ghost"]

def teardown_function():
    if "my_ghost" in sys.modules:
        del sys.modules["my_ghost"]

def test_ghost_import_success():
    ghost = project_07_injection.make_ghost("my_ghost", {"secret": 42})
    project_07_injection.inject("my_ghost", ghost)

    imported_module = project_07_injection.import_ghost("my_ghost")

    assert imported_module.secret == 42
    assert imported_module.__name__ == "my_ghost"

def test_ghost_identity_stability():
    ghost = project_07_injection.make_ghost("my_ghost", {})
    project_07_injection.inject("my_ghost", ghost)

    m1 = project_07_injection.import_ghost("my_ghost")
    m2 = project_07_injection.import_ghost("my_ghost")

    assert m1 is m2

