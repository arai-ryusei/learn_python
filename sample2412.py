#  例題ファイル：C:\pythonPG\sample2412.py

list_vari = [ 10, "abc", 40 ]
print( "初期リスト=", list_vari )
print()

list_vari[1] = 20 # 変更
print( "2番目変更=",list_vari )
print()
list_vari.insert(2, 30)
print( "3番目に1個挿入=",list_vari )
print()
list_vari.append([51,52,53])
print( "最後に1個追加=",list_vari )
print()
list_vari.extend([60,70,80])
print( "最後に3個追加=",list_vari )
print()

#del list_vari[4:6]
list_vari[4:6] = []
print( "5番目、6番目を削除=", list_vari )






