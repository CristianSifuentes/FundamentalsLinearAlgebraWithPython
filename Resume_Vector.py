import numpy as np
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