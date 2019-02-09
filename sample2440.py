#  例題ファイル：C:\pythonPG\sample2440.py

print()
print( "==========宣言・参照・変更・クリア==================" )
print("宣言と参照")
dict00 = { "key1":"A", "key2":20, "key3":"C" }
print( dict00 )
print( "1番目の値==>", dict00["key1"] )
print( "2番目の値==>", dict00["key2"] )
dict00["key1"] = "A00"
print( "1番目の値変更==>", dict00 )
dict00.clear()
print( "クリア==>", dict00 )

