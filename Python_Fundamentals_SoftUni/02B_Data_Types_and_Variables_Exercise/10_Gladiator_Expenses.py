number_of_loses = int(input())

helm_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = 0
broken_swords = 0
broken_shields = 0
broken_armors = 0

for loss in range(1, number_of_loses + 1):
    if loss % 2 == 0 and loss % 3 == 0:
        broken_shields += 1

        if broken_shields % 2 == 0 and broken_shields != 0:
            broken_armors += 1

    if loss % 2 == 0:
        broken_helmets += 1

    if loss % 3 == 0:
        broken_swords += 1

cost = ((broken_helmets * helm_price)
        + (broken_swords * sword_price)
        + (broken_shields * shield_price)
        + (broken_armors * armor_price))

print(f"Gladiator expenses: {cost:.02f} aureus")