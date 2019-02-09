#  例題:  np_example004.py

import numpy as np
import matplotlib.pyplot as plt

print(" 配列 A     ==");  A = np.array( [[1,2],[3,4]] );  print(A)
print(" Axis=0 の和==");  print( np.sum( A, axis=0 ).shape )  
print(" Axis=1 の和==");  print( np.sum( A, axis=1 ).shape )  
print(" Aの転置    ==");  print( A.T )



