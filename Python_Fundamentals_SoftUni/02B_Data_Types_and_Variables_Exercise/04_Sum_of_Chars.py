number_of_lines = int(input())
total_sum = 0

for char in range(number_of_lines):
    character = ord(input())
    total_sum += character

print(f"The sum equals: {total_sum}")
