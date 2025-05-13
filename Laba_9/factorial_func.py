def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    n = int(input("Введите целое неотрицательное число для вычисления факториала: "))
    result = factorial(n)
    print(f"Факториал числа {n} равен {result}")


if __name__ == "__main__":
    main()
