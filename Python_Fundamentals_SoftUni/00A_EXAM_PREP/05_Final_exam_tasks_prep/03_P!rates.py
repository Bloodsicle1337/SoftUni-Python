cities = {}

line = input()

while line != "Sail":
    town, population, gold = line.split("||")

    if town not in cities:
        cities[town] = {"people": int(population), "gold": int(gold)}
    else:
        cities[town]["people"] += int(population)
        cities[town]["gold"] += int(gold)

    line = input()

command = input()

while command != "End":
    parts = command.split("=>")
    action = parts[0]

    if action == "Plunder":
        town, people, gold = parts[1], int(parts[2]), int(parts[3])

        cities[town]["people"] -= people
        cities[town]["gold"] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[town]["people"] <= 0 or cities[town]["gold"] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        town, gold = parts[1], int(parts[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

    command = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

    for town, data in cities.items():
        print(f"{town} -> Population: {data['people']} citizens, Gold: {data['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")