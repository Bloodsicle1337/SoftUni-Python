groceries = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break

    parts = command.split()
    action = parts[0]

    if action == "Urgent":
        item = parts[1]
        if item not in groceries:
            groceries.insert(0, item)

    elif action == "Unnecessary":
        item = parts[1]
        if item in groceries:
            groceries.remove(item)

    elif action == "Correct":
        old_item = parts[1]
        new_item = parts[2]
        if old_item in groceries:
            index = groceries.index(old_item)
            groceries[index] = new_item

    elif action == "Rearrange":
        item = parts[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(", ".join(groceries))