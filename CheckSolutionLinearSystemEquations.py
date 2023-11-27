import numpy as np
import matplotlib.pyplot as plt
'''
matplotlib se utiliza principalmente para crear visualizaciones, mientras que la resolución de sistemas de ecuaciones 
lineales implica más el uso de álgebra lineal y técnicas numéricas. Sin embargo, 
puedo mostrarte un ejemplo básico donde visualizo gráficamente un sistema de 
ecuaciones lineales y resalto la solución utilizando axvline y axhline. 

Ten en cuenta que este método solo es práctico para sistemas de dos ecuaciones con dos incógnitas.
'''

# Definir el sistema de ecuaciones lineales
# 2x + y = 5
# -x + 2y = 3

# Crear un rango de valores para x
x_values = np.linspace(-2, 4, 100)

# Definir las ecuaciones
y1_values = 5 - 2 * x_values  # 2x + y = 5
y2_values = (3 + x_values) / 2  # -x + 2y = 3

# Crear el gráfico
plt.plot(x_values, y1_values, label='2x + y = 5')
plt.plot(x_values, y2_values, label='-x + 2y = 3')

# Marcar la solución (x, y)
solucion_x = 2
solucion_y = 1
plt.scatter(solucion_x, solucion_y, color='red')  # Marcar la solución en rojo

# Configurar límites de ejes
plt.xlim(-2, 4)
plt.ylim(-2, 4)

# Agregar líneas verticales y horizontales que pasan por la solución
plt.axvline(x=solucion_x, color='gray', linestyle='--')
plt.axhline(y=solucion_y, color='gray', linestyle='--')

# Etiquetas y leyenda
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Mostrar el gráfico
plt.show()

'''
En este ejemplo, he graficado dos ecuaciones lineales y he marcado visualmente el punto de intersección, 
que es la solución del sistema. Las líneas verticales y horizontales que pasan por la solución 
se han agregado con axvline y axhline. Ten en cuenta que este es solo un ejemplo gráfico y
 que para sistemas más complejos o con más ecuaciones, las técnicas de álgebra lineal y 
 métodos numéricos son más apropiados para encontrar la solución.
'''
