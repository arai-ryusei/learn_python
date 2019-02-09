#  例題ファイル：C:\pythonPG\sample2413.py

list_vari = [ 10, 20, 30, 40 ]
print( "初期　リスト  =", list_vari )
print( "リスト=>タプル=", tuple(list_vari))

print()
list_vari.sort(reverse=True)
print( "昇順にソート=", list_vari )
print( "値20の番地=",list_vari.index(20) )
print( "値20の個数=",list_vari.count(20) )
print( "クリア    =",list_vari.clear() )

print()
list_vari = ["10","20","30"]
print( "初期　リスト  =", list_vari )
str00 = "_".join( list_vari )
print( "文字列化  =", str00 )
str11 = str00.replace("0","A")
print( "置換0=>A  =", str11 )




