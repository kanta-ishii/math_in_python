import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 1) # ０の対数は取れない　→　0.01
y = -np.log2(x) # 洗濯情報量

plt.plot(x, y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()