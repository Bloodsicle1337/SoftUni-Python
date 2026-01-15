number = int(input()) # 0, 1, 2, 3
left_sum = 0
right_sum = 0

for i in range(number * 2): # 0, 1, 2, 3, 4, 5, 6
    new_number = int(input())
    if i < number:
        left_sum += new_number
    else:
        right_sum += new_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(right_sum - left_sum)}")
