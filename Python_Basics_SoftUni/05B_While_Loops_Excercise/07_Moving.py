house_width = int(input())
house_length = int(input())
house_height = int(input())

total_house_free_space = house_width * house_length * house_height

cubic_meters = 0

is_free = False

while cubic_meters < total_house_free_space:
    cubic_meters_input = input()

    if cubic_meters_input == "Done":
        is_free = True
        break

    cubic_meters_input = int(cubic_meters_input)
    cubic_meters += cubic_meters_input

if is_free:
    print(f"{total_house_free_space - cubic_meters} Cubic meters left.")

else:
    print(f"No more free space! You need {cubic_meters - total_house_free_space} Cubic meters more.")