import numpy as np
import matplotlib.pyplot as plt

data = np.array([0,1,1,2,2,2,3,3,4,5,6,6,7,7,7,8,8,9])

plt.hist(data, bins=10) #binsは柱の数
plt.show()
