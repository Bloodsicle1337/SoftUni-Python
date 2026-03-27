rows = int(input())
maze = []

kate_row = 0
kate_col = 0

for row in range(rows):
    current_row = list(input())

    if "k" in current_row:
        kate_row = row
        kate_col = current_row.index("k")

    maze.append(current_row)

visited = []


def find_longest_path(row, col):
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[row]):
        return 1

    if maze[row][col] == "#":
        return 0

    if [row, col] in visited:
        return 0

    visited.append([row, col])

    up = find_longest_path(row - 1, col)
    down = find_longest_path(row + 1, col)
    left = find_longest_path(row, col - 1)
    right = find_longest_path(row, col + 1)

    visited.remove([row, col])

    longest_path = max(up, down, left, right)

    if longest_path == 0:
        return 0

    return longest_path + 1


result = find_longest_path(kate_row, kate_col)

if result == 0:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {result - 1} moves")