from math import floor
from math import ceil

number_of_days_off = int(input())
food_prepared = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_kg = float(input()) / 1000

needed_food = ((number_of_days_off * dog_food_per_day_kg) +
               (number_of_days_off * cat_food_per_day_kg) +
               (number_of_days_off * turtle_food_per_day_kg))


if needed_food < food_prepared:
    print(f"{floor(food_prepared - needed_food)} kilos of food left.")
else:
    print(f"{ceil(needed_food - food_prepared)} more kilos of food are needed.")