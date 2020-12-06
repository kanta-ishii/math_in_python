import numpy as np
import matplotlib.pyplot as plt

x = np.array([50, 70, 40, 60, 80]) #数学の点数
y = np.array([60, 80, 50, 50, 70]) #英語の点数

print('---corrcoef()関数を使用---')
print(np.corrcoef(x, y)) #相関係数

print('---共分散と標準偏差から求める---')
cov_xy = np.average((x-np.average(x)*(y-np.average(y)))) #共分散
print(cov_xy/(np.std(x)*np.std(y)))

plt.scatter(x, y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()