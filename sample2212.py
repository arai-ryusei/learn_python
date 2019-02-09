#  例題ファイル：C:\pythonPG\sample2212.py

math = 82
english=70
flg1 = (math >= 80 and english >= 70)
flg2 = (math >= 70 and english >= 80)

if math >= 80 and english >= 80:
	print( "総合評価：A" )
elif flg1 or flg2:
	print( "総合評価：B" )
else:
	print( "総合評価：C" )

