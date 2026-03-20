def smallest_number(first_number: int, second_number: int, third_number: int) -> int:
    if first_number < second_number and first_number < third_number:
        return first_number

    elif second_number < first_number and second_number < third_number:
        return second_number

    else:
        return third_number

first= int(input())
second = int(input())
third = int(input())

print(smallest_number(first, second, third))