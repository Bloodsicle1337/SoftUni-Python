ORNAMENT_PRICE = 2
SKIRT_PRICE = 5
GARLAND_PRICE = 3
LIGHTS_PRICE = 15

total_cost = 0
total_spirit = 0
day_counter = 0

quantity_of_decorations_per_trip = int(input())
day_until_christmas = int(input())

for day in range(1, day_until_christmas + 1):
    day_counter += 1

    if day % 11 == 0:
        quantity_of_decorations_per_trip += 2

    if day % 10 == 0:
        total_spirit -= 20
        total_cost += (SKIRT_PRICE + GARLAND_PRICE + LIGHTS_PRICE)

    if day % 3 == 0 and day % 5 == 0:
        total_spirit += 30

    if day % 2 == 0:
        total_cost += ORNAMENT_PRICE * quantity_of_decorations_per_trip
        total_spirit += 5

    if day % 3 == 0:
        total_cost += (SKIRT_PRICE + GARLAND_PRICE) * quantity_of_decorations_per_trip
        total_spirit += 3 + 10

    if day % 5 == 0:
        total_cost += LIGHTS_PRICE * quantity_of_decorations_per_trip
        total_spirit += 17

if day_counter % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")