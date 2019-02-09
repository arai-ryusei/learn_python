#  例題:  np_example003.py

import numpy as np
import matplotlib.pyplot as plt

print(" スカラー＋ベクトル  a==");  a = 10 + np.array([ 1, 2, 3 ]);  print(a)
print(" スカラー / ベクトル b==");  b = 8 / np.array([ 2, 4, 8 ]);  print(b)
print(" ベクトル + 配列     A==");  A = np.array([1,2]) + np.array([[1,1],[2,2]]);  print(A)
print(" 配列 〇 配列     B==");     B = np.array( [[2,2],[3,3]] ) * np.array( [[1,2],[3,4]] );  
print(B)



