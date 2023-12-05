import numpy as np

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[-1, 0], [2, 1]])
C = np.array([[5, 6], [7, 8]])
c = 2

print(f"A.shape: {A.shape}")
print(f"len(matriz): {len(A)}")


# Operaciones
suma_matriz = A + B
resta_matriz = A - B
multiplicacion_escalar_matriz = c * A
producto_matrices = np.dot(A, B)

# Transposición de la multiplicación de matrices
transposed_product_AB = producto_matrices.T

# Multiplicación de matrices transpuestas
transposed_BA = np.dot(B.T, A.T)



# Operación de Transposición
transpuesta_A = A.T
transpuesta_B = B.T

# Producto Punto (Producto Interno)
producto_punto_matrices = np.sum(A * B)

# Producto Cruz (en matrices, sería un producto elemento a elemento)
producto_cruz_matrices = A * B

# 1. Propiedad Asociativa:
# Verificación de la propiedad asociativa
left_associative = A.dot(B.dot(C))
right_associative = (A.dot(B)).dot(C)

# 2. Propiedad Distributiva:
# Verificación de la propiedad distributiva
left_distributive = A.dot(B + C)
right_distributive = A.dot(B) + A.dot(C)

# 3. Propiedad Conmutativa (NO es válida para la multiplicación de matrices):
product_AB = A.dot(B)
product_BA = B.dot(A)


# Resultados
print(f"Suma de matrices:\n{suma_matriz}")
print(f"Resta de matrices:\n{resta_matriz}")
print(f"Multiplicación por escalar:\n{multiplicacion_escalar_matriz}")
print(f"Producto de matrices:\n{producto_matrices}")
print(f"Transpuesta de A:\n{transpuesta_A}")
print(f"Transpuesta de B:\n{transpuesta_B}")

print(f"Producto Punto de A y B: {producto_punto_matrices}")
print(f"Producto Cruz de A y B (elemento a elemento):\n{producto_cruz_matrices}")

# Propiedad Asociativa
print(f"A · (B · C):\n{left_associative}")
print(f"(A · B) · C:\n{right_associative}")
print("¿La propiedad es asociativa?", np.allclose(left_associative, right_associative))

# Propiedad Distributiva
print(f"A · (B + C):\n{left_distributive}")
print(f"A · B + A · C:\n{right_distributive}")
print("¿La propiedad es distributiva?", np.allclose(left_distributive, right_distributive))

# Propiedad Conmutativa (NO es válida para la multiplicación de matrices)
print(f"A · B:\n{product_AB}")
print(f"B · A:\n{product_BA}")
print("¿La propiedad es conmutativa?", np.array_equal(product_AB, product_BA))

print(f"(A · B)^T:\n{transposed_product_AB}")
print(f"B^T · A^T:\n{transposed_BA}")
print("¿Se cumple la propiedad?", np.array_equal(transposed_product_AB, transposed_BA))