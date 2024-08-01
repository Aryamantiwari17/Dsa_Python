#2 functions
def square(x):
    return x*x



numbers=[1,2,3,4,5,6,7,8]
map(square,numbers)
x=list(map(square,numbers))
print(x)

####lambda function
x=list(map(lambda x:x*x,numbers))
print(x)


num2=[1,2,3]
num3=[4,5,6]

added_numbers=list(map(lambda x,y:x+y,num2,num3))
print(added_numbers)