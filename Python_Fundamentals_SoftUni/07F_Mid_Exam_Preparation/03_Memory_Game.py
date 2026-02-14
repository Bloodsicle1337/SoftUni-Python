elements = input().split()
moves = 0

command = input()
while command != "end":
    moves += 1
    first_idx, second_idx = map(int, command.split())

    invalid = (
        first_idx == second_idx
        or first_idx < 0 or first_idx >= len(elements)
        or second_idx < 0 or second_idx >= len(elements)
    )

    if invalid:
        middle = len(elements) // 2
        penalty = f"-{moves}a"
        elements.insert(middle, penalty)
        elements.insert(middle, penalty)
        print("Invalid input! Adding additional elements to the board")
    else:
        first_el = elements[first_idx]
        second_el = elements[second_idx]

        if first_el == second_el:
            print(f"Congrats! You have found matching elements - {first_el}!")
            for idx in sorted([first_idx, second_idx], reverse=True):
                elements.pop(idx)
        else:
            print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

    command = input()

if command == "end" and len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(elements))