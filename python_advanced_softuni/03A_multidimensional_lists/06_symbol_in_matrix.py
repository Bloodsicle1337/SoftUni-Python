n = int(input())
matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

searched_symbol = input()

position = None
is_found = False


for i in range(n):
    for j in range(n):
        if matrix[i][j] == searched_symbol:
            position = (i, j)
            is_found = True
            break
        if is_found:
            break
if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")