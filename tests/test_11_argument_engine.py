import pytest
from dataclasses import dataclass
from typing import Any, Dict, Tuple




def test_positional_after_keyword_raises():
    def target_function(a,b,c):
        return a + b + c

    with pytest.raises(SyntaxError):
        eval("target_function(10, b=20, 30)")

def test_args_is_tuple_kwargs_is_dict():
    def probe(*args, **kwargs):
        return BindingReport(args_type=type(args),
                             kwargs_type=type(kwargs),
                             bound_params={},
                             original_ids={})
    
    report = probe(1, 2, 3, x=4, x=5)

    assert report.args_type is tuple
    assert report.kwargs_type is dict






