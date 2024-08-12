import random

def generate_matrix(rows, cols):
        return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix_1, matrix_2):
        rows = len(matrix_1)
        cols = len(matrix_1[0])
        return [[matrix_1[i][j] + matrix_2[i][j] for j in range(cols)] for i in range(rows)]

matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)

matrix_3 = add_matrices(matrix_1, matrix_2)

print("Matrix 1:")
for row in matrix_1:
        print(row)

print("\nMatrix 2:")
for row in matrix_2:
        print(row)

print("\nMatrix 3 (Sum):")
for row in matrix_3:
        print(row)