#  例題ファイル：C:\pythonPG\sample3440.py

print()
print( "====== 例外処理_1 ========" )
try:
	a = 10 / 0
except ZeroDivisionError as e:
	print( "例外発生時の処理：", e)
else:
	print("例外ない場合の処理")
finally:
	print("最後の処理")

print()
print( "====== 例外処理_2 ========" )
try:
	a = 10 / 0
except:
	print( "例外発生時の処理：")
else:
	pass

