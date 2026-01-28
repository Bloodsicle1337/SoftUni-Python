single_string = input().split(", ")
single_integers = []
target_value = 0
target_list = []

for string in single_string:
    string_int = int(string)
    if string_int == 0:
        target_list.append(string_int)

    else:
        single_integers.append(string_int)

for zero in target_list:
    single_integers.append(zero)

print(single_integers)
