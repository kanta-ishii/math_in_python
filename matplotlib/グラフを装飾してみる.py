'''
グラフを装飾してみよう
    ・軸のラベル
    ・グラフのタイトル
    ・グリッドの表示
    ・凡例を線のスタイル
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5)
y_1 = 2*x
y_2 = 3*x

plt.xlabel("x value", size=14) #size = 軸ラベルの文字の大きさを14にする
plt.ylabel("y value", size=14)

plt.title('My graph') #グラフタイトルを入れる

plt.grid() #グリッド線を入れる

plt.plot(x, y_1, label='y1')
plt.plot(x, y_2, label='y2', linestyle='dashed')
plt.legend()

plt.show()
