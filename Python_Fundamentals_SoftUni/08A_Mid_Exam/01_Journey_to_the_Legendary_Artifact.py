initial_energy = float(input())
artifact_pieces = 0
mountains_passed = 0
has_founded = False

while True:
    command = input()

    if command == "Journey ends here!":
        break

    if command == "mountain":
        initial_energy -= 10
        mountains_passed += 1

        if mountains_passed % 3 == 0:
            artifact_pieces += 1

            if artifact_pieces == 3:
                has_founded = True
                break

        if initial_energy <= 0:
            print("The character is too exhausted to carry on with the journey.")
            break

    elif command == "desert":
        initial_energy -= 15

        if initial_energy <= 0:
            print("The character is too exhausted to carry on with the journey.")
            break

    elif command == "forest":
        initial_energy += 7

if has_founded:
    print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")

elif initial_energy > 0:
    print(f"The character could not find all the pieces and needs {3 - artifact_pieces} more to complete the legendary artifact.")