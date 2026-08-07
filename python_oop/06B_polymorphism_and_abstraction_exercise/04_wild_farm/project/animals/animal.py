from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def feed(self, food: Food) -> str | None:
        pass


class Bird(Animal, ABC):
    def __init__(
        self,
        name: str,
        weight: float,
        wing_size: float
    ) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        animal_type = self.__class__.__name__

        return (
            f"{animal_type} "
            f"[{self.name}, {self.wing_size}, "
            f"{self.weight}, {self.food_eaten}]"
        )


class Mammal(Animal, ABC):
    def __init__(
        self,
        name: str,
        weight: float,
        living_region: str
    ) -> None:
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        animal_type = self.__class__.__name__

        return (
            f"{animal_type} "
            f"[{self.name}, {self.weight}, "
            f"{self.living_region}, {self.food_eaten}]"
        )