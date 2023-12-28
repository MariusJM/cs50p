from twttr import shorten
import pytest

def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Twitter, is the best") == "Twttr, s th bst"
    assert shorten("Tw1tt3r") == "Tw1tt3r"
    assert shorten("twIttEr Is nO mOrE") == "twttr s n mr"
