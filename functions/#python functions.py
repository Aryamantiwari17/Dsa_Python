#python functions
#LAMBDA FUNCTIONS
#lambda functions are small anonymous functions


additional = lambda a,b:a+b

print(additional(5,6))

def even(num):
    if num%2==0:
        print("true")
    else:
        return False
    
even(24)


even1=lambda num:num%2
print(even1(24))


def additional(x,y,z):
    return x+y+z
print(additional(12,13,14))


even2=lambda x,y,z:x+y+z
print(even2(12,13,14))