import numpy as np
import matplotlib.pyplot as plt

# Sistema con infinitas soluciones
A = np.array([[2, 1], [4, 2]])
b = np.array([4, 8])

plt.figure()

# Graficar las ecuaciones
x_vals = np.linspace(-10, 10, 100)
y1_vals = (b[0] - A[0, 0] * x_vals) / A[0, 1]
y2_vals = (b[1] - A[1, 0] * x_vals) / A[1, 1]

plt.plot(x_vals, y1_vals, label="2x + y = 4")
plt.plot(x_vals, y2_vals, label="4x + 2y = 8")

plt.title("Sistema con infinitas soluciones")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
