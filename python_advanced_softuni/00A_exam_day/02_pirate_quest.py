n = int(input())

sea_map = []
ship_row = 0
ship_col = 0
treasures = 0

for row in range(n):
    line = [char for char in input()]
    sea_map.append(line)

    if "S" in line:
        ship_row = row
        ship_col = line.index("S")

    treasures += line.count("*")

durability = 100
charm_used = False

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

sea_map[ship_row][ship_col] = "."

while treasures > 0 and durability > 0:
    command = input()

    if command == "stop":
        break

    next_row = ship_row + directions[command][0]
    next_col = ship_col + directions[command][1]

    if next_row < 0:
        next_row = n -1
    elif next_row == n:
        next_row = 0

    if next_col < 0:
        next_col = n - 1
    elif next_col == n:
        next_col = 0

    ship_row, ship_col = next_row, next_col

    current_position = sea_map[ship_row][ship_col]

    if current_position == "*":
        treasures -= 1
        sea_map[ship_row][ship_col] = "."

    elif current_position == "M":
        durability -= 25
        sea_map[ship_row][ship_col] = "."

    elif current_position == "C":
        if not charm_used:
            durability += 25

            if durability > 100:
                durability = 100

            charm_used = True

        sea_map[ship_row][ship_col] = "."

sea_map[ship_row][ship_col] = "S"

if durability <= 0:
    print(f"Shipwreck! Last known coordinates ({ship_row}, {ship_col})")

elif treasures == 0:
    print("Yo-ho-ho! All treasure chests collected!")

else:
    print("Retreat! Some treasures remain unclaimed.")

print(f"Ship Durability: {durability}")

if treasures > 0:
    print(f"Unclaimed chests: {treasures}")

for row in sea_map:
    print("".join(row))