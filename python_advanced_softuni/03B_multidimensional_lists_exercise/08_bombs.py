size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

bombs = input().split()

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(",")]

    bomb_value = matrix[row][col]

    if bomb_value <= 0:
        continue

    for row_change, col_change in directions:
        current_row = row + row_change
        current_col = col + col_change

        if 0 <= current_row < size and 0 <= current_col < size:
            if matrix[current_row][current_col] > 0:
                matrix[current_row][current_col] -= bomb_value

    matrix[row][col] = 0

alive_cells = 0
sum_of_cells = 0

for row in matrix:
    for value in row:
        if value > 0:
            alive_cells += 1
            sum_of_cells += value

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")

for row in matrix:
    print(*row)