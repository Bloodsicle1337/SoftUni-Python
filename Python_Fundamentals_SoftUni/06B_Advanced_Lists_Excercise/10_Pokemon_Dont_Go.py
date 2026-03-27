numbers_as_string = input().split()
numbers = []

for number in numbers_as_string:
    numbers.append(int(number))

removed_elements_sum = 0

while len(numbers) > 0:
    index = int(input())

    if index < 0:
        removed_element = numbers[0]
        removed_elements_sum += removed_element
        numbers[0] = numbers[-1]

    elif index > len(numbers) - 1:
        removed_element = numbers[-1]
        removed_elements_sum += removed_element
        numbers[-1] = numbers[0]

    else:
        removed_element = numbers.pop(index)
        removed_elements_sum += removed_element

    for current_index in range(len(numbers)):
        if numbers[current_index] <= removed_element:
            numbers[current_index] += removed_element
        else:
            numbers[current_index] -= removed_element

print(removed_elements_sum)