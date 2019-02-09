#  例題ファイル：C:\pythonPG\sample2467.py

print( "==========内部関数==================" )
print()
def outer_function():
	def inner_function():
		print("内部関数での表示")
	inner_function()

outer_function()

print()
print("内部関数のobject用いる")
def outer_function():
	def inner_function():
		print("内部関数での表示")
	inner_obj=inner_function
	return inner_obj
inner_function_obj = outer_function()
inner_function_obj()

print( "==========nonlocal宣言==================" )
print()
def outer_function():
	vari = 200
	print( vari )
	def inner_function():
		nonlocal vari
		print( vari+22) # 外部関数の変数に内部関数で２２を加算
	inner_function()
outer_function()

