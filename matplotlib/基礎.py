# %matplotlib inline  ← jupyterだと記述が必要なときもあるようだ

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5) #ある空間を等間隔で50個に分けてくれる
x_sample = np.linspace(1,50) #わかりやすい例

y = 2 * x
plt.plot(x,y)
plt.show()


# print(x)
# print(x_sample)
# print(len(x_sample))