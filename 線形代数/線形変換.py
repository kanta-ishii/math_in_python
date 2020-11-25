'''
quiver (始点のx座標, 始点のy座標, 矢印のx成分, 矢印のy成分
        angles = 矢印の角度の決定方法,
        scale_units = スケールの単位,
        scale = スケール,
        color = 矢印の色
        )
'''

import numpy as np
import matplotlib.pyplot as plt

def arrow(start, size, color):
    plt.quiver(start[0], start[1], size[0], size[1], angles='xy', scale_units='xy', scale=1, color=color)

#矢印の始点
s = np.array([0,0]) #原点

a = np.array([2,3]) #縦のベクトルを表す

arrow(s,a,color='black')

plt.xlim([-3,3])
plt.ylim([-3,3])
plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.axes().set_aspect('equal')
plt.show()