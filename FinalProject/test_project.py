import pytest
import bcrypt
from project import hash_password 
from project import format_time
from project import validate_numeric_input
from unittest.mock import MagicMock

def test_hash_password():
    password = "test_password"
    hashed_password = hash_password(password)
    assert hashed_password is not None
    assert isinstance(hashed_password, bytes)
    assert hashed_password != password.encode('utf-8')
    assert bcrypt.checkpw(password.encode('utf-8'), hashed_password)


def test_format_time():
    seconds = 123.456
    formatted_time = format_time(seconds)
    assert formatted_time is not None
    assert isinstance(formatted_time, str)
    assert formatted_time == "02:03.456"


def test_validate_numeric_input():
    result = validate_numeric_input('1', '123.45')
    assert result is True
    result = validate_numeric_input('1', 'abc')
    assert result is False
    result = validate_numeric_input('0', '123')
    assert result is True