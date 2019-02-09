#  例題ファイル：C:\pythonPG\sample3403.py

print( "====== カレントディレクトリ ========" )
from os import path 
thispath = path.abspath('sample3403.py')
print("カレントディレクトリ取得==", thispath)

paths = path.split( thispath ) 
print("カレントディレクトリ分割==", paths)

