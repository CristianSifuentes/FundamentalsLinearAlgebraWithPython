import numpy as np

# Definir dos matrices (2x3 y 3x2)
matriz_A = np.array([[1, 2, 3], [4, 5, 6]])
matriz_B = np.array([[7, 8], [9, 10], [11, 12]])

# Calcular el producto de las matrices
producto_matrices = np.dot(matriz_A, matriz_B)

# Mostrar las matrices originales y el producto
print("Matriz A (2x3):\n", matriz_A)
print("\nMatriz B (3x2):\n", matriz_B)
print("\nProducto de las matrices (2x2):\n", producto_matrices)

# Transposición de un producto de matrices: (AB)^T = B^T * A^T
transpuesta_producto = np.dot(matriz_B.T, matriz_A.T)

# Mostrar la transposición del producto
print("\nTransposición del producto (B^T * A^T):\n", transpuesta_producto)

# Variantes y ejercicios adicionales
variante_1 = np.dot(matriz_B, matriz_A).T  # Transponer después del producto original
variante_2 = np.dot(matriz_A.T, matriz_B.T)  # Transponer antes de realizar el producto

# Mostrar variantes
print("\nVariante 1 (AB)^T:\n", variante_1)
print("\nVariante 2 (A^T * B^T):\n", variante_2)

# Ejercicio adicional: Transposición de una transposición
matriz_original = np.array([[1, 2], [3, 4]])
transpuesta_original = matriz_original.T
transposicion_transpuesta = transpuesta_original.T

# Mostrar resultados del ejercicio adicional
print("\nMatriz Original:\n", matriz_original)
print("\nTranspuesta de la Matriz Original:\n", transpuesta_original)
print("\nTransposición de la Transpuesta:\n", transposicion_transpuesta)

'''

'''