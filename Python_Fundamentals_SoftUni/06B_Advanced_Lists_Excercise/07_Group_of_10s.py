numbers_as_string = input().split(", ")
numbers = []

for number in numbers_as_string:
    numbers.append(int(number))

group = 10

while len(numbers) > 0:
    current_group = []

    for number in numbers:
        if number <= group:
            current_group.append(number)

    print(f"Group of {group}'s: {current_group}")

    for number in current_group:
        numbers.remove(number)

    group += 10