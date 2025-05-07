from factorial_func import factorial
import pytest


@pytest.mark.parametrize("a, b", [(1, 1), (5, 120), (3, 6)])
def test_factorial_good(a, b):
    assert factorial(a) == b


@pytest.mark.parametrize("exsept, param", [(RecursionError, 1000),
                                           (RecursionError, 1.5),
                                           (TypeError, "text"),
                                           (RecursionError, -1)])
def test_factorial_bad(exsept, param):
    with pytest.raises(exsept):
        factorial(param)
