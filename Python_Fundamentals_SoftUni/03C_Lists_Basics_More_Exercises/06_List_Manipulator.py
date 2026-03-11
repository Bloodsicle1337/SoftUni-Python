numbers_as_string = input().split()
numbers = []

for current_number in numbers_as_string:
    numbers.append(int(current_number))

while True:
    command = input()

    if command == "end":
        break

    command_data = command.split()
    action = command_data[0]

    if action == "exchange":
        index = int(command_data[1])

        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            left_part = numbers[:index + 1]
            right_part = numbers[index + 1:]
            numbers = right_part + left_part

    elif action == "max":
        element_type = command_data[1]
        max_number = -1000000
        found_index = -1

        for index in range(len(numbers)):
            current_number = numbers[index]

            if element_type == "even":
                if current_number % 2 == 0:
                    if current_number >= max_number:
                        max_number = current_number
                        found_index = index

            elif element_type == "odd":
                if current_number % 2 != 0:
                    if current_number >= max_number:
                        max_number = current_number
                        found_index = index

        if found_index == -1:
            print("No matches")
        else:
            print(found_index)

    elif action == "min":
        element_type = command_data[1]
        min_number = 1000000
        found_index = -1

        for index in range(len(numbers)):
            current_number = numbers[index]

            if element_type == "even":
                if current_number % 2 == 0:
                    if current_number <= min_number:
                        min_number = current_number
                        found_index = index

            elif element_type == "odd":
                if current_number % 2 != 0:
                    if current_number <= min_number:
                        min_number = current_number
                        found_index = index

        if found_index == -1:
            print("No matches")
        else:
            print(found_index)

    elif action == "first":
        count = int(command_data[1])
        element_type = command_data[2]
        searched_numbers = []

        if count > len(numbers):
            print("Invalid count")
        else:
            for number in numbers:
                if element_type == "even":
                    if number % 2 == 0:
                        searched_numbers.append(number)

                elif element_type == "odd":
                    if number % 2 != 0:
                        searched_numbers.append(number)

                if len(searched_numbers) == count:
                    break

            print(searched_numbers)

    elif action == "last":
        count = int(command_data[1])
        element_type = command_data[2]
        searched_numbers = []

        if count > len(numbers):
            print("Invalid count")
        else:
            for index in range(len(numbers) - 1, -1, -1):
                current_number = numbers[index]

                if element_type == "even":
                    if current_number % 2 == 0:
                        searched_numbers.append(current_number)

                elif element_type == "odd":
                    if current_number % 2 != 0:
                        searched_numbers.append(current_number)

                if len(searched_numbers) == count:
                    break

            searched_numbers.reverse()
            print(searched_numbers)

print(numbers)