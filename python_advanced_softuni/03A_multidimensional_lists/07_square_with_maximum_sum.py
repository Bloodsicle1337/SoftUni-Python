n_row, n_col = [int(x) for x in input().split(",")]

matrix = []

for _ in range(n_row):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)

max_sum = float("-inf")
sub_matrix = []
for row_index in range(n_row - 1):
    for col_index in range(n_col - 1):
        current = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        below_el = matrix[row_index + 1][col_index]
        diagonal_el = matrix[row_index + 1][col_index + 1]

        sum_elements = current + next_el + below_el + diagonal_el
        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [
                [current, next_el],
                [below_el, diagonal_el]
            ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)