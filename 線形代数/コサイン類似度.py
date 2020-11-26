'''ベクトル同士の向きの近さを表す'''

import numpy as np

def cos_sim(vec_1, vec_2):
    return np.dot(vec_1, vec_2) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))

a = np.array([2,2,2,2])
b = np.array([1,1,1,1])
c = np.array([-1,-1,-1,-1])

print(cos_sim(a, b))
print(cos_sim(a, c))
'''↑ベクトルの向きがどれだけ揃っているかの指標になる'''