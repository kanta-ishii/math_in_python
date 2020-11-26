import numpy as np
import matplotlib.pyplot as plt

def my_func(x):
    return 3*x**2 +4*x -5

def my_func_dif(x): # 導関数
    return 6*x +4

x = np.linspace(-3,3)
y = my_func(x)

a = 1
y_t = my_func_dif(a) * x + my_func(a) - my_func_dif(a) * a

plt.plot(x, y, label='y')
plt.plot(x, y_t, label='y_t')
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()