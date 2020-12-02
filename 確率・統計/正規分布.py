import numpy as np
import matplotlib.pyplot as plt

def pdf(x, mu, sigma): #mu: 平均値, sigma: 標準偏差
    return 1 / (sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2 / (2*sigma**2)) #確率密度関数

x = np.linspace(-5, 5)
y_1 = pdf(x, 0.0, 0.5) #平均値: 0, 標準偏差: 0.5
y_2 = pdf(x, 0.0, 1.) #平均値: 0, 標準偏差: 1
y_3 = pdf(x, 0.0, 2.) #平均値: 0, 標準偏差: 2

plt.plot(x, y_1, label='σ:0.5', linestyle='dashed')
plt.plot(x, y_2, label='σ:1.0', linestyle='solid')
plt.plot(x, y_3, label='σ:2.0', linestyle='dashdot')
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()