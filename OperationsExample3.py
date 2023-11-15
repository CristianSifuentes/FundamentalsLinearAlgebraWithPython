import numpy as np

# Definir una matriz (2x3)
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Definir un vector (3,)
vector = np.array([2, 3, 4])

# Multiplicación del vector por la matriz
# multiplicacion_vector_matriz = np.dot(vector, matriz)
multiplicacion_vector_matriz = np.dot(matriz, vector)

# Imprimir resultados
print("Matriz:\n", matriz)
print("\nVector:\n", vector)
print("\nMultiplicación de la matriz por el vector:\n", multiplicacion_vector_matriz)
