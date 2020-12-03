import numpy as np
import matplotlib.pyplot as plt

x = np.array([50, 70, 40, 60, 80]) #数学の点数
y = np.array([60, 80, 50, 50, 70]) #英語の点数
z = np.array([60, 40, 60, 40, 30]) #国語の点数

cov_xy = np.average((x-np.average(x))*(y-np.average(y)))
print('cov_xy', cov_xy)

cov_xz = np.average((x-np.average(x))*(z-np.average(z)))
print('cov_xz', cov_xz)

plt.scatter(x, y, marker='o', label='xy', s=40)
plt.scatter(x, z, marker='x', label='xz', s=60)
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()