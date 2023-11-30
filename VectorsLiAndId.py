import numpy as np
import matplotlib.pyplot as plt


v1 = np.array([1,0])
v2 = np.array([2, -3])

print(v1)
print(v2)

for a in range(-10,10):
    for b in range(-10, 10):
        # print(v1[0]*a+v2[0]*b)
        # print(v1[1]*a+v2[1]*b)
        plt.scatter(v1[0]*a+v2[0]*b, v1[1]*a+v2[1]*b,
                   marker = '.',
                   color = 'orange')
plt.show()
