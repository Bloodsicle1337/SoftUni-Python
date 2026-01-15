sum_of_all_prime_numbers = 0
sum_of_all_non_prime_numbers = 0

while True:
    number_input = input()

    if number_input == "stop":
        break

    number_input = int(number_input)

    if number_input < 0:
        print("Number is negative.")
        continue

    is_number_prime = True

    for number in range(2, number_input):
        if number_input % number == 0:
            is_number_prime = False
            break

    if is_number_prime:
        sum_of_all_prime_numbers += number_input
    else:
        sum_of_all_non_prime_numbers += number_input

print(f"Sum of all prime numbers is: {sum_of_all_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_all_non_prime_numbers}")