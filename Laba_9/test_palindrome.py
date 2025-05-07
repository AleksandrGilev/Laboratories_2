from pickle import FALSE

from palindrome_func import palindrome
import pytest


@pytest.mark.parametrize("text, result", [("казак", True),
                                          ("топот", True),
                                          ("шалаш", True)])
def test_palindrome_valid(text, result):
    assert palindrome(text) == result


@pytest.mark.parametrize("text, result", [("привет", False),
                                          ("март", False),
                                          ("тест", False)])
def test_palindrome_invalid(text, result):
    assert palindrome(text) == result


@pytest.mark.parametrize("text, result", [("аа", False),
                                          ("b", False),
                                          ("", False)])
def test_palindrome_short(text, result):
    assert palindrome(text) == result


@pytest.mark.parametrize("text, result", [("А роза упала на лапу Азора", True)])
def test_palindrome_with_space(text, result):
    assert palindrome(text) == result


@pytest.mark.parametrize("text, result", [("кАзАК", True),
                                          ("ТопОТ", True)])
def test_palindrome_register(text, result):
    assert palindrome(text) == result
