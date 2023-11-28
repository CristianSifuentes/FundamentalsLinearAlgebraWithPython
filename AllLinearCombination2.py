import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2,5])
v2 = np.array([3,2])

for a in range(-10,10):
    for b in range(-10,10):
        plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a + v2[1]*b,
                   marker = '.',
                   color = "orange")
        
plt.xlim(-100,100)
plt.ylim(-100,100)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')

plt.show()