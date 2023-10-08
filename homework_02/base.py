import dataclasses
from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight=500, fuel=200, fuel_consumption=4):
        self.weight = weight
        self.started = None
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


Car = Vehicle(weight=1000)
print(Car)
