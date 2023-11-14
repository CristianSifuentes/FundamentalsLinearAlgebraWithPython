import numpy as np

# Escalar
escalar1 = 5
escalar2 = 3
suma_escalar = escalar1 + escalar2
print(f'Suma de escalares: {suma_escalar}\n')

# Vector
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
suma_vector = vector1 + vector2
combinacion_lineal = 2 * vector1 - 0.5 * vector2
print(f'Vector 1: {vector1}')
print(f'Vector 2: {vector2}')
print(f'Suma de vectores: {suma_vector}')
print(f'Combinación lineal: {combinacion_lineal}\n')

# Matriz
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
suma_matriz = matriz1 + matriz2
transpuesta_matriz1 = matriz1.T
suma_transpuesta = matriz1 + matriz1.T
transpuesta_transpuesta = matriz1.T.T
print(f'Matriz 1:\n{matriz1}')
print(f'Matriz 2:\n{matriz2}')
print(f'Suma de matrices:\n{suma_matriz}')
print(f'Transpuesta de Matriz 1:\n{transpuesta_matriz1}')
print(f'Suma de Matriz 1 con su transpuesta:\n{suma_transpuesta}')
print(f'Transpuesta de la transpuesta de Matriz 1:\n{transpuesta_transpuesta}\n')

# Tensor
tensor1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
tensor2 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])
suma_tensor = tensor1 + tensor2
print(f'Tensor 1:\n{tensor1}')
print(f'Tensor 2:\n{tensor2}')
print(f'Suma de tensores:\n{suma_tensor}')
