#  例題ファイル：C:\pythonPG\sample2443.py

dict00 = { "key1":"A"}
print( "初期　タプル=", dict00 ); print()

dict00.update( {"key2":"B", "key3":"C" })
print( "1番目以降に2個追加=",dict00 ); print()
dict00["key4"] = "B"
print( "4番目に1個追加=", dict00 )

print()
del dict00["key1"]
print( "1番目(key1)削除", dict00 ); print()
print("すべて削除かつ削除するKeyと値をタプルで出力")
while dict00:
	tuple00 = dict00.popitem() 
	print("    ",tuple00)

print( "最終の配列=", dict00 )

