class Car:
    def __init__(self,windows,doors,enginetype):##single inheritance
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    
    def drive(self):
        print(f"The person will drive the {self.enginetype} car")
       # print(f"The person will drive having  {self.windows} windows")
       # print(f"The person will drive having {self.doors} doors")


car1=Car(4,4,"Petrol")
car1.drive()
car2=Car(5,5,"Diesel")
car2.drive()

##tesla is inherit class of Car
class Tesla(Car):
    def __init__(self,windows,doors,enginetype,is_selfdrive):
        super().__init__(windows,doors,enginetype) ##trying to call the parent class
        self.is_selfdrive=is_selfdrive
    
    def self_drive(self):
        if self.enginetype=="Electric" and self.is_selfdrive==True:
            print("Car is self drive")
        else:
            print("none of the car is self drive ")

car8=Tesla(4,4,"Electric",True)
car8.self_drive()
car8.drive()#this function from parent class


