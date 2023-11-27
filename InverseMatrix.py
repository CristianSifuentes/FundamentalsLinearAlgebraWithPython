import numpy as np

# Definir una matriz 2x2
matriz_A = np.array([[2, 1],
                     [1, 3]])

# Calcular la matriz inversa
matriz_inversa = np.linalg.inv(matriz_A)

print("Matriz A:\n", matriz_A)
print("\nMatriz Inversa de A:\n", matriz_inversa)
