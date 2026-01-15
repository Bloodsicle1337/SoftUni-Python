max_number = int(input())

for first in range(1, max_number + 1):
    print("*" * first)

for second in range(max_number - 1, 0, -1):
    print("*" * second)