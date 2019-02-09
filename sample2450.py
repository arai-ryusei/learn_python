#  例題ファイル：C:\pythonPG\sample2450.py

print( "==========集合==================" )
print( "宣言：set00 = { 0, 10, 20, 30, 40, 50 }" )
print()
set00 = { 0, 10, 20, 30, 40, 50 }
print( "表示(順番がランダムになっている)" )
print( set00 );  print()

set00.add(11)
print("値11を追加", set00);  print()

set00.add(33)
print("値33を追加", set00);  print()

set00.remove(33)
print("値33を削除", set00);  print()

for value in set00:
	print( value, end=",  " )

print();  print()
print( "値10が含まれるか?", 10 in set00 );  print()

print( "値[10,50]が含まれるか?", (set00.issuperset([10, 50]))  );  print()

set00.clear()
print("クリア", set00);  print()

