def tribonacci_sequence(number: int) -> str:
    sequence = []

    for current_index in range(1, number + 1):
        if current_index == 1 or current_index == 2:
            sequence.append(1)

        elif current_index == 3:
            sequence.append(2)

        else:
            new_number = sequence[-1] + sequence[-2] + sequence[-3]
            sequence.append(new_number)

    return " ".join(str(num) for num in sequence)

count = int(input())
result = tribonacci_sequence(count)
print(result)