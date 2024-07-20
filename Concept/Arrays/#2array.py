# aaray methods
import array
from array import *

A1=array('i',[65,64,76])
print(A1)

A1.append(45)#add koi element aaray mein
print(A1)

y=A1.count(64)#count hai kitni baar element hai array mein
print(y)

z=A1.index(45)#kisi index par hai yeh element
print(z)

A1.pop()#POPING ELEMENT FROM LAST TO FIRST
A1.pop()
print(A1)
 
A1.pop(0)#eliminting element through indexing
print(A1)
 
A1=array('i',[65,64,76])
print(A1)

A1.remove(64)#remove element just by calling it
print(A1)