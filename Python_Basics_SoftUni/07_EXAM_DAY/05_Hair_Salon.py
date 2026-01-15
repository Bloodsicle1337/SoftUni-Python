HAIRCUT_MENS = 15
HAIRCUT_LADIES = 20
HAIRCUT_KIDS = 10

COLOR_TOUCH_UP = 20
COLOR_FULL_COLOR = 30

target_sum = input()
gathered_sum = 0
has_reached = False

while True:
    if target_sum == "closed":
        break

    target_sum = int(target_sum)
    command = input()

    if command == "closed":
        break

    if command == "haircut":
        type_of_command = input()

        if type_of_command == "mens":
            gathered_sum += HAIRCUT_MENS

        elif type_of_command == "ladies":
            gathered_sum += HAIRCUT_LADIES

        elif type_of_command == "kids":
            gathered_sum += HAIRCUT_KIDS

    elif command == "color":
        type_of_command = input()

        if type_of_command == "touch up":
            gathered_sum += COLOR_TOUCH_UP

        elif type_of_command == "full color":
            gathered_sum += COLOR_FULL_COLOR

    if gathered_sum >= target_sum:
        has_reached = True
        break

if has_reached:
    print(f"You have reached your target for the day!")
    print(f"Earned money: {gathered_sum}lv.")

else:
    print(f"Target not reached! You need {target_sum - gathered_sum}lv. more.")
    print(f"Earned money: {gathered_sum}lv.")
