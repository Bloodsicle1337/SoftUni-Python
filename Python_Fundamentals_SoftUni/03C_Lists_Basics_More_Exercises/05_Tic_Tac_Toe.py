first_row = input().split()
second_row = input().split()
third_row = input().split()

board = [first_row, second_row, third_row]
winner = ""

for row in board:
    if row[0] == row[1] == row[2] and row[0] != "0":
        winner = row[0]

first_col = [board[0][0], board[1][0], board[2][0]]
second_col = [board[0][1], board[1][1], board[2][1]]
third_col = [board[0][2], board[1][2], board[2][2]]

for col in [first_col, second_col, third_col]:
    if col[0] == col[1] == col[2] and col[0] != "0":
        winner = col[0]

left_diagonal = [board[0][0], board[1][1], board[2][2]]
right_diagonal = [board[0][2], board[1][1], board[2][0]]

if left_diagonal[0] == left_diagonal[1] == left_diagonal[2] and left_diagonal[0] != "0":
    winner = left_diagonal[0]

elif right_diagonal[0] == right_diagonal[1] == right_diagonal[2] and right_diagonal[0] != "0":
    winner = right_diagonal[0]

if winner == "1":
    print("First player won")
elif winner == "2":
    print("Second player won")
else:
    print("Draw!")