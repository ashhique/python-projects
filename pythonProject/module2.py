#module example
import module1
module1.negPos(10)

print("-------------------------------")
#check module name
print(__name__)
print(module1.__name__)
print("-------------------------------")

#assign function
convert=module1.negPos
convert(30)
convert(-30)
print("-------------------------------")
#import only function
from module1 import negPos
negPos(20)
print("-------------------------------")

#change name
from module1 import negPos as covert
covert(55)
covert(-365)
print("-------------------------------")
#in-build modules

import platform

print(platform.system())
print(platform.machine())
print(platform.node())
print(platform.processor())
print("-------------------------------")
#exception

num=0 #if it is zero
try:
    sum=10/num
    print(sum)
    print("try completed") #only work if  num!=0
except ZeroDivisionError:
    print("Can't divide by Zero") #only works if num=0

print("program completed")

