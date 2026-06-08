rows, cols = [int(x) for x in input().split()]

matrix = []
player_row = 0
player_col = 0

for row in range(rows):
    current_row = list(input())

    if "P" in current_row:
        player_row = row
        player_col = current_row.index("P")

    matrix.append(current_row)

commands = input()

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

won = False
dead = False


def spread_bunnies():
    new_bunnies = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                new_bunnies.append((row, col))

    for row, col in new_bunnies:
        for row_change, col_change in directions.values():
            current_row = row + row_change
            current_col = col + col_change

            if 0 <= current_row < rows and 0 <= current_col < cols:
                matrix[current_row][current_col] = "B"


for command in commands:
    row_change, col_change = directions[command]

    next_row = player_row + row_change
    next_col = player_col + col_change

    matrix[player_row][player_col] = "."

    if not (0 <= next_row < rows and 0 <= next_col < cols):
        won = True

    elif matrix[next_row][next_col] == "B":
        dead = True
        player_row = next_row
        player_col = next_col

    else:
        player_row = next_row
        player_col = next_col
        matrix[player_row][player_col] = "P"

    spread_bunnies()

    if won:
        break

    if matrix[player_row][player_col] == "B":
        dead = True
        break

for row in matrix:
    print("".join(row))

if won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")