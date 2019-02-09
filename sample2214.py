#  例題ファイル：C:\pythonPG\sample2214.py

sum = 0
flg = True
no  = 0

while flg:
	sum += no
	no  += 1
	if no > 100:
		flg = False
print( "sum=", sum )

