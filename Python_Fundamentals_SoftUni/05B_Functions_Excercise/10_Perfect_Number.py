def is_perfect(number: int) -> str:
    devisors_sum = 0
    for num in range(1, number):
        if number % num == 0:
            devisors_sum += num

    if number == devisors_sum:
        return "We have a perfect number!"

    else:
        return "It's not so perfect."

some_number = int(input())
result = is_perfect(some_number)

print(result)