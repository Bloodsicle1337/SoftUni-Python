coffee = 0

while True:
    command = input()

    if command == "END":
        break


    if command.islower():
        if (command == "cat") or (command == "dog") or (command == "coding") or (command == "movie"):
            coffee += 1

        else:
            continue

    if command.isupper():
        if (command == "CAT") or (command == "DOG") or (command == "CODING") or (command == "MOVIE"):
            coffee += 2

        else:
            continue

if coffee > 5:
    print("You need extra sleep")

else:
    print(f"{coffee}")