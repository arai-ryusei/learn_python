# func_ate.py

# 関数area(tate, yoko)
#　　　引　数：縦、横の長さ
#　　　戻り値：4角形の面積

def area(tate:'縦長', yoko:'横長')->'面積':
	"長方形の面積を計算する。"
	return tate*yoko

print()
print( area.__doc__)
print()
print("面積=", area(4,5) )


