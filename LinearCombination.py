import numpy as np
import matplotlib.pyplot as plt

def graficar_vector(vector, color, label):
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

# Definir dos vectores en el plano xy
v1 = np.array([2, 1])
v2 = np.array([-1, 3])

# Definir coeficientes para la combinación lineal
c1 = 3
c2 = -1

# Calcular la combinación lineal
combinacion_lineal = c1 * v1 + c2 * v2

# Crear el gráfico de los vectores y la combinación lineal
plt.figure()

# Llamar a la función para graficar los vectores
graficar_vector(v1, 'b', 'v1')
graficar_vector(v2, 'r', 'v2')
graficar_vector(combinacion_lineal, 'g', '3v1 - v2')

# Configuraciones adicionales
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Combinación Lineal de Vectores')
plt.show()
