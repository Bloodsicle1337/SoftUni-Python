change = int(float(input()) * 100)

number_of_coins = 0

while change:
    if change >= 200:
        change -= 200

    elif change >= 100:
        change -= 100

    elif change >= 50:
        change -= 50

    elif change >= 20:
        change -= 20

    elif change >= 10:
        change -= 10

    elif change >= 5:
        change -= 5

    elif change >= 2:
        change -= 2

    elif change >= 1:
        change -= 1

    number_of_coins += 1

print(number_of_coins)