rows = int(input())
board = []

for _ in range(rows):
    board.append(input().split())

visited = []


def find_connected_dots(row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
        return 0

    if board[row][col] == "-" or board[row][col] == "–":
        return 0

    if [row, col] in visited:
        return 0

    visited.append([row, col])

    count = 1
    count += find_connected_dots(row - 1, col)
    count += find_connected_dots(row + 1, col)
    count += find_connected_dots(row, col - 1)
    count += find_connected_dots(row, col + 1)

    return count


max_dots = 0

for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] == "." and [row, col] not in visited:
            current_count = find_connected_dots(row, col)

            if current_count > max_dots:
                max_dots = current_count

print(max_dots)