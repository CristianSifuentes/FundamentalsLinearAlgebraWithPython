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

# Producto Punto
producto_punto = np.dot(u, v)

# Resultados
print(f"Suma de vectores: {suma_vector}")
print(f"Resta de vectores: {resta_vector}")
print(f"Multiplicación por escalar: {multiplicacion_escalar}")
print(f"Transpuesta de u: {transpuesta_u}")
print(f"Producto Punto de u y v: {producto_punto}")

# Vectores en 3D
w = np.array([1, 2, 3])
x = np.array([4, 5, 6])

# Producto Cruz
producto_cruz = np.cross(w, x)

# Resultados
print(f"Producto Cruz de w y x: {producto_cruz}")

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

# Producto Punto (Producto Interno)
producto_punto_matrices = np.sum(A * B)

# Producto Cruz (en matrices, sería un producto elemento a elemento)
producto_cruz_matrices = A * B

# Resultados
print(f"Suma de matrices:\n{suma_matriz}")
print(f"Resta de matrices:\n{resta_matriz}")
print(f"Multiplicación por escalar:\n{multiplicacion_escalar_matriz}")
print(f"Producto de matrices:\n{producto_matrices}")
print(f"Transpuesta de A:\n{transpuesta_A}")
print(f"Transpuesta de B:\n{transpuesta_B}")

# Resultados
print(f"Producto Punto de A y B: {producto_punto_matrices}")
print(f"Producto Cruz de A y B (elemento a elemento):\n{producto_cruz_matrices}")

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Tensor tridimensional
tensor = np.fromfunction(lambda i, j, k: i + j + k, (3, 3, 3), dtype=int)

tensor.shape
print(f"tensor.shape: {tensor.shape}")
print(f"len(tensor): {len(tensor)}")

# Tensor tridimensional
tensor_A = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
tensor_B = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])

# Producto Tensorial
producto_tensorial = np.tensordot(tensor_A, tensor_B, axes=0)

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
# Resultados
print(f"Producto Tensorial de A y B:\n{producto_tensorial}")