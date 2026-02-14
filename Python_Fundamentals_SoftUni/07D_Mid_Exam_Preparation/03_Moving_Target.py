targets = list(map(int, input().split()))

while True:
    command = input()

    if command == "End":
        break

    parts = command.split()
    action = parts[0]
    index = int(parts[1])
    value = int(parts[2])

    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = value
        left = index - radius
        right = index + radius

        if 0 <= left and right < len(targets):
            for _ in range(right - left + 1):
                targets.pop(left)
        else:
            print("Strike missed!")

print("|".join(map(str, targets)))