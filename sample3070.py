#  例題ファイル：C:\pythonPG\sample3070.py

print( "========== スーパークラス ===============" )
class CarClass:
	def __init__(self, num="1234"):
		print("スーパークラスのコンストラクタ", num)
		self.number = num
	def setnumber(self, num):
		self.number = num
	def getnumber(self):
		return self.number

print( "====== クラスの継承とオーバーライド========" )
class CompanyCar(CarClass):
	def __init__(self, num):
		super(CompanyCar,self).__init__( num )
		print( "サブクラスのコンストラクタ",self.number)

toyota = CompanyCar("5555")
toyota.getnumber()

