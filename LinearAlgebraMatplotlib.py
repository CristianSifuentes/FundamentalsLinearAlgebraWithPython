import numpy as np
import matplotlib.pyplot as plt

# Crear vectores
vector1 = np.array([1, 2])
vector2 = np.array([-2, 1])

# Suma de vectores
resultant_vector = vector1 + vector2

# Configuración del gráfico
fig, ax = plt.subplots()
ax.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 1')
ax.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector 2')
ax.quiver(0, 0, resultant_vector[0], resultant_vector[1], angles='xy', scale_units='xy', scale=1, color='r', label='Sum')

# Establecer límites y etiquetas de ejes
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Mostrar una cuadrícula
ax.grid()

# Mostrar leyenda
ax.legend()

# Mostrar el gráfico
plt.show()
