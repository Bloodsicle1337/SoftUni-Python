SIZE = 5

matrix = []

shooter_row = 0
shooter_col = 0

total_targets = 0
shot_targets = []

for row in range(SIZE):
    current_row = input().split()
    matrix.append(current_row)

    if "A" in current_row:
        shooter_row = row
        shooter_col = current_row.index("A")

    total_targets += current_row.count("x")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

commands_count = int(input())

for _ in range(commands_count):
    command_parts = input().split()
    action = command_parts[0]
    direction = command_parts[1]

    row_change, col_change = directions[direction]

    if action == "move":
        steps = int(command_parts[2])

        next_row = shooter_row + row_change * steps
        next_col = shooter_col + col_change * steps

        if 0 <= next_row < SIZE and 0 <= next_col < SIZE:
            if matrix[next_row][next_col] == ".":
                matrix[shooter_row][shooter_col] = "."
                shooter_row = next_row
                shooter_col = next_col
                matrix[shooter_row][shooter_col] = "A"

    elif action == "shoot":
        bullet_row = shooter_row + row_change
        bullet_col = shooter_col + col_change

        while 0 <= bullet_row < SIZE and 0 <= bullet_col < SIZE:
            if matrix[bullet_row][bullet_col] == "x":
                matrix[bullet_row][bullet_col] = "."
                shot_targets.append([bullet_row, bullet_col])
                break

            bullet_row += row_change
            bullet_col += col_change

    if len(shot_targets) == total_targets:
        break

if len(shot_targets) == total_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    targets_left = total_targets - len(shot_targets)
    print(f"Training not completed! {targets_left} targets left.")

for target in shot_targets:
    print(target)