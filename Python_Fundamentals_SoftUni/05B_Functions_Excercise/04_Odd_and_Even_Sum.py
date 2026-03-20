def odd_even_sum(number: str) -> str:
    sum_of_odd = 0
    sum_of_even = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}"
input_number = input()

result = odd_even_sum(input_number)
print(result)
