import numpy as np
import matplotlib.pyplot as plt

s = np.random.normal(0, 1, 10000) #平均:0, 標準偏差:1, 10000個

#ヒストグラム
plt.hist(s, bins=25) #binsは棒の数

plt.xlabel('x', size=14)
plt.grid()

plt.show()