## Encapsulation 

##public,private and protected
class Person:
    def __init__(self,name,age):
        self.name=name #in public variables
        self.age=age


def get_name(person):
    return person.name
    
person =Person("At",21)
print(person.name)




 
 
class Person:
    def __init__(self,name,age,gender):
        self.__name=name #in private variables
        self.__age=age#IN PRIVATE VARIABLE
        self.gender=gender


def get_name(person):
        return person.__name



person =Person("At",21,"male")

#print(person.name)
print(person.get_name())




 ###protected class

class Person:
    def __init__(self,name,age,gender):
        self._name=name #in protected variable
        self._age=age#IN PRotected VARIABLE
        self.gender=gender


class Employee(Person) :
     def __init__(self,name,age,gender):
         return super().__init__(name,age,gender)


employee=Employee("ATY",34,"Male")
print(employee._name)#by classes derived from that class

          
     
     





