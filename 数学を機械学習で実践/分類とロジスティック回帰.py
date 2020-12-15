'''
分類：0,1などの離散的な値を出力とする機械学習のモデルを使う

ロジスティック回帰
          1  
y = ----------------
    1+exp(Σ akxk +b)

パラメータの最適化
        　∂E 
ai ← ai -η---
          ∂ai
          ∂E
b  ←  b -η--
          ∂b
'''
import numpy as np
import matplotlib.pyplot as plt

n_data = 500 #データ数
X = np.zeros((n_data, 2)) #入力
T = np.zeros((n_data)) #正解

for i in range(n_data):
    x_rand = np.random.rand() # x座標
    y_rand = np.random.rand() # y座標
    X[i, 0] = x_rand
    X[i, 1] = y_rand
    if x_rand > y_rand +0.2*np.random.randn():
        T[i] = 1

plt.scatter(X[:, 0], X[:, 1], c=T)
plt.colorbar()
plt.show()

eta = 0.01 #学習係数

'''分類'''
def classify(x, a_params, b_params):
    u = np.dot(x, a_params) + b_params
    return 1/(1+np.exp(-u))

'''交差エントロピー誤差'''
def cross_entropy(Y, T):
    delta = 1e-7
    return -np.sum(T*np.log(Y+delta) +(1-T)*np.log(1-Y+delta))

'''各パラメータの勾配'''
def grad_a_params(X, T, a_params, b_param):
    grad_a = np.zeros(len(a_params))
    for i in range(len(a_params)):
        for j in range(len(X)):
            grad_a[i] += (classify(X[j], a_params, b_param) -T[j]) *X[j, i]
    return grad_a

def grad_b_param(X, T, a_params, b_param):
    grad_b = 0
    for i in range(len(X)):
        grad_b += (classify(X[i], a_params, b_param) -T[i])
    return grad_b

'''学習'''
error_x = []
error_y = []
def fit(X, T, dim, epoch):
    a_params = np.random.randn(dim)
    b_param = np.random.randn()

    for i in range(epoch):
        grad_a = grad_a_params(X, T, a_params, b_param)
        grad_b = grad_b_param(X, T, a_params, b_param)
        a_params -= eta *grad_a
        b_param -= eta *grad_b

        Y = classify(X, a_params, b_param)
        error_x.append(i) #誤差の記録
        error_y.append(cross_entropy(Y, T)) #誤差の記録
    return (a_params, b_param)

a_params, b_param = fit(X, T, 2, 200)
Y = classify(X, a_params, b_param)

result_x = [] #x座標
result_y = [] #y座標
result_z = [] #確率
for i in range(len(Y)):
    result_x.append(X[i, 0])
    result_y.append(X[i, 1])
    result_z.append(Y[i])
    
print('---確率分布---')
plt.scatter(result_x, result_y, c=result_x)
plt.colorbar()
plt.show()

print('---誤差の推移---')
plt.plot(error_x, error_y)
plt.xlabel('Epoch', size=14)
plt.ylabel('Cross entropy', size=14)
plt.show()