import numpy as np

# Definir una matriz 3x3
matriz_A = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Multiplicar la matriz por la matriz identidad
matriz_identidad = np.identity(3)
resultado = np.dot(matriz_A, matriz_identidad)

print("Matriz A:\n", matriz_A)
print("\nMatriz Identidad:\n", matriz_identidad)
print("\nResultado de multiplicar A por la Identidad:\n", resultado)
