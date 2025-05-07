import numpy as np

N = int(input("Введите размер матриц N: "))

A = np.random.randint(1, 101, size=(N, N))
B = np.random.randint(1, 101, size=(N, N))

C_greater = A > B
C_less = A < B
C_equal = A == B

print("Матрица A:")
print(A)
print("\nМатрица B:")
print(B)
print("\nМатрица C (A > B):")
print(C_greater)
print("\nМатрица C (A < B):")
print(C_less)
print("\nМатрица C (A == B):")
print(C_equal)
