import numpy as np

# Definir dos matrices (2x3)
matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
matriz2 = np.array([[2, 0, 1], [1, 2, 3]])

# Calcular el producto interno entre las dos matrices
producto_interno = np.dot(matriz1, matriz2.T)  # Transponer la segunda matriz para que las dimensiones sean compatibles

# Imprimir resultados
print("Matriz 1:\n", matriz1)
print("\nMatriz 2:\n", matriz2)
print("\nProducto interno entre las dos matrices:\n", producto_interno)
