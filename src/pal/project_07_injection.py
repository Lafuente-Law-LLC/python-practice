import sys
import types
import importlib


def make_ghost(name:str, attrs: dict) -> types.ModuleType:
    module = types.ModuleType(name)
    for key, value in attrs.items():
        setattr(module, key, value)
    return module

def inject(name: str, module: types.ModuleType) -> None:
    sys.modules[name] = module

def import_ghost(name: str) -> types.ModuleType:
    return importlib.import_module(name)



