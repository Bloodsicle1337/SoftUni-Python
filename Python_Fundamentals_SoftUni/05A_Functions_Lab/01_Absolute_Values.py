def absolute_numbers(string):
    stringed_list = string.split()
    floater_list = []
    for number in stringed_list:
        floater = float(number)
        floater_list.append(abs(floater))

    return floater_list

print(absolute_numbers(input()))