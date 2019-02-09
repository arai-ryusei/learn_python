# 課題演習  Learning_Neu_0063.py   ( Neu_2-4-2E.py )

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
eta      = 0.05  # 学習係数
epoch    = 50001  # 101
interval = 2500   # 経過の表示間隔 10

# +++++++++++++++++++ 中間層 +++++++++++++++++++
class MiddleLayer:
    def __init__(self, n, m):         # 初期設定(n=Mid_Neuron, m=InputOutSignal)
        self.w = wb_width * np.random.randn( n, m )  # 重み    （2x7行列    ）W39
        self.b = wb_width * np.random.randn( m )     # バイアス（1x7ベクトル）B39

    def forward(self, x): # シグモイド関数  (1x6行列    ）U39, X39
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y = 1/(1+np.exp(-u))  

    def backward(self, grad_y):
        delta = grad_y * (1-self.y)*self.y
        
        self.grad_w = np.dot(self.x.T, delta)
        self.grad_b = np.sum(delta, axis=0)
        
        self.grad_x = np.dot(delta, self.w.T) 
        
    def update(self, eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b

# +++++++++++++++++++ 出力層 +++++++++++++++++++
class OutputLayer:
    def __init__(self, n, m):         # 初期設定(n=Out_Neuron, m=MidOutSignal)
        self.w = wb_width * np.random.randn( n, m )  # 重み     （7x3行列    ）Wxxii
        self.b = wb_width * np.random.randn(m)       # バイアス （1x3ベクトル）Bxxii
    
    def forward(self, x): # ソフトマックス関数（1x2行列    ）Uxxii, abc
        self.x = x
        u = np.dot(x, self.w) + self.b
        #self.y = np.exp(u)/np.sum(np.exp(u), axis=1, keepdims=True)  
        self.y = u
    
    def backward(self, ym):
        delta = self.y - ym
        
        self.grad_w = np.dot(self.x.T, delta)
        self.grad_b = np.sum(delta, axis=0)
        
        self.grad_x = np.dot(delta, self.w.T) 

    def update(self, eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b

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
       
    for jdx in index_random:#●●●●●●●●●●●●

        x = input_data[  jdx]  # 入力
        t0 = correct_data[jdx]  # 正解出力
        yM = np.array([0,0,0])
        yM[t0-1] = 1

        # 順伝播
        middle_layer.forward(x.reshape(1,2))
        output_layer.forward(middle_layer.y)

        # 逆伝播
        output_layer.backward(yM.reshape(1,3))
        middle_layer.backward(output_layer.grad_x)
        
        # 重みとバイアスの更新
        middle_layer.update(eta)
        output_layer.update(eta)
        
        if k%interval == 0:
            
            y = output_layer.y.reshape(-1)  # 行列をベクトルに戻す
            
            # 誤差の計算
            total_error += (y[0]-yM[0])*(y[0]-yM[0])+(y[1]-yM[1])*(y[1]-yM[1])+(y[2]-yM[2])*(y[2]-yM[2])# 
            
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
