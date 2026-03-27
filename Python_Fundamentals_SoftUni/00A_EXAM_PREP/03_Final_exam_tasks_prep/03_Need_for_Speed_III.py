n = int(input())

cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()

while command != "Stop":
    parts = command.split(" : ")
    action = parts[0]

    if action == "Drive":
        car, distance, fuel = parts[1], int(parts[2]), int(parts[3])

        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car]["mileage"] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")

    elif action == "Refuel":
        car, fuel = parts[1], int(parts[2])

        current_fuel = cars[car]["fuel"]
        added = min(75 - current_fuel, fuel)
        cars[car]["fuel"] += added

        print(f"{car} refueled with {added} liters")

    elif action == "Revert":
        car, kilometers = parts[1], int(parts[2])

        cars[car]["mileage"] -= kilometers

        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car, data in cars.items():
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")