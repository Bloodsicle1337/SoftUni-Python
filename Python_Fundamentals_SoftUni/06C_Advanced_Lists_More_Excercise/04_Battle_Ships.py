rows = int(input())
field = []

for _ in range(rows):
    current_row = input().split()
    row_data = []

    for element in current_row:
        row_data.append(int(element))

    field.append(row_data)

attacks = input().split()
destroyed_ships = 0

for attack in attacks:
    attack_data = attack.split("-")
    row = int(attack_data[0])
    col = int(attack_data[1])

    if field[row][col] > 0:
        field[row][col] -= 1

        if field[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)