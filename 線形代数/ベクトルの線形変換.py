import numpy as np
import matplotlib.pyplot as plt

a = np.array([2,3])
A = np.array([[2,-1],[2,-2]])
b = np.dot(A,a)

print('変換前のベクトル (a) :',a)
print('変換前のベクトル (b) :',b)

def arrow(start, size, color):
    plt.quiver(start[0], start[1], size[0], size[1], angles='xy', scale_units='xy', scale=1, color=color)

s = np.array([0,0])

arrow(s, a, color='black')
arrow(s, b, color='black')

plt.xlim([-3,3])
plt.ylim([-3,3])
plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()
plt.axes().set_aspect('equal')
plt.show()