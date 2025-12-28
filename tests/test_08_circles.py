import pytest
import importlib
import sys


def test_circular_import_crash():
    for mod in ["pal.project_08_circles.module_a_bad",
                "pal.project_08_circles.module_b_bad"]:
        if mod in sys.modules:
            del sys.modules[mod]
    
    with pytest.raises((ImportError, AttributeError)):
        importlib.import_module("pal.project_08_circles.module_a_bad")

def test_circular_import_fix():

    for mod in ["pal.project_08_circles.module_a_fixed",
                "pal.project_08_circles.module_b_fixed"]:
        if mod in sys.modules:
            del sys.modules[mod]
    
    mod_a = importlib.import_module("pal.project_08_circles.module_a_fixed")

    assert mod_a.get_b_name() == "Module B"

