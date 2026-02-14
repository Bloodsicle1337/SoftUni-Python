pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
maximum_health_capacity = int(input())

battle_over = False

while True:
    command = input()

    if command == "Retire":
        break

    parts = command.split()
    action = parts[0]

    if action == "Fire":
        index = int(parts[1])
        damage = int(parts[2])

        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                battle_over = True
                break

    elif action == "Defend":
        start_index = int(parts[1])
        end_index = int(parts[2])
        damage = int(parts[3])

        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    battle_over = True
                    break
            if battle_over:
                break

    elif action == "Repair":
        index = int(parts[1])
        health = int(parts[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > maximum_health_capacity:
                pirate_ship[index] = maximum_health_capacity

    elif action == "Status":
        threshold = maximum_health_capacity * 0.2
        count = 0
        for section in pirate_ship:
            if section < threshold:
                count += 1
        print(f"{count} sections need repair.")

if not battle_over:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
