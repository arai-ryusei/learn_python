# https://udemy.benesse.co.jp/ai/python-numpy.html
# cd C:\PythonPG
# python C:\PythonPG\Numpy_009.py
#

import numpy as np #モジュールであるNumPyをnpという名前でインポート

print( )
A = np.array( [ 1,2,3,4,5 ] )
print("　行列A[1,2,3,4,5]\n　平均値==", np.average(A))
print("　標準偏差==", np.std(A))
print("　分散==", np.var(A))

print( )
print("　(0,1)正規分布==", np.random.rand())

