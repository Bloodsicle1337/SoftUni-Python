MUMS_SPRING_SUMMER = 2.00
MUMS_FALL_WINTER = 3.75

ROSES_SPRING_SUMMER = 4.10
ROSES_FALL_WINTER = 4.50

TULIPS_SPRING_SUMMER = 2.50
TULIPS_FALL_WINTER = 4.15

BOUQUET = 2

number_of_mums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
holiday = input()

all_flowers = number_of_mums + number_of_roses + number_of_tulips
flower_price = 0

if season == "Spring":
    flower_price = ((number_of_mums * MUMS_SPRING_SUMMER) +
             (number_of_roses * ROSES_SPRING_SUMMER) +
             (number_of_tulips * TULIPS_SPRING_SUMMER))
    if holiday == "Y":
        flower_price += flower_price * 0.15
    if number_of_tulips > 7:
        flower_price -= flower_price * 0.05
if season == "Summer":
    flower_price = ((number_of_mums * MUMS_SPRING_SUMMER) +
             (number_of_roses * ROSES_SPRING_SUMMER) +
             (number_of_tulips * TULIPS_SPRING_SUMMER))
    if holiday == "Y":
        flower_price += flower_price * 0.15
if season == "Autumn":
    flower_price = ((number_of_mums * MUMS_FALL_WINTER) +
             (number_of_roses * ROSES_FALL_WINTER) +
             (number_of_tulips * TULIPS_FALL_WINTER))
    if holiday == "Y":
        flower_price += flower_price * 0.15
if season == "Winter":
    flower_price = ((number_of_mums * MUMS_FALL_WINTER) +
             (number_of_roses * ROSES_FALL_WINTER) +
             (number_of_tulips * TULIPS_FALL_WINTER))
    if number_of_roses >= 10:
        flower_price -= flower_price * 0.10
    if holiday == "Y":
        flower_price += flower_price * 0.15

if all_flowers > 20:
    flower_price -= flower_price * 0.20

final_price = flower_price + BOUQUET

print(f"{final_price:.2f}")


