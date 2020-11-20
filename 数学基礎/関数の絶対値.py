import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi)
sin_y = np.abs(np.sin(x))
cos_y = np.abs(np.cos(x))

plt.scatter(x, sin_y, label='sin')
plt.scatter(x, cos_y, label='cos')
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()