import matplotlib.pyplot as plt

# Coordenadas del punto de inicio
x = [0, 0, 0]
y = [0, 0, 0]

# Componentes x e y de los vectores
u = [1, -2, 3]
v = [2, 1, -1]

# Crear el gráfico de vectores
plt.quiver(x, y, u, v, scale=1, angles='xy', scale_units='xy', color=['r', 'g', 'b'])

# Configuraciones adicionales
plt.xlim(-3, 4)
plt.ylim(-3, 4)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Vectores')
plt.grid(True)
plt.show()
