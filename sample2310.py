#  例題ファイル：C:\pythonPG\sample2310.py

print()
print ( "例題１:[  'みかん', 'なし', 'りんご']" )
for element in [ "みかん", "なし", "りんご"]:
	print ( element + ",  ", end="" )
print()
print()

print ( "例題２:[ 'みかん', 'なし', 'りんご'] "+"+ else文" )
for element in [ "みかん", "なし", "りんご"]:
	print ( element + ",  ", end="" )
else:
	print ("繰り返し最後", end="" )
print()
print()

print ( "例題３:\"ELEMENT\"" )
for element in "ELEMENT":
	print ( element + ",  ", end="" )
print()
print()

print ( "例題４:range(0, 5)" )
for element in range(0, 5):
	print ( str(element) + ",  ", end="" )
print()

