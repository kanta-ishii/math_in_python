import numpy as np
import matplotlib.pyplot as plt

# パレート分布に従う乱数の生成
s = np.random.pareto(4, 1000) # a:4, m:1, 1000個

plt.hist(s, bins=25)

plt.xlabel('x', size=14)
plt.grid()

plt.show()