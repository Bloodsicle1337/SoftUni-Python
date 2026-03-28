coded_message = input()
command = input()
updated_message = ""

while command != "Finalize":
    parts = command.split()
    action = parts[0]

    if action == "Encrypt":
        updated_message = coded_message[::-1]
        print(updated_message)
        coded_message = updated_message

    elif action == "Decrypt":
        updated_message = ""

        for char in coded_message:
            if char.islower():
                updated_message += char.upper()
            elif char.isupper():
                updated_message += char.lower()
            else:
                updated_message += char

        print(updated_message)
        coded_message = updated_message

    elif action == "Substitute":
        updated_message = ""
        old_char, new_char = parts[1], parts[2]

        if old_char not in coded_message:
            print("Character not found.")
        else:
            for char2 in coded_message:
                if char2 == old_char:
                    char2 = new_char
                updated_message += char2

            print(updated_message)
            coded_message = updated_message

    elif action == "Scramble":
        index_action, character = int(parts[1]), parts[2]
        updated_message = ""

        if index_action < 0 or index_action >= len(coded_message):
            print("Index out of bounds.")
        else:
            for index in range(len(coded_message)):
                if index == index_action:
                    updated_message += character
                else:
                    updated_message += coded_message[index]

            print(updated_message)
            coded_message = updated_message

    elif action == "Remove":
        updated_message = ""
        substring = parts[1]

        updated_message = coded_message.replace(substring, "")
        print(updated_message)
        coded_message = updated_message

    else:
        print("Invalid command detected!")

    command = input()