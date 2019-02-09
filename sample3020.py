#  例題ファイル：C:\pythonPG\sample3020.py

print( "==========クラス変数==================" )

class MyClass:
	access_count = 0

	def __init__(self):
		MyClass.access_count += 1
		print(MyClass.access_count)  # クラス変数へのアクセス


a1 = MyClass()
a2 = MyClass()
a3 = MyClass()
print()
print( MyClass.access_count)  # クラス変数へのアクセス
print( a1.access_count)       # オブジェクトからクラス変数へのアクセス

