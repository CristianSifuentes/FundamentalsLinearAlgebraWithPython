import numpy as np
escalar = 5.4324
print(escalar)

escalar_python = True
print(escalar_python)
print(type(escalar_python))



import numpy as np

# Escalar
escalar = np.array(5)
print("Escalar:")
print(f"Valor: {escalar}")
print(f"Tamaño (size): {escalar.size}")
print(f"Forma (shape): {escalar.shape}\n")

# Vector
vector = np.array([1, 2, 3])
print("Vector:")
print(f"Valores: {vector}")
print(f"Tamaño (size): {vector.size}")
print(f"Longitud (len): {len(vector)}")
print(f"Forma (shape): {vector.shape}\n")

# Matriz
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:")
print(f"Valores:\n{matriz}")
print(f"Tamaño (size): {matriz.size}")
print(f"Longitud (len): {len(matriz)}")
print(f"Forma (shape): {matriz.shape}\n")

# Tensor
tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Tensor:")
print(f"Valores:\n{tensor}")
print(f"Tamaño (size): {tensor.size}")
print(f"Longitud (len): {len(tensor)}")
print(f"Forma (shape): {tensor.shape}\n")

