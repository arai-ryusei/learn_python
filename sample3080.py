#  例題ファイル：C:\pythonPG\sample3080.py

print( "===== 2個のスーパークラス ==========" )
class Super11:
	def __init__(self):
		print("11111")
	def func11(self):
		print ( "Super11:func11" )

class SuperAA:
	def __init__(self):
		print("AAAAAA")
	def funcAA(self):
		print ( "SuperAA:funcAA" ) 


print( "====== サブクラス ========" )
class SubClass( SuperAA, Super11 ):
	pass 


object = SubClass() 
object.func11() 
object.funcAA()

