import numpy as np

'''乱数'''
r_num = np.random.randint(6)+1 #０〜５の乱数に1を足す
print(r_num)

r_dec = np.random.rand() #０から１の間の小数をランダムに返す
print(r_dec)

'''均一な乱数'''
import matplotlib.pyplot as plt

n = 1000 # サンプル数
x = np.random.rand(n) # 0-1の均一な乱数
y = np.random.rand(n) # 0-1の均一な乱数

plt.scatter(x,y)
plt.grid()
plt.show()

'''偏った乱数'''
import numpy as np
import matplotlib.pyplot as plt

n = 1000 # サンプル数
x = np.random.randn(n) # 0-1の均一な乱数
y = np.random.randn(n) # 0-1の均一な乱数

plt.scatter(x,y)
plt.grid()
plt.show()