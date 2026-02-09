def mini_calculator(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b

    elif operator == "divide":
        if 0 < b:
            result = int(a / b)

    elif operator == "add":
        result = a + b

    elif operator == "subtract":
        result = a - b

    return result

input_operator = input()
first_number = int(input())
second_number = int(input())

print(mini_calculator(first_number, second_number, input_operator))