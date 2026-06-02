rows = int(input())
matrix = []

for r in range(rows):
    data = [int(c) for c in input().split(", ") if int(c) % 2 == 0]
    matrix.append(data)

print(matrix)
