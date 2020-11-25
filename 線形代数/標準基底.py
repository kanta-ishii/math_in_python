import numpy as np
import matplotlib.pyplot as plt

a = np.array([2,3])
e_x = np.array([1,0]) # 基準基底
e_y = np.array([0,1]) # 基準基底

def arrow(start, size, color):
    plt.quiver(start[0], start[1], size[0], size[1], angles='xy', scale_units='xy', scale=1, color=color)

s = np.array([0,0])

arrow(s, a, color='blue')
arrow(s, e_x, color='black')
arrow(s, e_y, color='black')

plt.xlim([-3,3])
plt.ylim([-3,3])
plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.axes().set_aspect('equal')
plt.show()