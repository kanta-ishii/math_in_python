import numpy as np
import matplotlib.pyplot as plt

def show_cov(cov):
    print('---Covariance.:{}---'.format(cov))
    average = np.array([0,0]) #xとyのそれぞれの平均
    cov_matrix = np.array([[1,cov],[cov,1]]) #共分散を行列で指定

    #共分散からペアのデータを3000組生成。dataは(3000,2)の形状の行列になる
    data = np.random.multivariate_normal(average, cov_matrix, 3000)
    x = data[:, 0] #最初の列をx座標に
    y = data[:, 1] #次の列をy座標に

    plt.scatter(x, y, marker='x', s=20)

    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    plt.grid()

    plt.show()

show_cov(0.6) #共分散: 0.6
show_cov(0.) #共分散: 0.0
show_cov(-0.6) #共分散: -0.6