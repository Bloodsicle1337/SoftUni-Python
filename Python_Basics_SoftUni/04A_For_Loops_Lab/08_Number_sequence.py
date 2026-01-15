import sys

number = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize

for _ in range(number):
    n = int(input())
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")