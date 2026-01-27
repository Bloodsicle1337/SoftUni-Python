list_of_str_integers = input().split()
numbers_to_remove = int(input())
list_of_integers = []
list_of_removed_integers = []
list_to_adjust_str = []
for string in list_of_str_integers:
    int_string = int(string)
    list_of_integers.append(int_string)

list_to_adjust = list_of_integers.copy()
list_of_integers.sort()
list_of_removed_integers = list_of_integers[:numbers_to_remove]

for number in list_of_removed_integers:
    list_to_adjust.remove(number)

for index in range(len(list_to_adjust)):
    stringed_index = str(list_to_adjust[index])
    list_to_adjust_str.append(stringed_index)

result = (", ".join(list_to_adjust_str))
print(result)
