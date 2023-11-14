import numpy as np

# Definir escalares, vectores, matrices y tensor
escalar = np.array(5)
vector = np.array([1, 2, 3])
matriz = np.array([[1, 2, 3], [4, 5, 6]])
tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Imprimir los elementos
print("Escalar:\n", escalar)
print("\nVector:\n", vector)
print("\nMatriz:\n", matriz)
print("\nTensor:\n", tensor)

# Operaciones de suma y combinaciones lineales
suma_escalares = escalar + 10
suma_vectores = vector + np.array([5, 5, 5])
suma_matrices = matriz + np.array([[1, 1, 1], [1, 1, 1]])
combinacion_lineal = 2 * matriz - 3 * np.array([[1, 2, 3], [4, 5, 6]])

# Imprimir resultados de suma y combinaciones lineales
print("\nSuma de escalares:\n", suma_escalares)
print("\nSuma de vectores:\n", suma_vectores)
print("\nSuma de matrices:\n", suma_matrices)
print("\nCombinación lineal:\n", combinacion_lineal)

# Operaciones de transposición
transpuesta_matriz = matriz.T
transpuesta_transpuesta = transpuesta_matriz.T

# Imprimir resultados de transposición
print("\nTranspuesta de la matriz:\n", transpuesta_matriz)
print("\nTranspuesta de la transpuesta:\n", transpuesta_transpuesta)

# Suma de una matriz con su transpuesta
suma_matriz_transpuesta = matriz + matriz.T

# Imprimir resultado de la suma de matriz con su transpuesta
print("\nSuma de una matriz con su transpuesta:\n", suma_matriz_transpuesta)
