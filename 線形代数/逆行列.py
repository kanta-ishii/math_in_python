import numpy as np

a = np.array([[1,2],[3,4]])
print(np.linalg.inv(a))

b = np.array([[1,2],[0,0]])
print(np.linalg.inv(b))