#o(n2)
num=[9,4,3,2,3,3]
for i in range (len(num)):
    for  j in range (i+1,len(num)):
     if num[i]==num[j]:
        print(str(num[i]) + " is duplicate")
        break
     
#2 for loops so it becomes n2 
