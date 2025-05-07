from count_repeted_chars_func import count_repeted_chars
import pytest


@pytest.mark.parametrize("text, result", [("python", 0),
                                          ("programming", 3),
                                          ("", 0),
                                          ("hello world", 2),
                                          ("hello", 1)])
def test_count_repeted_chars(text, result):
    assert count_repeted_chars(text) == result
