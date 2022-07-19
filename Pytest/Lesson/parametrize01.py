import pytest

@pytest.mark.parametrize("tes_input,expected",[("3+5",8),("5-5",0),("3*5",15),("3/5",0.6)])

def test_eval(tes_input,expected):
    assert  eval(tes_input) ==expected