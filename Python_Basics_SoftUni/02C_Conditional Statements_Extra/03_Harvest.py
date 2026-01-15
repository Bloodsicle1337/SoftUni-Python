from math import ceil
from math import floor
grape_field = int(input())
grapes_per_square_meter = float(input())
total_grapes = grape_field * grapes_per_square_meter
wine_quota = int(input())
workers = int(input())

litters_of_wine_yield = total_grapes * 0.40 / 2.5

if litters_of_wine_yield < wine_quota:
    print(f"It will be a tough winter! More {floor(wine_quota - litters_of_wine_yield)} liters wine needed.")
else:
    left_wine = litters_of_wine_yield - wine_quota
    print(f"Good harvest this year! Total wine: {floor(litters_of_wine_yield)} liters.")
    print(f"{ceil(left_wine)} liters left -> {ceil(left_wine / workers)} liters per person.")