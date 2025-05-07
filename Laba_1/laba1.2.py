def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def print_table(n):
    print("  ", end="")
    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
    print()

    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
        for j in range(1, n + 1):
            if gcd(i, j) == 1:
                print(" X", end=" ")
            else:
                print(" O", end=" ")
        print()

while True:
    try:
        N = int(input("Введите число N: "))
        break
    except ValueError:
        print("Введите корректное число.")

print_table(N)
