import numpy as np

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Escalares
a = 5
b = 3
c = 2
#print(f"a.shape: {a.shape}")
#AttributeError: 'int' object has no attribute 'shape'

# Operaciones
suma = a + b
resta = a - b
multiplicacion = c * a
division = a / b if b != 0 else None

# Resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")



# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Vectores
u = np.array([2, 3])
v = np.array([-1, 5])
c = 2

print(f"u.shape: {u.shape}")


# Operaciones
suma_vector = u + v
resta_vector = u - v
multiplicacion_escalar = c * v

# Resultados
print(f"Suma de vectores: {suma_vector}")
print(f"Resta de vectores: {resta_vector}")
print(f"Multiplicación por escalar: {multiplicacion_escalar}")



# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[-1, 0], [2, 1]])
c = 2

print(f"A.shape: {A.shape}")


# Operaciones
suma_matriz = A + B
resta_matriz = A - B
multiplicacion_escalar_matriz = c * A
producto_matrices = np.dot(A, B)

# Resultados
print(f"Suma de matrices:\n{suma_matriz}")
print(f"Resta de matrices:\n{resta_matriz}")
print(f"Multiplicación por escalar:\n{multiplicacion_escalar_matriz}")
print(f"Producto de matrices:\n{producto_matrices}")


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Tensor tridimensional
tensor = np.fromfunction(lambda i, j, k: i + j + k, (3, 3, 3), dtype=int)

tensor.shape
print(f"tensor.shape: {tensor.shape}")


# Operaciones
suma_tensores = tensor + tensor
multiplicacion_escalar_tensor = 2 * tensor
contraccion_tensor = np.sum(tensor, axis=2)

# Resultados
print(f"Suma de tensores:\n{suma_tensores}")
print(f"Multiplicación por escalar:\n{multiplicacion_escalar_tensor}")
print(f"Contracción de tensor:\n{contraccion_tensor}")