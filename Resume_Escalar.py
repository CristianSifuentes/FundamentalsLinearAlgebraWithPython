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




escalar = 3.1
print(escalar.shape)

