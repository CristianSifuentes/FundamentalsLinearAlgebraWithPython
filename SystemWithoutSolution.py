import numpy as np
import matplotlib.pyplot as plt

# Sistema sin solución
A = np.array([[2, 1], [2, 1]])
b = np.array([4, 6])

plt.figure()

# Graficar las ecuaciones
x_vals = np.linspace(-10, 10, 100)
y1_vals = (b[0] - A[0, 0] * x_vals) / A[0, 1]
y2_vals = (b[1] - A[1, 0] * x_vals) / A[1, 1]

plt.plot(x_vals, y1_vals, label="2x + y = 4")
plt.plot(x_vals, y2_vals, label="2x + y = 6")

plt.title("Sistema sin solución")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
