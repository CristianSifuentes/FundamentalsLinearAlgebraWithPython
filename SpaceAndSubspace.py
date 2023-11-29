import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1,1])
v2 = np.array([-1, -1])

print(v1)
print(v2)

for a in range(-10,10):
    for b in range(-10, 10):
        # print(v1[0]*a+v2[0]*b)
        # print(v1[1]*a+v2[1]*b)
        plt.scatter(v1[0]*a+v2[0]*b, v1[1]*a+v2[1]*b,
                   marker = '.',
                   color = 'orange')
        
plt.xlim(-25,25)
plt.ylim(-25,25)

plt.axvline(x=0, color = "grey")
plt.axhline(y=0, color = "grey")

plt.show()


print(v1 == -1 * v2)