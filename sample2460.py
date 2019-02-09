#  例題ファイル：C:\pythonPG\sample2460.py

print(); print( "関数１" )
def aaa():
	print("　　　関数内：引数なし・戻り値なし")
aaa()

print(); print( "関数２" )
def bbb():
	print("　　　関数内：引数なし・戻り値あり")
	return ["ret1", "ret2"] # 戻り値：リスト
ret = bbb()
print( "戻り値=", ret )

print(); print( "関数３１" )
def ccc( x, y ):
	print("　　　引数値 =", str(x) +",  " +y )
ccc( 10, "str_10")

print(); print( "関数４" )
def ggg( x ):
	print("　　　引数値(半径) =", x )
	return x*x*3.141592
ret = ggg(10 )
print( "戻り値(円の面積)=", ret )

