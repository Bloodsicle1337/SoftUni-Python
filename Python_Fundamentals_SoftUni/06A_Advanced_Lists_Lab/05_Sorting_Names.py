names = input().split(", ")

for first_index in range(len(names)):
    for second_index in range(first_index + 1, len(names)):
        first_name = names[first_index]
        second_name = names[second_index]

        if len(first_name) < len(second_name):
            names[first_index], names[second_index] = names[second_index], names[first_index]

        elif len(first_name) == len(second_name):
            if first_name > second_name:
                names[first_index], names[second_index] = names[second_index], names[first_index]

print(names)