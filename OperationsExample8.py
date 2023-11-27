import matplotlib.pyplot as plt

'''
axvline y axhline:

axvline crea una línea vertical en un gráfico en una posición específica del eje x.
axhline crea una línea horizontal en un gráfico en una posición específica del eje y.
'''

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear un gráfico de dispersión
plt.scatter(x, y)

# Dibujar líneas verticales y horizontales
plt.axvline(x=3, color='r', linestyle='--')  # Línea vertical en x=3
plt.axhline(y=8, color='g', linestyle=':')   # Línea horizontal en y=8

# Mostrar el gráfico
plt.show()
