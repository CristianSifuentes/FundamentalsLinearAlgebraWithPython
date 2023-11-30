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
#print(f"len(escalares): {len(a)}")




# Operaciones
suma = a + b
resta = a - b
multiplicacion = c * a
division = a / b if b != 0 else None

# Operación de Transposición
# ... (no aplica a escalares)
#print(f"Transpuesta escalar: {a.T}")
#AttributeError: 'float' object has no attribute 'T'

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
print(f"len(vector): {len(u)}")



# Operaciones
suma_vector = u + v
resta_vector = u - v
multiplicacion_escalar = c * v

# Operación de Transposición
transpuesta_u = u.T  # No tiene efecto en un vector


# Resultados
print(f"Suma de vectores: {suma_vector}")
print(f"Resta de vectores: {resta_vector}")
print(f"Multiplicación por escalar: {multiplicacion_escalar}")
print(f"Transpuesta de u: {transpuesta_u}")



# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[-1, 0], [2, 1]])
c = 2

print(f"A.shape: {A.shape}")
print(f"len(matriz): {len(A)}")


# Operaciones
suma_matriz = A + B
resta_matriz = A - B
multiplicacion_escalar_matriz = c * A
producto_matrices = np.dot(A, B)

# Operación de Transposición
transpuesta_A = A.T
transpuesta_B = B.T


# Resultados
print(f"Suma de matrices:\n{suma_matriz}")
print(f"Resta de matrices:\n{resta_matriz}")
print(f"Multiplicación por escalar:\n{multiplicacion_escalar_matriz}")
print(f"Producto de matrices:\n{producto_matrices}")
print(f"Transpuesta de A:\n{transpuesta_A}")
print(f"Transpuesta de B:\n{transpuesta_B}")

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Tensor tridimensional
tensor = np.fromfunction(lambda i, j, k: i + j + k, (3, 3, 3), dtype=int)

tensor.shape
print(f"tensor.shape: {tensor.shape}")
print(f"len(tensor): {len(tensor)}")


# Operaciones
suma_tensores = tensor + tensor
multiplicacion_escalar_tensor = 2 * tensor
contraccion_tensor = np.sum(tensor, axis=2)

# Operación de Transposición
transpuesta_tensor = tensor.T

# Resultados
print(f"Suma de tensores:\n{suma_tensores}")
print(f"Multiplicación por escalar:\n{multiplicacion_escalar_tensor}")
print(f"Contracción de tensor:\n{contraccion_tensor}")
print(f"Transpuesta de tensor:\n{transpuesta_tensor}")
