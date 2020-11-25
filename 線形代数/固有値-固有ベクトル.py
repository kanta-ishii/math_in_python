import numpy as np

a = np.array([[3,1],[2,4]])

ev = np.linalg.eig(a) #固有値と固有ベクトルを同時に求める

print(ev[0])

print(ev[1])