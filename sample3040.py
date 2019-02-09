#  例題ファイル：C:\pythonPG\sample3040.py

# １個のクラス変数のみを持つクラス。
class MyVariClass:
	Vari = 9.8

myclass = MyVariClass() # オブジェクトの生成

MyVariClass.AddClass = 100 # 新しいクラス変数の追加
print("追加されたクラス変数=", MyVariClass.AddClass)

myclass.addinstance = 200  # 新しいインスタンス変数の追加
print("追加されたインスタンス変数=", myclass.addinstance)

