first_number_max = int(input())
second_number_max = int(input())
third_number_max = int(input())
result = ""

for first_number in range(1, first_number_max + 1):
    if first_number % 2 != 0:
        continue

    for second_number in range(2, second_number_max + 1):
        is_prime = True

        for div in range(2, second_number):
            if second_number % div == 0:
                is_prime = False
                break
        if not is_prime:
            continue

        for third_number in range(1, third_number_max + 1):

            if third_number % 2 != 0:
                continue

            else:
                result += f"{first_number} {second_number} {third_number}\n"

print(result)