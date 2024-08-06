
###encapsulation with geeter and setter

class Person:
    def __init__(self,name,age):
        self.__name=name##private access modifier or variable
        self.__age=age#private access 



    
    ##GETTER METHOD FOR NAME


    def get_name(self):
        return self.__name
    
 
    ##setter

    def set_name(self,name):
        self.__name=name

    
    def get_age(self):
       return self.__age
    
    
    def set_age(self,age):
          if age>0:
              self.__age=age

          else:
              print("less go ")

person=Person("ATY",34)

##access and modify private vairiable
print(person.get_name())
print(person.get_age())

x=person.set_age(35)
print(person.get_age())














