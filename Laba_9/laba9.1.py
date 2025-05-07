import pytest


def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Факториал можно вычислить только для целых чисел")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_large():
    with pytest.raises(RecursionError):
        factorial(1000)


def test_factorial_float():
    with pytest.raises(TypeError):
        factorial(1.5)


def test_factorial_string():
    with pytest.raises(TypeError):
        factorial("test")


def main():
    try:
        user_input = int(input("Введите целое неотрицательное число для вычисления факториала: "))
        result = factorial(user_input)
        print(f"Факториал числа {user_input} равен {result}")
    except ValueError as e:
        if "invalid literal for int" in str(e):
            print("Ошибка: Введите целое число")
        else:
            print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка: {e}")
    except RecursionError:
        print("Ошибка: Слишком большое число для вычисления факториала")


if __name__ == "__main__":
    main()
