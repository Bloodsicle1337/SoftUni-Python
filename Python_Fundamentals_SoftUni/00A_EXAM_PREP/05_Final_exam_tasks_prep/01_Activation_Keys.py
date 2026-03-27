key = input()

command = input()

while command != "Generate":
    parts = command.split(">>>")
    action = parts[0]

    if action == "Contains":
        substring = parts[1]

        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        case, start, end = parts[1], int(parts[2]), int(parts[3])
        substring = key[start:end]

        if case == "Upper":
            key = key[:start] + substring.upper() + key[end:]
        else:
            key = key[:start] + substring.lower() + key[end:]

        print(key)

    elif action == "Slice":
        start, end = int(parts[1]), int(parts[2])
        key = key[:start] + key[end:]
        print(key)

    command = input()

print(f"Your activation key is: {key}")