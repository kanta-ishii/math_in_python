import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 1) # ０の対数は取れない　→　0.01から0.99の範囲に
y = -x*np.log2(x) - (1-x)*np.log2(1-x) # 平均情報量

plt.plot(x, y)

plt.xlabel('x', size=14)
plt.ylabel('y', size=14)
plt.grid()

plt.show()