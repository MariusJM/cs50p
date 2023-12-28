from response import check_validity
import pytest

def test_email():
    assert check_validity("mariusjm.work@gmail.com") == True
    assert check_validity("malan@harvard.edu") == True
    assert check_validity("malan@@@harvard.edu") == False
    assert check_validity("malan@harv@ard.edu") == False
    assert check_validity("malan@harvard..edu") == False
