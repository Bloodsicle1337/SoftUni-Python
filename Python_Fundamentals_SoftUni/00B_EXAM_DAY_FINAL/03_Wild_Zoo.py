animals = {}
areas = {}

command = input()

while command != "EndDay":
    action, info = command.split(": ")
    parts = info.split("-")

    if action == "Add":
        animal, food, area = parts[0], int(parts[1]), parts[2]

        if animal not in animals:
            animals[animal] = {"food": food, "area": area}

            if area not in areas:
                areas[area] = 0
            areas[area] += 1
        else:
            animals[animal]["food"] += food

    elif action == "Feed":
        animal, food = parts[0], int(parts[1])

        if animal in animals:
            animals[animal]["food"] -= food

            if animals[animal]["food"] <= 0:
                area = animals[animal]["area"]
                del animals[animal]
                areas[area] -= 1
                print(f"{animal} was successfully fed")

    command = input()

print("Animals:")
for animal, data in animals.items():
    print(f"{animal} -> {data['food']}g")

print("Areas with hungry animals:")
for area, count in areas.items():
    if count > 0:
        print(f"{area}: {count}")