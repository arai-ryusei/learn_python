#  例題ファイル：C:\pythonPG\sample3445.py

print( "====== 例外処理::raise ========" )

class MyException(Exception):
	pass

print()
nn = 0.001
mm = 0.0
try:
	if -0.002<nn and nn < 0.002:
		raise MyException("nn="+str(nn),'例外の近似0割り')
	mm= 1.0/nn
except MyException as mye:
	print( mye )
	#print(mye.args)
	#print(mye.args[0])
	#print(mye.args[1])
else:
	print("mm==", mm)
finally:
	print()
	print("at finally")

