number_of_strings = int(input())

for string in range(number_of_strings):
    string_input = input()

    if "," in string_input or "." in string_input or "_" in string_input:
        print(f"{string_input} is not pure!")

    else:
        print(f"{string_input} is pure.")