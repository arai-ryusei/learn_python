#  例題ファイル：C:\pythonPG\sample3045.py

class CapsuleClass:
	def __init__( self ):
		print("+++ アクセスコンストラクタに：__ini__() +++")
		self._AAA = "AAA"
		self.__BBB = "BBB"
	
	def __funcA( self ):
		print("=== アクセス：__funcA() ===")

print()
myclass = CapsuleClass()       # オブジェクトの生成
print( "アクセス変数に:_AAA  ==>", myclass._AAA )
print( "アクセス変数に:_ _BBB==>", myclass._CapsuleClass__BBB )
myclass._CapsuleClass__funcA() # メソッドにアクセス

print()
myclass.__init__( )           # コンストラクタにアクセス

