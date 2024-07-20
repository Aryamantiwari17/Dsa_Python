#
list=['January' ,'Feburary=' ,'March', 'April', 'May']
#print(list)

exp=[2200,2350,2600,2130,2190]
print(exp)

num=exp[1]-exp[0]
print(num)

num1=exp[0]+exp[1]+exp[2]
print(num1)

for i in range (len(exp)):
    if i==2000:
     print("yes")
     break
    else:
     print("no") 
     break

exp.append(1980)
print(exp)

exp[3]=exp[3]-200
print(exp)

exp.insert(0,1234)
print(exp)


