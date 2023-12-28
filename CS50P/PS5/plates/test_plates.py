from plates import is_valid
import pytest

def test_first_letters():
    assert is_valid("CS50") == True
    assert is_valid("CS505050") == False
    assert is_valid("CS00") == False
    assert is_valid("CS00as") == False
    assert is_valid("CSCS50") == True
    assert is_valid("CS") == True
def test_number_placement():
    assert is_valid("CS50") == True
    assert is_valid("C5") == False
    assert is_valid("5C") == False
    assert is_valid("00") == False
    assert is_valid("50") == False
    assert is_valid("5") == False
    assert is_valid("CS5!") == False
    assert is_valid("CSCS050") == False
    assert is_valid("cs50cs") == False
    assert is_valid("asd123") == True
    assert is_valid("asd12e") == False
    assert is_valid("asd0123") == False
"""

    assert is_valid("C5S0") == False
    assert is_valid("C,4551A") == False
    assert is_valid("Cs4 51A") == False
    assert is_valid("CS45-1A") == False
    assert is_valid(",-*/.=") == False
    assert is_valid("CS4551A") == False
    assert is_valid("C5S05d1") == False
    assert is_valid("C5S0a64") == False
    assert is_valid("CS05") == False
    assert is_valid("C") == False
    assert is_valid("CS5000") == True
    assert is_valid("C5S0564") == False
    assert is_valid("C5S0564") == False

    assert is_valid("CS") == True
    assert is_valid("11") == False
    assert is_valid("00") == False
    assert is_valid("C1") == True
    assert is_valid(",1") == False


def test_length():
    assert is_valid("C") == False
    assert is_valid("CS5000") == True
    assert is_valid("C5S0564") == False
    assert is_valid("C5S0564") == False

def test_numbers_middle():
    assert is_valid("CS4551A") == False
    assert is_valid("C5S05d1") == False
    assert is_valid("C5S0a64") == False
    assert is_valid("CS05") == False

def test_not_alnum():
    assert is_valid("C,4551A") == False
    assert is_valid("Cs4 51A") == False
    assert is_valid("CS45-1A") == False
    assert is_valid(",-*/.=") == False
    #assert is_valid("asdfgh") == True
    #assert is_valid("123456") == True
"""
