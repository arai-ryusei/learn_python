#  例題ファイル：C:\pythonPG\sample3320.py

print( "====== 文字クラス_2 ========" )

str00 = "abc123abc123abc"
print("対象文字列==", str00)
print( "'b'index==", str00.index("b", 2) )
print( "'b'count==", str00.count("b") )
list00 = str00.split("123")
print( "split(123)==", list00 )

print()
list11 = ["111","222","333"]
print("対象文字列==", list11 )
str11 = "_A_".join( list11 )
print( "join(_A_) ==", str11 )

print()
# 文字列の置換
str00 = "abc123abc123abc"
print("対象文字列==", str00 )
str11 = str00.replace("a","-")
print("replace(a,-)       ==",str11)

import re
str00 = "abc123abc123abc"
str11 = re.sub('[a-z]+',"BB",str00,2)
print("re.sub((a-z)+==>BB)==",str11)

