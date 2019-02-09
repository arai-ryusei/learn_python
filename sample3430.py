#  例題ファイル：C:\pythonPG\sample3430.py

print( "====== ファイル操作_3 ========" )

import os
import os.path
if os.path.exists(r'Data\text2.txt'):
	print ("存在")
else:
	print ("非存在")

os.remove(r'Data\text2.txt')

if os.path.exists(r'Data\text2.txt'):
	print ("存在")
else:
	print ("非存在")

print( "=========================" )
