# 1) Create a file engine_factory.py Realize a class that describes
# an engine object.
# During instance creation we should set model_name, number_of_cylinders,
# engine_displacement,
# engine_resource (will count in kilometers), fuel_type. realize a method
# that represent engine information. A
# dd description at docstring. Create a class that extends engine class.
# This class has additional instance attributes as current_engine_mileage,
# unique_number.
# For each instance you should generate unique_number (think about how it do).
# Create a method takes number of kilometers and increase
# current_engine_mileage.
# Also we need a property that shows the difference between
# current_engine_mileage and engine_resource.
# Create 2-3 instances and play with methods.

import random
import string


class Engine:

    """Class represent engine"""


    def __init__(self, model_name, number_of_cylinders,
                 engine_displacement, engine_resource, fuel_type):
        self.model_name = model_name
        self.number_of_cylinders = number_of_cylinders
        self.engine_displacement = engine_displacement
        self.engine_resource = engine_resource
        self.fuel_type = fuel_type

    def info_engine(self):
        print(f"model_name: {self.model_name},\n"
              f"number_of_cylinders:{self.number_of_cylinders},\n"
              f"engine_displacement:{self.engine_displacement},\n"
              f"engine_resource:{self.engine_resource} km,\n"
              f"fuel_type:{self.fuel_type}")


class EngineExtended(Engine):

    def __init__(self, model_name, number_of_cylinders, engine_displacement,
                 engine_resource, fuel_type,
                 current_engine_mileage, unique_number):
        Engine.__init__(self, model_name, number_of_cylinders,
                        engine_displacement, engine_resource, fuel_type)
        self.current_engine_mileage = current_engine_mileage
        self.unique_number = unique_number

    def uni_number(self, size=8, chars=None):
        if not chars:
            chars = string.ascii_uppercase + string.digits
        return "".join(random.choice(chars) for _ in range(size))

    def set_mileage_to_engine(self, number_km):

        self.current_engine_mileage = self.current_engine_mileage + number_km
        remaining_engine_life = (
                self.engine_resource - self.current_engine_mileage
        )
        print(f"remaining_engine_life:{remaining_engine_life},\n")
        return self.current_engine_mileage


a = Engine("BMW", 4, "3,2", 350000, "gas")
a.info_engine()
b = EngineExtended("Toyota", 4, "2", 350000, "petrol", 10000,
                   EngineExtended.uni_number(EngineExtended))
print(b.uni_number())
print(b.set_mileage_to_engine(300))
print(b.set_mileage_to_engine(400))
c = EngineExtended("Mersedes", 4, "1,6", 300000, "petrol", 150000,
                   EngineExtended.uni_number(EngineExtended))
print(c.uni_number())
print(b.set_mileage_to_engine(12))
