#  例題ファイル：C:\pythonPG\sample3450.py

import datetime

print( "====== 日付・時刻 ========" )

dt = datetime.datetime.now()
print( dt )
print( dt.strftime("%Y-%m-%d") )

str0 = "2018-01-18"
dt = datetime.datetime.strptime(str0, "%Y-%m-%d")
print(dt+datetime.timedelta(days=1, minutes=5))

