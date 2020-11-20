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
def tan(x):
    return np.tan(x) # tanθ = tan(x)

x = np.linspace(-1.3, 1.3)
tan_y = tan(x)

plt.plot(x, tan_y, label='tan')
plt.legend()

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.show()