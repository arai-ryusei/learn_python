#  例題ファイル：C:\pythonPG\sample2-2-010.py

def func_A( v, *w ):
	func_B()
	w1 = list( w[0] )
	list_x = []
	for element in w1:
		x1 = v*element
		list_x.append( x1 )
	return list_x

def func_B():
	print( "関数func_A()内から関数func_B()が呼ばれた" )

print()
a = 3
list_b = [11,22,33]
ret = func_A( a, list_b )
print( "戻り値=", ret )

