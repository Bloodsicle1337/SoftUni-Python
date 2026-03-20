def sorting(numbers: list) -> list:
    list_as_digits = []
    for num in numbers:
        list_as_digits.append(int(num))
    sorted_list = sorted(list_as_digits)
    return sorted_list

numbers_list = input().split()
result = sorting(numbers_list)

print(result)
