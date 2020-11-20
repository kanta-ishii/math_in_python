import numpy as np
import matplotlib.pyplot as plt

#べき乗関数
def f(x):
    a = 3
    return x**a

x = np.linspace(0,2)
y = f(x)

plt.plot(x,y)
plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()
