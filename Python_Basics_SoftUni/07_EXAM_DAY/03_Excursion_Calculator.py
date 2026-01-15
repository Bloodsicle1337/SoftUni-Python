number_of_people = int(input())
season = input()
total_price = 0

if season == "spring":
    if number_of_people <= 5:
        total_price += number_of_people * 50.00

    else:
        total_price += number_of_people * 48.00

elif season == "summer":
    if number_of_people <= 5:
        total_price += number_of_people * 48.50
        total_price -= total_price * 0.15

    else:
        total_price += number_of_people * 45.00
        total_price -= total_price * 0.15

elif season == "autumn":
    if number_of_people <= 5:
        total_price += number_of_people * 60.00

    else:
        total_price += number_of_people * 49.50

elif season == "winter":
    if number_of_people <= 5:
        total_price += number_of_people * 86.00
        total_price += total_price * 0.08

    else:
        total_price += number_of_people * 85.00
        total_price += total_price * 0.08

print(f"{total_price:.2f} leva.")