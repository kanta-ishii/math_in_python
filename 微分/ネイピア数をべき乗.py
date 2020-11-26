import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2)
y = np.exp(x)

plt.plot(x, y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()