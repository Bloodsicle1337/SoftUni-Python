dungeon = input().split("|")

health = 100
bitcoins = 0

for room_index in range(1, len(dungeon) + 1):
    room = dungeon[room_index - 1].split()
    command = room[0]
    number = int(room[1])

    if command == "potion":
        healed = min(number, 100 - health)
        health += healed
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        monster = command
        health -= number

        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_index}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
