###Magic methods

###basic methods
class Person:
   def __init__(self,name,age):
        self.name=name
        self.age=age

    
   def __str__(self):##overriden
    
     return f"my name is {self.name},{self.age} years of age"
   

   def __repr__(self):
      return f"Person {self.name}"


    


person=Person("at",21)
print(person)
print(repr(person))
