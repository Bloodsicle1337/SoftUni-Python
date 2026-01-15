import sys
number = int(input())
sum_of_numbers = 0
max_number = -sys.maxsize

for _ in range(number):
    n = int(input())
    if n >= max_number:
        max_number = n
    sum_of_numbers += n
new_sum = sum_of_numbers - max_number
if max_number == new_sum:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - new_sum)}")