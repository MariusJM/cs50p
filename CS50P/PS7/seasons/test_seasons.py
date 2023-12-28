from seasons import convert_time
import pytest

def test_function():
    assert convert_time(1988, 6, 23) == "Eighteen million, six hundred twenty-four thousand, nine hundred sixty minutes"
    assert convert_time(January, 1, 1999) == "Invalid date"
