materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary = ""
won_legendary = False
while not won_legendary:
    current_materials = input().split()

    for index in range(0,len(current_materials), 2):
        key = current_materials[index + 1].lower()
        value = int(current_materials[index])

        if key not in materials.keys():
            materials[key] = 0

        materials[key] += value

        if materials["shards"] >= 250:
            legendary = "Shadowmourne"
            materials["shards"] -= 250
            won_legendary = True

        elif materials["fragments"] >= 250:
            legendary = "Valanyr"
            materials["fragments"] -= 250
            won_legendary = True

        elif materials["motes"] >= 250:
            legendary = "Dragonwrath"
            materials["motes"] -= 250
            won_legendary = True

        if won_legendary:
            break

print(f"{legendary} obtained!")
for key, value in materials.items():
    print(f"{key}: {value}")