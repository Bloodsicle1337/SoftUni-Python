number_of_male_clients = int(input())
number_of_female_clients = int(input())
total_number_of_tables = int(input())
number_of_used_tables = 0
result = ""

is_full = False


for male_on_table in range(1, number_of_male_clients + 1):

    for female_on_table in range(1, number_of_female_clients + 1):
        number_of_used_tables += 1
        result += f"({male_on_table} <-> {female_on_table}) "

        if number_of_used_tables >= total_number_of_tables:
            is_full = True
            break


    if is_full:
        break

print(result)