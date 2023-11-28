import numpy as np
import matplotlib.pyplot as plt

def graficar_combinaciones_lineales(v1, v2):
    plt.figure()

    for c1 in range(-10, 11):
        for c2 in range(-10, 11):
            combinacion_lineal = c1 * v1 + c2 * v2
            print(combinacion_lineal)
            plt.quiver(0, 0, combinacion_lineal[0], combinacion_lineal[1], angles='xy', scale_units='xy', scale=1, color='b', alpha=0.3)

    # Configuraciones adicionales
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title('Todas las Combinaciones Lineales de dos Vectores')
    plt.show()

# Definir dos vectores en el plano xy
v1 = np.array([2, 1])
v2 = np.array([-1, 3])

# Llamar a la función para graficar todas las combinaciones lineales
graficar_combinaciones_lineales(v1, v2)
