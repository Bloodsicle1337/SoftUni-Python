items_in_each_city_cell = list(map(int, input().split("|")))
number_of_items_gathered = 0

while True:
    command = input()

    if command == "Adventure over":
        break

    if "Step" in command:
        parts = command.split("$")
        action = parts[0]
        index = int(parts[1])
        steps = int(parts[2])

        if 0 <= index < len(items_in_each_city_cell):

            if action == "Step Backward":
                new_index = (index - steps) % len(items_in_each_city_cell)

            elif action == "Step Forward":
                new_index = (index + steps) % len(items_in_each_city_cell)

            number_of_items_gathered += items_in_each_city_cell[new_index]
            items_in_each_city_cell[new_index] = 0


    elif "Double" in command:
        new_command = command.split()
        index_double = int(new_command[1])

        if 0 <= index_double < len(items_in_each_city_cell):
            items_in_each_city_cell[index_double] *= 2

    elif "Switch" in command:
        items_in_each_city_cell.reverse()

print(" - ".join(map(str, items_in_each_city_cell)))
print(f"Robo finished the adventure with {number_of_items_gathered} items!")