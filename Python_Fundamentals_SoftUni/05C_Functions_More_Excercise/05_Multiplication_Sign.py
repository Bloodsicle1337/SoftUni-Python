def multiplication_sign(first_num: int, second_num: int, third_num: int) -> str:
    if first_num == 0 or second_num == 0 or third_num == 0:
        return "zero"

    negative_count = 0

    if first_num < 0:
        negative_count += 1

    if second_num < 0:
        negative_count += 1

    if third_num < 0:
        negative_count += 1

    if negative_count % 2 == 0:
        return "positive"

    else:
        return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = multiplication_sign(first_number, second_number, third_number)
print(result)