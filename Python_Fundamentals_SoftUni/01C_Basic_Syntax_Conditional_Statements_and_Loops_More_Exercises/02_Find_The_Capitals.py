single_string = list(input())
index_list = []

for index, char in enumerate(single_string):
    if char.isupper():
        index_list.append(index)

print(index_list)


