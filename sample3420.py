#  例題ファイル：C:\pythonPG\sample3420.py

print( "====== ファイル操作_2 ========" )

fp = open('Data\\text.txt', "a", encoding='utf-8')
fp.writelines("\nあいうえお")
fp.writelines("\nかきくけこ")
fp.close()


print( "=========================" )
