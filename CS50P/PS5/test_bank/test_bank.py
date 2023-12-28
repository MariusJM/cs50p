from bank import value
import pytest

def test_hello():
    assert value("hello") == int(0)
    assert value("hello,") == int(0)
def test_hi():
    assert value("hi") == int(20)
def test_yo():
    assert value("Yo") == int(100)
    assert value("“What’s up") == int(100)
def test_upper():
    assert value("Hello") == int(0)
    assert value("Hi") == int(20)
