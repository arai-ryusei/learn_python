#  func_deco2.py

def deco_func(func00):
     
    def new_func():
        print('付加機能１')
        ret_str = func00()
        print(ret_str)
        print('付加機能２')
    return new_func

@deco_func
def base_func():
	return "基礎の機能"

base_func()


