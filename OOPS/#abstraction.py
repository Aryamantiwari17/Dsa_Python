#abstraction
from abc import ABC,abstractmethod
#abstract base class
class Vehicle(ABC):
    def drive(self):
        print("vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass


"""
Driving a car
You can drive a car without knowing how the engine works or
 what its internal components are. 
 You only need to know that pressing the accelerator increases speed and
applying the brakes stops the car.
"""

class Car(Vehicle):
    def start_engine(self):
        print("car engine is started")

    
def operate(vehicle):
        vehicle.start_engine()
        vehicle.drive()


car=Car()
operate(car)







 