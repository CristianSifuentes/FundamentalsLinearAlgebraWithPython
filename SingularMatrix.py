import numpy as np

# Definir una matriz 2x2 singular
matriz_B = np.array([[1, 2],
                     [2, 4]])

# Intentar calcular la matriz inversa (generará un error porque es singular)
try:
    matriz_inversa_B = np.linalg.inv(matriz_B)
except np.linalg.LinAlgError:
    matriz_inversa_B = None

print("Matriz B:\n", matriz_B)
print("\nIntento de calcular la matriz inversa de B:\n", matriz_inversa_B)
