budget = int(input())
season = input()
number_of_fisherman = int(input())
price = 0

if season == "Spring":
    price = 3000
    if 0 < number_of_fisherman <= 6:
        price -= price * 0.10
    elif 6 < number_of_fisherman <= 11:
        price -= price * 0.15
    elif number_of_fisherman > 12:
        price -= price * 0.25
elif (season == "Summer") or (season == "Autumn"):
    price = 4200
    if 0 < number_of_fisherman <= 6:
        price -= price * 0.10
    elif 6 < number_of_fisherman <= 11:
        price -= price * 0.15
    elif number_of_fisherman > 12:
        price -= price * 0.25
elif season == "Winter":
    price = 2600
    if 0 < number_of_fisherman <= 6:
        price -= price * 0.10
    elif 6 < number_of_fisherman <= 11:
        price -= price * 0.15
    elif number_of_fisherman > 12:
        price -= price * 0.25

if (number_of_fisherman % 2 == 0) and (season != "Autumn"):
    price -= price * 0.05

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")