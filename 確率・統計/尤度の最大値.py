import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([2.4, 1.2, 3.5, 2.1])

mu = np.average(x_data) #平均値
sigma = np.std(x_data) #標準偏差

def pdf(x, mu, sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2)) #確率密度関数

def log_likelihood(p):
    return np.sum(np.log(p)) #対数尤度

x_sigma = np.linspace(0.5, 8) #横軸に使う標準偏差
y_loglike = [] #横軸に使う対数度数

for s in x_sigma:
    log_like = log_likelihood(pdf(x_data, mu, s))
    y_loglike.append(log_like) #対数尤度を縦軸に追加

plt.plot(x_sigma, np.array(y_loglike))
plt.plot([sigma, sigma], [min(y_loglike), max(y_loglike)], linestyle='dashed') #データの標準偏差の位置に縦線を引く

plt.xlabel('x_sigma', size=14)
plt.ylabel('y_loglike', size=14)
plt.grid()

plt.show()
