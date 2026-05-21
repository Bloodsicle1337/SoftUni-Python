number_of_cars = int(input())
parking = set()

for _ in range(number_of_cars):
    command, car_number = input().split(", ")
    if command == "IN":
        parking.add(car_number)

    elif command == "OUT":
        if car_number not in parking:
            continue

        else:
            parking.remove(car_number)

if parking:
    print("\n".join(parking))

else:
    print("Parking Lot is Empty")