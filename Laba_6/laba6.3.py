import numpy as np


def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            n = int(lines[0].strip())
            A = []
            b = []
            for i in range(1, n + 1):
                A.append(list(map(float, lines[i].strip().split())))
            b = list(map(float, lines[n + 1].strip().split()))
        return np.array(A), np.array(b)
    except FileNotFoundError:
        print("Файл не найден")
        return []


def solve_linear_system(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        return "Система не имеет решения или имеет бесконечно много решений."


def main():
    filename = "input.txt"
    A, b = read_data_from_file(filename)
    solution = solve_linear_system(A, b)
    print("Решение системы:", solution)


if __name__ == "__main__":
    main()
