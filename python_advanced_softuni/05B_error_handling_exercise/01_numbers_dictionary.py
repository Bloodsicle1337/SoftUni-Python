numbers = {}

current_input = input()

while current_input != "Search":
    key = current_input

    try:
        value = int(input())
        numbers[key] = value
    except ValueError:
        print("The variable number must be an integer")

    current_input = input()


current_input = input()

while current_input != "Remove":
    key_to_find = current_input

    try:
        print(numbers[key_to_find])
    except KeyError:
        print("Number does not exist in dictionary")

    current_input = input()


current_input = input()

while current_input != "End":
    key_to_delete = current_input

    try:
        del numbers[key_to_delete]
    except KeyError:
        print("Number does not exist in dictionary")

    current_input = input()


print(numbers)