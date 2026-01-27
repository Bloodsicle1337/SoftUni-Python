string_list = input().split()
integers_list = []

for string in string_list:
    string_value = int(string)
    integers_list.append(-int(string_value))

print(integers_list)