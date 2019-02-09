# 課題演習 Neu_2-4-2E.py

import numpy as np
import matplotlib.pyplot as plt

# +++++++++++++++++++ 座標 +++++++++++++++++++
X = np.arange(0.0, 1.0, 0.1) # 10個
Y = np.arange(0.1, 1.1, 0.1)
# +++++++++++++++++++ 教師信号：入力、正解データを作成 +++++++++++++++++++
input_data = []
correct_data = list(
[1,1,1,1,1,1,1,1,1,1,
 2,1,1,1,1,1,1,1,1,1,
 2,2,1,1,1,1,1,1,1,1,
 2,2,1,1,1,1,3,3,3,1,
 2,2,2,1,1,3,3,3,3,1,
 2,2,2,1,1,3,3,3,3,1,
 2,2,2,2,2,2,2,3,3,3,
 2,2,2,2,2,2,2,3,3,3,
 2,2,2,2,2,2,2,2,3,3,
 2,2,2,2,2,2,2,2,3,3] )
for y in Y:
    for x in X:
        input_data.append([x, y])

n_data = len(correct_data)  # データ数  100個
input_data = np.array(input_data)
correct_data = np.array(correct_data)

print(input_data.shape)
print(correct_data.shape)
# +++++++++++++++++++ 各設定値 +++++++++++++++++++
IN_Neuron  = 2  # 入力層のニューロン数
Mid_Neuron = 7  # 中間層のニューロン数
Out_Neuron = 3  # 出力層のニューロン数

wb_width = 0.01  # 重みとバイアスの広がり具合
eta      = 0.1  # 学習係数
epoch    = 1001  # 101
interval = 500   # 経過の表示間隔 10

# +++++++++++++++++++ 中間層 +++++++++++++++++++
class MiddleLayer:
    def __init__(self, n, m):         # 初期設定(n=Mid_Neuron, m=InputOutSignal)
        self.w = np.array( [ [ -3.7, -6.3, -6.0, -13.1, -7.9, 7.9, -12.7], [ -2.4, 0.1, 0.6, -5.9, 1.6, -7.7, 9.7] ] )  # 重み    （2x7行列    ）W39
        self.b = np.array(  [ 0.2, 1.3, 1.0, 9.4, 0.8, -2.6, -1.7]  )     # バイアス（1x7ベクトル）B39

    def forward(self, x): # シグモイド関数  (1x6行列    ）U39, X39
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y = 1/(1+np.exp(-u))  


# +++++++++++++++++++ 出力層 +++++++++++++++++++
class OutputLayer:
    def __init__(self, n, m):         # 初期設定(n=Out_Neuron, m=MidOutSignal)
        self.w = np.array( [ [ 1.7, 0.8, -2.4], [ 0.2, 3.5, -3.7], [ 0.0, 3.4, -3.4], [ 7.2, -8.1, 0.9], [-1.0, 5.2, -4.1], [ 8.0, -5.6, -2.5], [ 0.0, 9.5, -9.5] ] )  # 重み     （7x3行列    ）Wxxii
        self.b = np.array( [-3.2, -0.7, 3.9] )       # バイアス （1x3ベクトル）Bxxii
    
    def forward(self, x): # ソフトマックス関数（1x2行列    ）Uxxii, abc
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y = np.exp(u)/np.sum(np.exp(u), axis=1, keepdims=True)  

# +++++++++++++++++++ 各層の初期化 +++++++++++++++++++
middle_layer = MiddleLayer(IN_Neuron, Mid_Neuron)
output_layer = OutputLayer(Mid_Neuron, Out_Neuron)



# +++++++++++++++++++ 学習 +++++++++++++++++++
kk=0
for k in range(epoch):#◆◆◆◆◆◆◆◆◆◆◆◆◆◆

    # 入力ベクトルのインデックスをシャッフル
    index_random = np.arange(n_data) # データ数  484個
    np.random.shuffle(index_random)
    
    # 結果の表示用
    total_error = 0
    x_1 = []
    y_1 = []
    x_2 = []
    y_2 = []
    x_3 = []
    y_3 = []
       
    #for jdx in index_random:#●●●●●●●●●●●●
    for jdx in range(11):#●●●●●●●●●●●●

        x = input_data[  jdx]  # 入力
        t0 = correct_data[jdx]  # 正解出力
        t = np.array([0,0,0])
        t[t0-1] = 1

        # 順伝播
        middle_layer.forward(x.reshape(1,2))
        output_layer.forward(middle_layer.y)

        
        if k%interval == 0:
            
            y = output_layer.y.reshape(-1)  # 行列をベクトルに戻す
            
            print("***+++++++++++++++++++++++++****************=", jdx)
            print(y[0], end="     ")
            print(y[1], end="     ")
            print(y[2])
            # 確率の大小を比較し、分類する
            if y[0] > y[1] and y[0] > y[2] :
                x_1.append(x[0])
                y_1.append(x[1])
            elif y[1] > y[0] and y[1] > y[2] :
                x_2.append(x[0])
                y_2.append(x[1])
            else:
                x_3.append(x[0])
                y_3.append(x[1])



    #●●●●●●●●●●●●
    if k%interval == 0:
        print("------------------------------------------------------", kk)
        print("****middle_layer.w********",middle_layer.w)
        print("****middle_layer.b********",middle_layer.b)
        print("****output_layer.w********",output_layer.w)
        print("****output_layer.b********",output_layer.b)
        kk = kk + 1

        # 出力のグラフ表示
        plt.plot(x_1, y_1, 'x')# 下の領域 x
        plt.plot(x_2, y_2, 'ro')
        plt.plot(x_3, y_3, 'g^')
        plt.show()
        
        # エポック数と誤差の表示
        print("Epoch:" + str(k) + "/" + str(epoch), "Error:" + str(total_error/n_data))
#◆◆◆◆◆◆◆◆◆◆◆◆◆◆
# ********************************************************************************************
