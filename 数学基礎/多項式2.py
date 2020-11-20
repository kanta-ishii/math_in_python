import numpy as np
import matplotlib.pyplot as plt

#多項式計算
def f(x):
    return 4*x**3 + 2*x**2 + 2*x**2 + x + 3

x = np.linspace(-2,2)
y = f(x)

plt.plot(x,y)
plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()