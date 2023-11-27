import numpy as np

# Definir una matriz 2x2
matriz_A = np.array([[2, 1],
                     [1, 3]])

# Calcular la matriz inversa
matriz_inversa = np.linalg.inv(matriz_A)

print("Matriz A:\n", matriz_A)
print("\nMatriz Inversa de A:\n", matriz_inversa)

'''
Ten en cuenta que en el ejemplo de la matriz inversa, la función np.linalg.inv() se 
utiliza para calcular la inversa de una matriz. 
Si la matriz es singular y no tiene inversa, se generará una excepción de LinAlgError. 
En el ejemplo de la matriz singular, se captura esta excepción para mostrar que la matriz no tiene inversa.
'''