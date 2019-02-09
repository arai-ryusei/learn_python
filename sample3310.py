#  例題ファイル：C:\pythonPG\sample3310.py

print( "====== 文字クラス ========" )

# 数値--->文字列
print( str(12.3)+" 数値" )

# 文字列--->数値
print( "(F)16       ==> int ", int("F",16) )
print( "(11111111)2 ==> int ", int("11111111", 2) )
print( "3.141592    ==>float", float("3.141592") )

# 文字列から文字列抽出
str0 = "12345ABCD9"
print(str0)
print( "1番目の文字      =", str0[0]  )
print( "(6-9)番目の文字列=", str0[5:9]  )

