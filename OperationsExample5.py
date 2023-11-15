import numpy as np

# Definir tres matrices (2x2)
matriz_A = np.array([[1, 2], [3, 4]])
matriz_B = np.array([[5, 6], [7, 8]])
matriz_C = np.array([[9, 10], [11, 12]])

# Propiedad Asociativa: (A * B) * C == A * (B * C)
asociativa_izquierda = np.dot(np.dot(matriz_A, matriz_B), matriz_C)
asociativa_derecha = np.dot(matriz_A, np.dot(matriz_B, matriz_C))

# Propiedad Distributiva: A * (B + C) == (A * B) + (A * C)
distributiva_izquierda = np.dot(matriz_A, matriz_B + matriz_C)
distributiva_derecha = np.dot(matriz_A, matriz_B) + np.dot(matriz_A, matriz_C)

# Propiedad Conmutativa: A * B == B * A
conmutativa = np.array_equal(np.dot(matriz_A, matriz_B), np.dot(matriz_B, matriz_A))

# Imprimir resultados
print("Matriz A:\n", matriz_A)
print("\nMatriz B:\n", matriz_B)
print("\nMatriz C:\n", matriz_C)

print("\nPropiedad Asociativa:")
print("(A * B) * C:\n", asociativa_izquierda)
print("A * (B * C):\n", asociativa_derecha)

print("\nPropiedad Distributiva:")
print("A * (B + C):\n", distributiva_izquierda)
print("(A * B) + (A * C):\n", distributiva_derecha)

print("\nPropiedad Conmutativa:")
print("A * B == B * A:", conmutativa)


'''
En este ejemplo:

La propiedad asociativa se verifica al comparar (A * B) * C con A * (B * C).
La propiedad distributiva se verifica al comparar A * (B + C) con (A * B) + (A * C).
La propiedad conmutativa se verifica al comparar A * B con B * A.
Es importante notar que la propiedad conmutativa no siempre se cumple en la multiplicación de matrices, a diferencia de la propiedad asociativa y distributiva. En este ejemplo, las matrices son pequeñas y específicamente elegidas para cumplir con estas propiedades.

'''