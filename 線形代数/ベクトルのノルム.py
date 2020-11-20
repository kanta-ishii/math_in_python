'''
L2
    ベクトルの各要素を2乗和し平方根をとる
L1
    ベクトルの各要素の絶対値を足し合わせて
'''

import numpy as np

a = np.array([1,1,-1,-1])

'''L2ノルム'''
print(np.linalg.norm(a))

'''L1ノルム'''
print(np.linalg.norm(a, 1))