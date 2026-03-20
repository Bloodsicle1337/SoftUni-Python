def min_max_and_sum(integers: list) -> str:
    list_as_integers = []

    for num in integers:
        list_as_integers.append(int(num))

    sum_of_integers = sum(list_as_integers)
    min_number = min(list_as_integers)
    max_number = max(list_as_integers)

    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_of_integers}"

integers_list_str = input().split()
result = min_max_and_sum(integers_list_str)
print(result)
