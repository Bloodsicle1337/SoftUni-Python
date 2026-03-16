number_of_commands = int(input())
parking_spaces = {}

for number in range(number_of_commands):
    register_validation = input().split()

    if len(register_validation) == 3:
        if register_validation[1] not in parking_spaces.keys():
            parking_spaces[register_validation[1]] = register_validation[2]
            print(f"{register_validation[1]} registered {register_validation[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_spaces[register_validation[1]]}")


    elif len(register_validation) == 2:
        if register_validation[1] not in parking_spaces.keys():
            print(f"ERROR: user {register_validation[1]} not found")

        else:
            del parking_spaces[register_validation[1]]
            print(f"{register_validation[1]} unregistered successfully")

for username, license_plate_number in parking_spaces.items():
    print(f"{username} => {license_plate_number}")