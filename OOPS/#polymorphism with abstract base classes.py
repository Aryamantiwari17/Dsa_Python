#polymorphism with abstract base classes

from abc import ABC,abstractmethod

## define an abstract class

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass




###derived class
class Car(Vehicle):

    def start_engine(self):
        return "Car engine started"


    


##derived class 2

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    
    #create objects of car and Motocycle
def start_vehicle(vehicle):
    print(vehicle.start_engine())



car=Car()
motorcycle=Motorcycle()
start_vehicle(car)
start_vehicle(motorcycle)
    


