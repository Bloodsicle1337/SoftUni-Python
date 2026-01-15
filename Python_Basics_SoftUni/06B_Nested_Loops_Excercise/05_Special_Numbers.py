START = 1111
END = 9999

magic_number = int(input())

for number in range(START, END + 1):
    stringed_number = str(number)

    is_valid = True

    for char in stringed_number:
        char = int(char)
        if (char == 0) or magic_number % char != 0:
            is_valid = False
            break

    if is_valid:
        print(number, end=" ")