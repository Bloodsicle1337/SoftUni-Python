number_of_lines = int(input())

for _ in range(number_of_lines):
    text = input()

    start_name_index = text.index("@") + 1
    end_name_index = text.index("|")
    name = text[start_name_index:end_name_index]

    start_age_index = text.index("#") + 1
    end_age_index = text.index("*")
    age = text[start_age_index:end_age_index]

    print(f"{name} is {age} years old.")