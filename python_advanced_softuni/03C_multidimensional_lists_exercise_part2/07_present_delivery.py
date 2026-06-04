presents = int(input())
n = int(input())

matrix = []

santa_row = 0
santa_col = 0

nice_kids = 0
happy_nice_kids = 0

for row in range(n):
    current_row = input().split()
    matrix.append(current_row)

    if "S" in current_row:
        santa_row = row
        santa_col = current_row.index("S")

    nice_kids += current_row.count("V")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while presents > 0:
    command = input()

    if command == "Christmas morning":
        break

    row_change, col_change = directions[command]

    matrix[santa_row][santa_col] = "-"

    santa_row += row_change
    santa_col += col_change

    current_cell = matrix[santa_row][santa_col]

    if current_cell == "V":
        presents -= 1
        happy_nice_kids += 1

    elif current_cell == "C":
        for direction in directions:
            kid_row_change, kid_col_change = directions[direction]

            kid_row = santa_row + kid_row_change
            kid_col = santa_col + kid_col_change

            if matrix[kid_row][kid_col] == "V":
                presents -= 1
                happy_nice_kids += 1
                matrix[kid_row][kid_col] = "-"

            elif matrix[kid_row][kid_col] == "X":
                presents -= 1
                matrix[kid_row][kid_col] = "-"

            if presents == 0:
                break

    matrix[santa_row][santa_col] = "S"

if presents == 0 and happy_nice_kids < nice_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(" ".join(row))

if happy_nice_kids == nice_kids:
    print(f"Good job, Santa! {happy_nice_kids} happy nice kid/s.")
else:
    nice_kids_left = nice_kids - happy_nice_kids
    print(f"No presents for {nice_kids_left} nice kid/s.")