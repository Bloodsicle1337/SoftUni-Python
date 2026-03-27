numbers_as_string = input().split(", ")
numbers = []
even_indices = []

for current_number in numbers_as_string:
    numbers.append(int(current_number))

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        even_indices.append(index)

print(even_indices)