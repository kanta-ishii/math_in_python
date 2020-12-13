'''
交差エントロピー：確率分布がどれだけあるべき値と離れているかを表す尺度
'''

import numpy as np

delta = 1e-7 #微小な値

def cross_entropy(p, t):
    return -np.sum(t*np.log(p+delta) +(1-t)*np.log(1-p+delta)) #交差エントロピー

p_1 = np.array([0.2, 0.8, 0.1, 0.3, 0.9, 0.7]) #正解から離れている
p_2 = np.array([0.7, 0.3, 0.9, 0.8, 0.1, 0.2]) #正解に近い

t = np.array([1,0,1,1,0,0]) #正解

print('---予測と正解から離れている---')
print(cross_entropy(p_1, t))
print('---予測と正解に近い---')
print(cross_entropy(p_2, t))