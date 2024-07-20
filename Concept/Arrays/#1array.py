import array
from array import *#import all modules

a1=array('i',[98,54,67])
type(a1)
print(a1)#pritn the array

for x in a1:#acces to every element and print it
    print(x)

#now accessing array through indexing

for i in range(3):#0,1,2
        print(a1[i],end=' ')

#accesing elemnts through while loop
        