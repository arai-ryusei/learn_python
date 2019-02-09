#  例題ファイル：C:\pythonPG\sample3030.py

class ClassMethods:
	vari = 0   # クラス変数

	def __init__(self):
		self.vari = 0
		ClassMethods.vari = ClassMethods.vari + 1

	@classmethod
	def class_method( cls ):
		"""(クラス)メソッド呼び出し"""
		print("クラス変数vari=", cls.vari)

object = ClassMethods()
print( "クラスメソッドへの２通りアクセス" )
object.class_method( )
ClassMethods.class_method( )

