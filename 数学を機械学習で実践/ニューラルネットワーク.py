'''
・機械学習アルゴリズム
    ・機械学習
    ・遺伝的アルゴリズム
    ・群知能
    ・ファジイ制御
    ・強化学習
    ・決定木
    ・サポートベクターマシン
    ・K近傍法
    ・ニューラルネットワーク

<ニューロンの順伝播の式>
u = wx +b
y = f(u)

x: 入力
y: 出力
w: 重み
b: バイアス
f: 活性化関数
'''

'''正解データの用意'''
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi/2, np.pi/2) #入力: -π/2からπ/2の範囲
T = (np.sin(X) +1)/2 #正解: 0から1までの範囲
n_data = len(T)

'''順伝播'''
def forward(x, w, b):
    u = x*w +b
    y = 1/(1+np.exp(-u))
    return y

'''逆伝播'''
def backword(x, y, t):
    delta = (y -t)*(1 -y)*y
    grad_w = x*delta #重みの勾配
    grad_b = delta #バイアスの勾配
    return (grad_w, grad_b)
    
def show_output(X, Y, T, epoch):
    plt.plot(X, T, linestyle='dashed')
    plt.scatter(X, Y, marker='+')

    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    plt.grid()
    plt.show()

    print('Epoch:', epoch)
    print('Error:', 1/2*np.sum((Y -T)**2)) #二乗和誤差を表示

#固定値
eta = 0.1 #学習係数
epoch = 100 #エポック数

#初期値
w = 0.2 #重み
b = -0.2 #バイアス

'''学習'''
for i in range(epoch):
    if i < 10:
        Y = forward(X, w, b)
        show_output(X, Y, T, i)
        idx_rand = np.arange(n_data)
        np.random.shuffle(idx_rand)
        for j in idx_rand: #ランダムなサンプル
            x = X[j] #入力
            t = T[j] #正解
            y = forward(x, w, b) #順伝播
            grad_w, grad_b = backword(x, y, t) #逆伝播
            w -= eta * grad_w #重みの更新
            b -= eta * grad_b #バイアスの更新

'''結果を表示'''
Y = forward(X, w, b)
show_output(X, Y, T, epoch)