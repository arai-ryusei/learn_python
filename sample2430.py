#  例題ファイル：C:\pythonPG\sample2430.py
print()
aaa = ("A","B","C","D", "E", "D")
print( "タプル=", aaa )
print( "長さ=", len(aaa) )
print( "2,3,4番目のサブタプル=", aaa[2:5] )

print()
tuple00 = tuple("ABC")
print( "(ABC=>Tuple)=",tuple00 )
tuple00 = tuple(["A", "B", ["C","D"]])
print( "(List==>Tuple)=", tuple00 )

