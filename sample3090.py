#  例題ファイル：C:\pythonPG\sample3090.py

#import Data.super11aa as Dsuper
import Data.super11aa

print( "====== サブクラス ========" )
#class SubClass( Dsuper.SuperAA, Dsuper.Super11 ):
class SubClass( Data.super11aa.SuperAA, Data.super11aa.Super11 ):
	pass 

object = SubClass() 
object.func11() 
object.funcAA()

