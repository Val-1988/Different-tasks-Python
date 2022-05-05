#Create car_factory.py .
# Inside realize a class Car.
# Each instance has a type (types examples: Wagon, Sedan, Hatchback, Coupe),
# model, win_code, model, color (Red, Black, White, Gray, Silver).
# Win code generates as A-B-CCCC-DD-EEEEEEE,
# where A is the first letter of type,
# B - first letter of the color, CCCC - year,
# DD - month, EEEEEEE - unique number.
# Brand is the class attribute.
# Engine instance pass as an attribute.
# Create one classmethod, one staticmethod for this class with any usful logic.

import random
import string
import datetime


class Engine:

    def __init__(self, type_fuel, number_of_cylinders):
        self.type_fuel = type_fuel
        self.number_of_cylinders = number_of_cylinders

    def engine_discript(self):
        print(f"number of cylinders: {self.number_of_cylinders},\n")
        print(f"type_fuel: {self.type_fuel}, \n")


class Car:
    BRAND = "Toyota"

    def __init__(self,
                 car_type,
                 model,
                 year, color,
                 type_fuel,
                 number_of_cylinders):
        self.car_type = car_type
        self.model = model
        self.year = year
        self.color = color
        self.engine = Engine(type_fuel, number_of_cylinders)

    @classmethod
    def car_descript(cls):
        print("This Car:", cls.BRAND)

    @staticmethod
    def fuel_consumption(fuel_volume, distance):
        consumption = fuel_volume*100/distance
        return consumption

    def win(self, size=7, month="10"):
        chars = string.ascii_uppercase + string.digits
        e = "".join(random.choice(chars) for _ in range(size))
        self.win_code = f"{self.car_type[0]}-{self.color[0]}-{self.year}" \
                        f"-{month}-{e}"
        return self.win_code


a = Car("Wagon", "AnyModel", "2021", "RED", "gas", "4")
b = Car("Sedan", "TheOtherModel", "1988", "Gray", "electricity", "4")
print(a.win())
print(b.win())
print(b.engine.engine_discript())
print(Car.fuel_consumption(7, 120))
print(Car.car_descript())

