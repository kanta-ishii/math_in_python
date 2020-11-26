import numpy as np
import matplotlib.pyplot as plt

def my_func(x): #最小値を求める関数
    return x**2 -2*x

def grad_func(x): # 導関数
    return 2*x -2

eta = 0.1
x = 4.
record_x = []
record_y = []
for i in range(20):
    y = my_func(x)
    record_x.append(x)
    record_y.append(y)
    x -= eta * grad_func(x)

x_f = np.linspace(-2, 4)
y_f = my_func(x_f)

plt.plot(x_f, y_f, linestyle='dashed')
plt.scatter(record_x, record_y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()