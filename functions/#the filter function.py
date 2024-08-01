#the filter function

def even(num):
    if num%2==0:
        print(num)


    
ones=[1,2,3,4,5,5,6,7,8,9,10]

list(filter(even,ones))

greter_than__5= list(filter(lambda x:x>5,ones))
print(greter_than__5)



#filter with A LAMBDA FIUNCTION AND MUTIPLE CONDITION
greter_than= list(filter(lambda x:x>5 and x%2==0,ones))
print(greter_than)

