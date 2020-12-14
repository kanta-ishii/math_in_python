'''
データの傾向モデル：Y=f(X)
X={x1, x2, x3, •••, xn}
Y={y1, y2, y3, •••, ym}
    Yの各値：連続値　→　回帰　
    Yの各値：離散値　→　分類　ex) 0,1みたいな

<多項式を当てはめて多項式回帰>
       n
f(x) = Σ a*k x**k
      k=0

最小二乗法：二乗和Jを最小にする、関数f(x)のパラメータを求める
    m
J = Σ(f(xj)-tj)**2
   j=1

二乗和誤差：1/2をかけるのは微分する際に扱いやすくするため
         m
J = {1/2}Σ(f(xj)-tj)**2
        j=1

最急降下法：誤差を最小にする
'''
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi) #入力
T = np.sin(X) #データ
plt.plot(X, T)

T += 0.4*np.random.randn(len(X)) #正規分布に従うノイズを加える
plt.scatter(X, T) #ノイズの付加後

plt.show()

X /= np.pi #収束しやすくするため、Xの範囲を−１から１の間に収める
eta = 0.01 #学習係数


'''多項式'''
def polynomial(x, params):
    poly = 0
    for i in range(len(params)):
        poly += params[i]*x**i
    return poly

'''各パラメータの勾配'''
def grad_params(X, T, params):
    grad_ps = np.zeros(len(params))
    for i in range(len(params)):
        for j in range(len(X)):
            grad_ps[i] += (polynomial(X[j], params) -T[j])*X[j]**i
    return grad_ps

'''学習'''
def fit(X, T, degree, epoch): #degree:多項式, epoch:繰り返し回数
    params = np.random.randn(degree+1)
    for i in range(len(params)):
        params[i] *= 2**i 

    for i in range(epoch):
        params -= eta*grad_params(X, T, params)
    
    return params

'''結果'''
degrees = [1,3,6] #次数
for degree in degrees:
    params = fit(X, T, degree, 1000)
    Y = polynomial(X, params)
    plt.scatter(X,T)
    plt.plot(X, Y, linestyle='dashed')
    plt.show()

