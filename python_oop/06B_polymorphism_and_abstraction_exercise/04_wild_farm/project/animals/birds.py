from project.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    def make_sound(self) -> str:
        return "Hoot Hoot"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, Meat):
            return (
                f"{self.__class__.__name__} does not eat "
                f"{food.__class__.__name__}!"
            )

        self.weight += food.quantity * self.WEIGHT_INCREASE
        self.food_eaten += food.quantity

        return None


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    def make_sound(self) -> str:
        return "Cluck"

    def feed(self, food: Food) -> None:
        self.weight += food.quantity * self.WEIGHT_INCREASE
        self.food_eaten += food.quantity