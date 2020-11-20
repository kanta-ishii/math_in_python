import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.2, 2.4, 0.0, 1.4, 1.5, 0.3, 0.7])
y = np.array([2.4, 1.4, 1.0, 0.1, 1.7, 2., 0.6])

plt.scatter(x, y)
plt.grid()
plt.show()