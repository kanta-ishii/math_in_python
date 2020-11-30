from matplotlib import lines
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
total = 0 #試行数
num_5 = 0 #5が出た回数
n = 50000 #サイコロを振る回数

for i in range(n):
    if np.random.randint(6)+1 == 5:
        num_5 += 1

    total += 1
    x.append(i)
    y.append(num_5/total)

plt.plot(x, y)
plt.plot(x, [1/6]*n, linestyle='dashed')

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()  

plt.show()