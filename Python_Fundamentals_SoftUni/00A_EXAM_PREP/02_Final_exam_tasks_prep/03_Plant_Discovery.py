n = int(input())

plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": int(rarity), "ratings": []}

command = input()

while command != "Exhibition":
    parts = command.split(": ")
    action = parts[0]

    if action == "Rate":
        plant, rating = parts[1].split(" - ")

        if plant in plants:
            plants[plant]["ratings"].append(int(rating))
        else:
            print("error")

    elif action == "Update":
        plant, new_rarity = parts[1].split(" - ")

        if plant in plants:
            plants[plant]["rarity"] = int(new_rarity)
        else:
            print("error")

    elif action == "Reset":
        plant = parts[1]

        if plant in plants:
            plants[plant]["ratings"] = []
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")

for plant, data in plants.items():
    ratings = data["ratings"]
    avg = sum(ratings) / len(ratings) if ratings else 0
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {avg:.2f}")