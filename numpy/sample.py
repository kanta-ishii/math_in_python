import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6]])
z = np.zeros(8)
o = np.ones(8)
f = np.arange(8)



print(a)
print(a[3])
print(a+3)
print(b)
print(b[1][2])
print(b[1,2])#上記と同じ
b[0,2] = 9
print(b[1,:])
b[1,:] = np.array([7,8,9])
print(b)
print('合計:',np.sum(b))
print('平均:',np.average(b))
print('最大値:',np.max(b))
print('最小値:',np.min(b))
print(z)
print(o)
print(f)
