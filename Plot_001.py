import numpy as np
import matplotlib.pyplot as plt # pltとしてインポートされるのが慣例です。


X = np.linspace(-10, 10, 1000)

y = np.sin(X) # サインの値を計算する

plt.plot(X, y) # これでプロットをする。plotで点と点同士をなめらかにつなぐ

# [<matplotlib.lines.Line2D at 0x1093f7550>]

plt.show() # グラフの表示




