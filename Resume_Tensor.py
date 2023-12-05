import numpy as np
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