from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("0/2") == 0
    with pytest.raises(ValueError):
        assert convert("cat")
#    with pytest.raises(ZeroDivisionError):
#        convert("2/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
