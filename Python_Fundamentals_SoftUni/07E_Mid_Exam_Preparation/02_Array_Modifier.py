numbers = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        break

    parts = command.split()
    action = parts[0]

    if action == "swap":
        index1 = int(parts[1])
        index2 = int(parts[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

    elif action == "multiply":
        index1 = int(parts[1])
        index2 = int(parts[2])
        numbers[index1] = numbers[index1] * numbers[index2]

    elif action == "decrease":
        for i in range(len(numbers)):
            numbers[i] -= 1

print(", ".join(map(str, numbers)))