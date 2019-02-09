#  例題ファイル：C:\pythonPG\sample2414.py

list_vari=[[1,2],[3,4],[5,6]]
print( "初期3x2リスト" )
print( list_vari )
print( "リスト[1][0]   =", list_vari[1][0] )
list_vari= [ [[1,2],[3,4],[5,6]],[[10,20],[30,40],[50,60]] ]
print( "初期2x3x2リスト" )
print( list_vari )
print( "リスト[1][1][0]=", list_vari[1][1][0] )

print()
list_vari0 = [ 1000, 2000, 3000 ]
print( "初期　リスト   =", list_vari0 )
list_vari1 = list_vari0
list_vari1[1] -= 500
print( "500引いたリスト=", list_vari1 )
print( "初期　リスト   =", list_vari0 )

print()
list_vari0 = [ 1000, 2000, 3000 ]
print( "初期　リスト   =", list_vari0 )
list_vari1 = list( list_vari0 )
list_vari1[1] -= 500
print( "500引いたリスト=", list_vari1 )
print( "初期　リスト   =", list_vari0 )

