from project.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10
    ALLOWED_FOODS = (Vegetable, Fruit)

    def make_sound(self) -> str:
        return "Squeak"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, self.ALLOWED_FOODS):
            return (
                f"{self.__class__.__name__} does not eat "
                f"{food.__class__.__name__}!"
            )

        self.weight += food.quantity * self.WEIGHT_INCREASE
        self.food_eaten += food.quantity

        return None


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40
    ALLOWED_FOODS = (Meat,)

    def make_sound(self) -> str:
        return "Woof!"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, self.ALLOWED_FOODS):
            return (
                f"{self.__class__.__name__} does not eat "
                f"{food.__class__.__name__}!"
            )

        self.weight += food.quantity * self.WEIGHT_INCREASE
        self.food_eaten += food.quantity

        return None


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30
    ALLOWED_FOODS = (Vegetable, Meat)

    def make_sound(self) -> str:
        return "Meow"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, self.ALLOWED_FOODS):
            return (
                f"{self.__class__.__name__} does not eat "
                f"{food.__class__.__name__}!"
            )

        self.weight += food.quantity * self.WEIGHT_INCREASE
        self.food_eaten += food.quantity

        return None


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00
    ALLOWED_FOODS = (Meat,)

    def make_sound(self) -> str:
        return "ROAR!!!"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, self.ALLOWED_FOODS):
            return (
                f"{self.__class__.__name__} does not eat "
                f"{food.__class__.__name__}!"
            )

        self.weight += food.quantity * self.WEIGHT_INCREASE
        self.food_eaten += food.quantity

        return None