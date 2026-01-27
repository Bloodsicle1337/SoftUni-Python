no_money = False
gifts = input().split()

while not no_money:
    command = input()
    if command == "No Money":
        no_money = True

    command_list = command.split()

    command_type, gift_type = command_list[0], command_list[1]

    if command_type == "OutOfStock":
        for gift in range(len(gifts)):
            if gifts[gift] == gift_type:
                gifts[gift] = "None"

    elif command_type == "Required":
        index = int(command_list[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_type

    elif command_type == "JustInCase":
        gifts[-1] = gift_type

for gift_item in gifts:
    if gift_item != "None":
        print(gift_item, end=" ")