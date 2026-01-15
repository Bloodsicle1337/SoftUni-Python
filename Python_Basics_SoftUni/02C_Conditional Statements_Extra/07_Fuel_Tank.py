type_of_fuel = input().lower()
liters_in_tank = float(input())

if type_of_fuel == "diesel":
    if liters_in_tank >= 25:
        print(f"You have enough {type_of_fuel}.")
    else:
        print(f"Fill your tank with {type_of_fuel}!")
elif type_of_fuel == "gasoline":
    if liters_in_tank >= 25:
        print(f"You have enough {type_of_fuel}.")
    else:
        print(f"Fill your tank with {type_of_fuel}!")
elif type_of_fuel == "gas":
    if liters_in_tank >= 25:
        print(f"You have enough {type_of_fuel}.")
    else:
        print(f"Fill your tank with {type_of_fuel}!")
else:
    print("Invalid fuel!")