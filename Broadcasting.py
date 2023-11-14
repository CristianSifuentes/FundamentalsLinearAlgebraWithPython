import numpy as np

# Matriz de tamaño (2, 3)
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Vector de tamaño (3,)
vector = np.array([10, 20, 30])

# Broadcasting en la suma
resultado = matriz + vector

# Imprimir resultados
print("Matriz:\n", matriz)
print("\nVector:\n", vector)
print("\nResultado de la suma usando broadcasting:\n", resultado)
'''
En este ejemplo, el vector [10, 20, 30] se expande automáticamente a lo largo de la dimensión 0 
para que coincida con el tamaño de la matriz (2, 3). La suma se realiza elemento por elemento, y 
el resultado es una matriz del mismo tamaño (2, 3).

Broadcasting simplifica el código y hace que las operaciones sean más eficientes y 
legibles al evitar la necesidad de expandir manualmente las dimensiones. 
Sin embargo, es importante entender las reglas de broadcasting para usarlo
 correctamente en tus operaciones.
'''
