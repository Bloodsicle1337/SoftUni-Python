ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

flower_type = input()
number_of_flowers = int(input())
budget = int(input())

flower_price = 0

if flower_type == "Roses":
    flower_price += (ROSES_PRICE * number_of_flowers)

    if number_of_flowers > 80:
        flower_price -= flower_price * 0.10
elif flower_type == "Dahlias":
    flower_price += (DAHLIAS_PRICE * number_of_flowers)

    if number_of_flowers > 90:
        flower_price -= flower_price * 0.15
elif flower_type == "Tulips":
    flower_price += (TULIPS_PRICE * number_of_flowers)

    if number_of_flowers > 80:
        flower_price -= flower_price * 0.15
elif flower_type == "Narcissus":
    flower_price += (NARCISSUS_PRICE * number_of_flowers)

    if number_of_flowers < 120:
        flower_price += flower_price * 0.15
elif flower_type == "Gladiolus":
    flower_price += (GLADIOLUS_PRICE * number_of_flowers)

    if number_of_flowers < 80:
        flower_price += flower_price * 0.20

if budget >= flower_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {budget - flower_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {flower_price - budget:.2f} leva more.")