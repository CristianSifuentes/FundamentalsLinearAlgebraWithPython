import numpy as np
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Vectores
u = np.array([2, 3])
v = np.array([-1, 5])

vector = np.array([1/2,1/2,1/2,1/2])

vector2 =  np.array([-50,-25,0,25,100,-300])
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


# Normas
# Vector
# v = np.array([3, -4])

# Norma L1
norm_l1 = np.linalg.norm(v, ord=1)

# Norma L2 (por defecto)
norm_l2 = np.linalg.norm(v)

# Norma L0
norm_l0 = np.linalg.norm(v, ord=0)

# Norma al cuadrado (L2 al cuadrado)
norm_squared = np.sum(v**2)

# Norma infinito
norm_inf = np.linalg.norm(v, ord=np.inf)

# Resultados
print(f"Vector: {v}")
print(f"Norma L1: {norm_l1}")
print(f"Norma L2: {norm_l2}")
print(f"Norma L0: {norm_l0}")
print(f"Norma al cuadrado: {norm_squared}")
print(f"Norma infinito: {norm_inf}")


no = np.linalg.norm(vector)
no2 = np.linalg.norm(vector2, ord=0)



print(no)
print(no2)