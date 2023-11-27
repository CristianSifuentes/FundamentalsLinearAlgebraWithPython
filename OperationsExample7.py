import matplotlib.pyplot as plt

'''
xlim y ylim:

xlim se utiliza para establecer los límites del eje x en un gráfico.
ylim se utiliza para establecer los límites del eje y en un gráfico.
'''
# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear un gráfico de dispersión
plt.scatter(x, y)

# Establecer límites de ejes
plt.xlim(0, 6)
plt.ylim(0, 12)

# Mostrar el gráfico
plt.show()
