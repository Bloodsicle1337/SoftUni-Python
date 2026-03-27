password = input()

command = input()

while command != "Done":
    parts = command.split()
    action = parts[0]

    if action == "TakeOdd":
        password = "".join(password[i] for i in range(1, len(password), 2))
        print(password)

    elif action == "Cut":
        index, length = int(parts[1]), int(parts[2])
        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
        print(password)

    elif action == "Substitute":
        substring, substitute = parts[1], parts[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")