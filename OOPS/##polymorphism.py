##polymorphism
class Animal:#base class1
    def speak(self):
        return "Sounds of the animal"
    

class Dog(Animal):#base class2
    
    def speak(self):
        return "Woof!"
    

class Cat(Animal):
    
    def speak(self):
        return "Meow!"
    
    ##function that demonstrate polymorphism

def animal_speak(animal):
        print(animal.speak())##overdiing function
    
    


dog=Dog()
cat=Cat()
print(dog.speak())## method overidding kari hai
print(cat.speak())
animal_speak(dog)##yeh new object override ka rha haii

