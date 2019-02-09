#  例題ファイル：C:\pythonPG\sample2480.py

print( "==========ジェネレータ==================" )
def lions():
	yield '秋山選手'
	yield '源田選手'
	yield '浅村選手'
	yield '山川選手'
obj = lions() # ジェネレータオのブジェクトの生成
for person in obj:
	print(person)

print("=================================")
