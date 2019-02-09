#  例題ファイル：C:\pythonPG\sample2470.py

y1 = 1000
y3 = 3000
def func_A( ):
	print( "Global 参照のみ==", y3 + 333 )
	global y1
	y1 = y1 + 111
	global y2
	y2 = 2000
	y2 = y2 + 222

func_A()
print ( "Global 変数==", y1 )
print ( "Global 変数==", y2 )

