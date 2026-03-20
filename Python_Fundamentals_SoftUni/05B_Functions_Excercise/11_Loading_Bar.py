def loading_bar(number: int) -> str:
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    percentage_numbers = number // 10
    number_of_dots = 10 - percentage_numbers
    return f"{number}% [{'%' * percentage_numbers}{'.' * number_of_dots}]\nStill loading..."
some_number = int(input())

result = loading_bar(some_number)
print(result)