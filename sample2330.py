#  例題ファイル：C:\pythonPG\sample2330.py

print()
j = 0
while j<5:
	if j==3:
		break
	print ( str(j) + ",  ", end="" )
	j = j+1
else:
	print("write In else")

print("After ForEnd with break at j==3")


print()
j = 0
while j<5:
	if j==3:
		j = j+1
		continue
	print ( str(j) + ",  ", end="" )
	j = j+1
else:
	print("In else")

print("After ForEnd with continue at j==3")

