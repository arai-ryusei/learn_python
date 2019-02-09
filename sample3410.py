#  例題ファイル：C:\pythonPG\sample3410.py

print( "====== ファイル操作 ========" )

print("=====================================")
print("++++++　すべて　++++++")
fp = open('Data\\text.txt', "r", encoding='utf-8')
str0 = fp.read()
fp.close()
print(str0)

print("=====================================")
print("++++++　行毎に全行　++++++")

fp = open('Data\\text.txt', "r", encoding='utf-8')
str1 = fp.readlines()
fp.close()
for row in str1:
	print( row.replace( "\n", "") )

print("=====================================")
print("++++++　１行ずつ　++++++")

fp = open('Data\\text.txt', "r", encoding='utf-8')
for row in fp:
	print( row.replace( "\n", "") )
fp.close()




