#  func_deco.py


def deco_func(func00):
     
    def new_func():
        print('付加機能１')
        ret_str = func00()
        print(ret_str)
        print('付加機能２')
    return new_func
 
def base_func():
	return "基礎の機能"

func11 = base_func            # 関数オブジェクト
new_func2 = deco_func(func11) # 新たに機能を追加した関数オブジェクトを作成
new_func2()                   # 新たに作成した関数の実行


