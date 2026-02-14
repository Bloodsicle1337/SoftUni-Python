def is_valid_index(index, ship):
    return 0 <= index < len(ship)


def fire(war_ship, index, damage):
    if not is_valid_index(index, war_ship):
        return False

    war_ship[index] -= damage
    if war_ship[index] <= 0:
        print("You won! The enemy ship has sunken.")
        return True
    return False


def defend(pirate_ship, start_index, end_index, damage):
    if not (is_valid_index(start_index, pirate_ship) and
            is_valid_index(end_index, pirate_ship)):
        return False

    for i in range(start_index, end_index + 1):
        pirate_ship[i] -= damage
        if pirate_ship[i] <= 0:
            print("You lost! The pirate ship has sunken.")
            return True
    return False


def repair(pirate_ship, index, health, max_health):
    if not is_valid_index(index, pirate_ship):
        return

    pirate_ship[index] += health
    if pirate_ship[index] > max_health:
        pirate_ship[index] = max_health


def status(pirate_ship, max_health):
    threshold = max_health * 0.2
    count = sum(1 for section in pirate_ship if section < threshold)
    print(f"{count} sections need repair.")


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
        battle_over = fire(war_ship, index, damage)

    elif action == "Defend":
        start = int(parts[1])
        end = int(parts[2])
        damage = int(parts[3])
        battle_over = defend(pirate_ship, start, end, damage)

    elif action == "Repair":
        index = int(parts[1])
        health = int(parts[2])
        repair(pirate_ship, index, health, maximum_health_capacity)

    elif action == "Status":
        status(pirate_ship, maximum_health_capacity)

    if battle_over:
        break


if not battle_over:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
