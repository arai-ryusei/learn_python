#  例題ファイル：C:\pythonPG\sample3010.py

print( "==========クラス定義==================" )
class MyCarClass:
	def __init__(self):# コンストラクタ
		self.carname = "" # インスタンス変数 フィールド変数）

	def __str__(self):    #文字列化
		return "車クラス"

	def __del__(self):  #デストラクタ
		print("車クラスの終了")

	def getCarName(self):         # getCarName()メソッド
		return self.carname

	def setCarName(self, carname): # setCarName()メソッド
		self.carname = carname

print( "==========オブジェクト生成============" )
car = MyCarClass() # インスタンスを生成
print(car) # オブジェクトの文字列化表示

car.setCarName("TOYOTAクラウン") # メソッドの呼び出し

print ("メソッドアクセス==", car.getCarName()) # メソッドの呼び出し

print("オブジェクトアクセス==", car.carname)   # オブジェクト.インスタンス変数の参照

