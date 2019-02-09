#  例題ファイル：C:\pythonPG\sample3060.py

print( "========== スーパークラス ===============" )
class CarClass:
	def __init__(self, num="1234"):
		self.number = num
	def setnumber(self, num):
		self.number = num
	def getnumber(self):
		print( "At superメソッド",self.number )

print( "====== クラスの継承とオーバーライド========" )
class CompanyCar(CarClass):
	def getnumber(self):
		super().getnumber()
		print( "At オーバーライドメソッド",self.number)

toyota = CompanyCar("2222")
toyota.getnumber()

