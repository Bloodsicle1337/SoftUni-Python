START = 1111
END = 9999

lucky_number = int(input())

for number in range(START, END + 1):
    stringed_num = str(number)
    d0 = 0
    d1 = 0
    d2 = 0
    d3 = 0
    is_invalid = False

    for index, digit in enumerate(stringed_num):
        if digit == "0":
            is_invalid = True
            break

        if index == 0:
            d0 = int(digit)

        elif index == 1:
            d1 = int(digit)

        elif index == 2:
            d2 = int(digit)

        elif index == 3:
            d3 = int(digit)

    if is_invalid:
        continue

    if (d0 + d1) == (d2 + d3):
        if lucky_number % (d0 + d1) == 0:
            print(number, end=" ")
