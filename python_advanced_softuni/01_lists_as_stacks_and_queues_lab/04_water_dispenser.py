from collections import deque

dispenser_liters = int(input())
command = input()
people_wanting_water = deque()

while command != "Start":
    people_wanting_water.append(command)
    command = input()

while command != "End":
    command = input()

    if "refill" in command:

        dispenser_liters += int(command.split()[1])

    elif command.isdigit():
        if dispenser_liters >= int(command):
            dispenser_liters -= int(command)
            print(f"{people_wanting_water.popleft()} got water")

        else:
            print(f"{people_wanting_water.popleft()} must wait")

print(f"{dispenser_liters} liters left")