number_of_dragons = int(input())
dragons = {}

for _ in range(number_of_dragons):
    dragon_type, name, damage, health, armor = input().split()

    if damage == "null":
        damage = 45
    else:
        damage = int(damage)

    if health == "null":
        health = 250
    else:
        health = int(health)

    if armor == "null":
        armor = 10
    else:
        armor = int(armor)

    if dragon_type not in dragons:
        dragons[dragon_type] = {}

    dragons[dragon_type][name] = {
        "damage": damage,
        "health": health,
        "armor": armor
    }

for dragon_type in dragons:
    total_damage = 0
    total_health = 0
    total_armor = 0
    count = 0

    for name in dragons[dragon_type]:
        total_damage += dragons[dragon_type][name]["damage"]
        total_health += dragons[dragon_type][name]["health"]
        total_armor += dragons[dragon_type][name]["armor"]
        count += 1

    average_damage = total_damage / count
    average_health = total_health / count
    average_armor = total_armor / count

    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    sorted_dragons = sorted(dragons[dragon_type].items())

    for name, stats in sorted_dragons:
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")