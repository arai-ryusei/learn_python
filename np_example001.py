#  例題:  np_example001.py

import numpy as np
import matplotlib.pyplot as plt

print(" ベクトル生成");                        print( np.arange( 0, 5)   )
print(" 刻み幅指定してベクトル生成");          print( np.arange( 0, 1, 0.1)   )
print(" 個数指定してベクトル生成");            print( np.linspace( 0,  1,  11)  )

list0 = np.arange(1,13)
print(" ベクトル");             print( list0 )
print(" 配列大きさ");           print(np.shape(list0))
print(" 3x4配列生成");          list1 = list0.reshape(3,4)
print(  list1 );     
print(" 配列大きさ");          print(  np.shape( list1 ) )
print(" 配列Size");            print(   np.size(list1)  )
print(" 配列長さ");            print(   len(list1)  )

