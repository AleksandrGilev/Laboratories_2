import numpy as np

N = int(input("Введите размер матрицы N: "))

A = np.random.randint(1, 101, size=(N, N))

print("Сгенерированная матрица:")
print(A)

column_sums = A.sum(axis=0)
min_sum_column = np.argmin(column_sums) + 1

print(f"Номер столбца с минимальной суммой: {min_sum_column}")
