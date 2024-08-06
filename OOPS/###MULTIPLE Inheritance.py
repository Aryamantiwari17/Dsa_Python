###MULTIPLE Inheritance

class Animal:#base class 1
    def __init__(self,name):
        self.name=name


    def speak(self):
        print("Subclasses must implemnt this method")


class Pet:#base class2
    def __init__(self,owner):
        self.owner=owner


class Dog(Animal,Pet):##derived class
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    
    def speak(self):
        return   f"{self.name}  says woof and the owner is {self.owner}"
    

    



##create an object

dog=Dog("buddy","AT")
x=dog.speak()
print(x)





    



