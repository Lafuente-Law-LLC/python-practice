import gc
import weakref
import pytest
from pal import project_09_gc


def test_cycle_survival_without_gc():
    gc.disable()

    try:
        node_ref = project_09_gc.make_cycle()


        assert node_ref() is not None
    finally:
        gc.enable()

def test_cycle_reclamation_with_gc():
    gc.disable()

    try:
        node_ref = project_09_gc.make_cycle()
        assert node_ref() is not None

        gc.collect()

        assert node_ref() is None
    finally:
        gc.enable()

