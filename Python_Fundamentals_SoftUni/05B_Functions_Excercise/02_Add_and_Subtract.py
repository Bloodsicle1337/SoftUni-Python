def sum_number(first_int: int, second_int: int) -> int:
    result = first_int + second_int
    return result

def subtract(sum_numbers_return: int, third_int: int) -> int:
    sub_result = sum_numbers_return - third_int
    return sub_result

def add_and_subtract(first_number: int, second_number: int, third_number: int) -> int:
    result_this = sum_number(first_number, second_number)
    final_result = subtract(result_this, third_number)
    return final_result


first = int(input())
second = int(input())
third = int(input())

display_result = add_and_subtract(first, second, third)
print(display_result)