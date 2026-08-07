from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 0.9

    def drive(self, distance: float):
        needed_fuel = distance * (
            self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION
        )

        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6
    REFUEL_PERCENTAGE = 0.95

    def drive(self, distance: float):
        needed_fuel = distance * (
            self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION
        )

        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * self.REFUEL_PERCENTAGE