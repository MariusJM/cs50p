from numb3rs import validate
import pytest

def test_good_ip():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True

def test_bad_ip():
    assert validate("512.512.512.512") == False
    assert validate("254.54116.dsa.a") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.2.s.1000") == False
    assert validate("cat") == False
    assert validate("a.b.v.a") == False
