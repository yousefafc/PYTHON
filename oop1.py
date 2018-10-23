#!/usr/bin/python
class garage:
    vehicle = []
    def add_vehicle(self, vehicle):
        self.vehicle.append(vehicle)
        pass


class vehicle(garage):
            def __init__(self, type):
                self.type = type
                pass
def __str__(self):
    return(self.name)
class car(vehicle):
    def __init__(self,make,model,colour,doors):
        self.make = make
        self.model = model
        self.colour = colour.lower()
        self.doors = doors
        def carprint(self):
            return self.make + self.model + self.colour + self.colour + self.door
        pass
    pass

class motorbike(vehicle):
    def __init__(self,make,model,colour,cc):
        self.make = make
        self.model = model
        self.colour = colour.lower()
        self.cc = cc
        pass
    pass



x = car("ford", "fiesta", "silver", 5)
y = motorbike("yamaha","yzf","black",125)
print(x.colour)
garage1 = garage.add_vehicle(x)
print(garage1)


