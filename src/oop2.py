# To the GroundVehicle class, add method drive() that prints "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.
v = vehicles
class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels
num_wheels = 4
    # TODO


# Subclass Motorcycle from Vehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it prints "BRAAAP!!"
class Motorcycle(Vehicle):
    def __init__(self):
    super()__init__("num_wheels")

    def call(self):
        print("BRAAAP!!")
    
    def num_wheels(self)
        print(2)

# TODO
v = vehicles()
v.drive()
v.sound() #generic sound

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and call drive() on each.

# TODO
for v in vehicles:
    v.drive()