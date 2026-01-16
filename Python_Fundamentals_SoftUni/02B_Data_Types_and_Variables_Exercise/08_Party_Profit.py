companions = int(input())
days_of_adventure = int(input())
coins = 0

for current_day in range(1, days_of_adventure + 1):
    if current_day % 10 == 0:
        companions -= 2

    if current_day % 15 == 0:
        companions += 5

    if current_day % 3 == 0:
        coins -= companions * 3

    if current_day % 5 == 0:
        coins += companions * 20

        if current_day % 3 == 0:
            coins -= companions * 2

    coins += 50
    coins -= companions * 2

split = coins // companions

print(f"{companions} companions received {split} coins each.")