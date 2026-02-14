initial_treasure_chest = input().split("|")

while True:
    command = input()

    if command == "Yohoho!":
        break

    if "Loot" in command:
        parts = command.split()
        items = parts[1:]

        for item in items:
            if item not in initial_treasure_chest:
                initial_treasure_chest.insert(0, item)

    elif "Drop" in command:
        indexer = command.split()
        index_number = int(indexer[1])
        if 0 <= index_number <= len(initial_treasure_chest):
            item_removed = initial_treasure_chest.pop(index_number)
            initial_treasure_chest.append(item_removed)
        else:
            continue

    elif "Steal" in command:
        counter = command.split()
        count = int(counter[1])
        count = min(count, len(initial_treasure_chest))
        stolen_items = initial_treasure_chest[-count:]
        initial_treasure_chest = initial_treasure_chest[:-count]
        print(", ".join(stolen_items))

if len(initial_treasure_chest) == 0:
    print("Failed treasure hunt.")

else:
    average_gain = sum([len(loot) for loot in initial_treasure_chest]) / len(initial_treasure_chest)
    print(f"Average treasure gain: {average_gain:.02f} pirate credits.")