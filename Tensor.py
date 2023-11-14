
'''
Claro, a continuación, te proporciono un ejemplo simple en Python utilizando la biblioteca 
NumPy para trabajar con tensores. En este caso, representaremos un tensor tridimensional y 
realizaremos algunas operaciones básicas:
'''

import numpy as np

# Crear un tensor tridimensional (3x3x3)
tensor_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                     [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

# Imprimir el tensor original
print("Tensor 3D original:\n", tensor_3d)

# Acceder a elementos específicos
element = tensor_3d[1, 2, 1]
print(f"\nElemento en la posición (1, 2, 1): {element}")

# Operaciones de tensor
tensor_sum = tensor_3d + 10
tensor_product = tensor_3d * 2

# Imprimir resultados de operaciones
print("\nTensor 3D + 10:\n", tensor_sum)
print("\nTensor 3D * 2:\n", tensor_product)


'''
En este ejemplo, tensor_3d es un tensor tridimensional de tamaño 3x3x3. 
Realizamos algunas operaciones básicas, como acceder a elementos 
específicos y realizar operaciones de suma y multiplicación con escalares.

Recuerda que, en el contexto del aprendizaje automático, 
los tensores suelen representar datos de dimensiones superiores, 
como imágenes en color (3D) o secuencias temporales (2D) 
para procesamiento de lenguaje natural. NumPy y bibliotecas 
de aprendizaje automático como TensorFlow y PyTorch son 
herramientas poderosas para trabajar con tensores en Python.
'''