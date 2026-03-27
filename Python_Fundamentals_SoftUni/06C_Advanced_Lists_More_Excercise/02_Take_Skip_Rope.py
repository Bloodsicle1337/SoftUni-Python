text = input()

numbers = []
non_numbers = []

for char in text:
    if char.isdigit():
        numbers.append(int(char))
    else:
        non_numbers.append(char)

take_list = []
skip_list = []

for index in range(len(numbers)):
    if index % 2 == 0:
        take_list.append(numbers[index])
    else:
        skip_list.append(numbers[index])

result = ""
current_index = 0

for index in range(len(take_list)):
    take_count = take_list[index]
    skip_count = skip_list[index]

    for char_index in range(current_index, current_index + take_count):
        if char_index < len(non_numbers):
            result += non_numbers[char_index]

    current_index += take_count
    current_index += skip_count

print(result)