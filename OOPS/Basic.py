class Car:
    pass

audi=Car()
bmw=Car()

print(type(audi))#tell which class it belongs
print(audi)#telling it is  the object 

##instance varaiable and methods

audi.windows=4
print(audi.windows)#windows is taking as an attribute


tata=Car()
tata.doors=4
#print(tata.windows)


dir()
##instance variable and methods
class Dog:
    ## creating a constructor
    def __init__(self,name,age): ### self is use for instance varialble
        self.name=name
        self.age=age

    ## create object
dog1=Dog("Buddy",3)
dog2=Dog("Lucy",4)
print(dog1)
print(dog1.name)
print(dog1.age)
print(dog2)
print(dog2.name)

##define a class with instance methods

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def bark(self):
        print(f"{self.name} says woof")

dog1=Dog("Buddy",3)
dog1.bark()
dog2=Dog("Lucy",4)
dog2.bark()






       
