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

'''
Mis disculpas por la confusión. Efectivamente, el error se debe a que las dimensiones de las matrices no son compatibles para la multiplicación en ese orden específico. Para realizar la multiplicación de un vector por una matriz en NumPy, el número de columnas en la matriz debe ser igual al número de elementos en el vector.
'''


'''
En este ejemplo, la multiplicación np.dot(matriz, vector) es válida porque el número de columnas en la matriz (3) es igual al número de elementos en el vector (3). Este resultado será un nuevo vector cuyos elementos son combinaciones lineales de las filas de la matriz multiplicadas por los elementos del vector.






'''