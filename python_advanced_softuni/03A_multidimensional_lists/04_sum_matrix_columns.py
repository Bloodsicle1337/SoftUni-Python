n_row, n_col = [int(x) for x in input().split(",")]

matrix = []

for row in range(n_row):
    data = [int(el) for el in input().split()]
    matrix.append(data)

for col_index in range(n_col):
    col_sum = 0

    for row_index in range(n_row):
        col_sum += matrix[row_index][col_index]

    print(col_sum)

