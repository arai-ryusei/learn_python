#  例題ファイル：C:\pythonPG\sample2462.py

print( "===def 関数名(引数1, 引数2, ・・・,*引数シーケンス,**引数辞書)===" )

def func00( vari1, vari2, *list_vari, **dic_vari):
	print(vari1)
	print(vari2)
	print(list_vari)
	print(dic_vari)
func00(10, 'aa' , 30, 'bb', 'cc', dic0=60, dic1='dd' )    # 呼び出し

print("====================")
