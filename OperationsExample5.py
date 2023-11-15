import numpy as np

# Definir matrices (2x2) y vectores (2,)
matriz_A = np.array([[1, 2], [3, 4]])
matriz_B = np.array([[5, 6], [7, 8]])
matriz_C = np.array([[9, 10], [11, 12]])

vector_x = np.array([2, 3])
vector_y = np.array([4, 5])
vector_z = np.array([6, 7])

# Propiedad Asociativa con Matrices: (A * B) * C == A * (B * C)
asociativa_izquierda_matrices = np.dot(np.dot(matriz_A, matriz_B), matriz_C)
asociativa_derecha_matrices = np.dot(matriz_A, np.dot(matriz_B, matriz_C))

# Propiedad Asociativa con Vectores: (x dot y) dot z == x dot (y dot z)
asociativa_izquierda_vectores = np.dot(np.dot(vector_x, vector_y), vector_z)
asociativa_derecha_vectores = np.dot(vector_x, np.dot(vector_y, vector_z))

# Propiedad Distributiva con Matrices: A * (B + C) == (A * B) + (A * C)
distributiva_izquierda_matrices = np.dot(matriz_A, matriz_B + matriz_C)
distributiva_derecha_matrices = np.dot(matriz_A, matriz_B) + np.dot(matriz_A, matriz_C)

# Propiedad Distributiva con Vectores: x dot (y + z) == (x dot y) + (x dot z)
distributiva_izquierda_vectores = np.dot(vector_x, vector_y + vector_z)
distributiva_derecha_vectores = np.dot(vector_x, vector_y) + np.dot(vector_x, vector_z)

# Propiedad Conmutativa con Vectores: x dot y == y dot x
conmutativa_vectores = np.dot(vector_x, vector_y) == np.dot(vector_y, vector_x)

# Imprimir resultados
print("Matrices:")
print("Matriz A:\n", matriz_A)
print("Matriz B:\n", matriz_B)
print("Matriz C:\n", matriz_C)

print("\nPropiedad Asociativa con Matrices:")
print("(A * B) * C:\n", asociativa_izquierda_matrices)
print("A * (B * C):\n", asociativa_derecha_matrices)

print("\nPropiedad Distributiva con Matrices:")
print("A * (B + C):\n", distributiva_izquierda_matrices)
print("(A * B) + (A * C):\n", distributiva_derecha_matrices)

print("\nVectores:")
print("Vector x:", vector_x)
print("Vector y:", vector_y)
print("Vector z:", vector_z)

print("\nPropiedad Asociativa con Vectores:")
print("(x dot y) dot z:", asociativa_izquierda_vectores)
print("x dot (y dot z):", asociativa_derecha_vectores)

print("\nPropiedad Distributiva con Vectores:")
print("x dot (y + z):", distributiva_izquierda_vectores)
print("(x dot y) + (x dot z):", distributiva_derecha_vectores)

print("\nPropiedad Conmutativa con Vectores:")
print("x dot y == y dot x:", conmutativa_vectores)
