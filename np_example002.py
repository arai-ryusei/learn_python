#  例題:  np_example002.py

import numpy as np
import matplotlib.pyplot as plt

print(" 2x2配列A(要素=1)==");  A  = np.ones( (2,2) );  print(A)
print(" 任意のベクトルa==");  a  = np.array([ 10, 20 ]);  print(a)
print(" 任意の2x2配列B==");  B  = np.arange( 1, 5).reshape(2,2);  print(B)

print(" スカラー倍A*2==");  C2 = A*2;  print(C2)


print(" 配列の和 A+B==");  print( A + B )

print(" ベクトル・配列の積 aA==");  print( np.dot( a, A ) )

print(" 配列の積 AB==");  print( np.dot( A, B ) )
