#  例題ファイル：C:\pythonPG\sample2446.py

dict00 = { "key1":"A", "key2":20, "key3":"C" }
print( dict00 ); print( )

key00 = list(dict00.keys())
print( "key一覧=", key00 ); print( )

value00 = list(dict00.values())
print( "value一覧=", value00 ); print( )

items00 = list( dict00.items() )
print( "(key,value)一覧Tuple=",items00 ); print( )

bbb = "key1" in dict00
print( "key1有無=", bbb  ); print( )

print( "======キー・値をfor文で取得==========" )
dict00 = { "key1":"A", "key2":20, "key3":"C" }
print( dict00 ); print( )

for key in dict00.keys():
	print(key, end="   ")
print( ); print( )

for value in dict00.values():
	print(value, end="     ")
print( ); print( )

for key, value in dict00.items():
	print( key, value, end="     " )
print( ); print( )
