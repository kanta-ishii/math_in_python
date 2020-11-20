'''
三角関数
    底辺=a, 高さ=b, 辺=c, 鋭角=θ, 直角あり
    sinθ = b/c
    cosθ = a/c
    tanθ = b/a
    (sinθ)**2 + (cosθ)**2 = 1
    tanθ = sinθ/cosθ

※ sin() は cos() をx方向にπ/2だけずらしたもの
'''

import numpy as np
import matplotlib.pyplot as plt

#三角関数計算
def sin(x):
    return np.sin(x) # sinθ = sin(x)

def cos(x):
    return np.cos(x) # cosθ = cos(x)

x = np.linspace(-np.pi, np.pi) #円周率を取得
sin_y, cos_y = sin(x), cos(x)


plt.plot(x, sin_y, label='sin')
plt.plot(x, cos_y, label='cos')
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()