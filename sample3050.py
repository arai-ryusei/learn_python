#  例題ファイル：C:\pythonPG\sample3050.py

print( "========== スーパークラス ===============" )
class CarClass:
	def __init__(self, num="1234"):
		self.__number = num
	def setnumber(self, num):
		self.__number = num
	def getnumber(self):
		return self.__number

print( "========== クラスの継承 ===============" )
class CompanyCar(CarClass):
	def setcompany( self, company ):
		self.company = company
	def getcompany(self):
		print(self.company)

toyota = CompanyCar("2222")
print(toyota.getnumber())
toyota.setcompany("TOYOTA")

