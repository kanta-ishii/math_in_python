import numpy as np
import matplotlib.pyplot as plt

#平方根計算
def f(x):
    return np.sqrt(x)

x = np.linspace(0,9)
y = f(x)

plt.plot(x,y)
plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()