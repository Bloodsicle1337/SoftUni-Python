n_row, n_col = [int(x) for x in input().split()]

matrix = []

for _ in range(n_row):
    data = [x for x in input().split()]
    matrix.append(data)

matches_found = 0
for row_index in range(n_row - 1):
    for col_index in range(n_col - 1):
        current = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        below_el = matrix[row_index + 1][col_index]
        diagonal_el = matrix[row_index + 1][col_index + 1]

        if (current == next_el) and (next_el == below_el) and (below_el == diagonal_el):
            matches_found += 1

print(matches_found)