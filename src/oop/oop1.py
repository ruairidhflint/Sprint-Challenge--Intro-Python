# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#

# Base Class
class Vehicle():
    def __init__(self):
        pass


# Ground Vehicle Class
class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass


# Flight Vehicle Class
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass