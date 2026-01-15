BUS_PRICE_PER_TON = 200
TRUCK_PRICE_PER_TON = 175
TRAIN_PRICE_PER_TON = 120

number_of_trips = int(input())
bus_sum = 0
truck_sum = 0
train_sum = 0
bus_tons = 0
truck_tons = 0
train_tons = 0
for trip in range(number_of_trips):
    tons = int(input())

    if tons <= 3:
        bus_sum += tons * BUS_PRICE_PER_TON
        bus_tons += tons
    elif tons <= 11:
        truck_sum += tons * TRUCK_PRICE_PER_TON
        truck_tons += tons
    elif tons > 11:
        train_sum += tons * TRAIN_PRICE_PER_TON
        train_tons += tons
total_tons = bus_tons + truck_tons + train_tons
average_per_ton = (truck_sum + train_sum + bus_sum) / total_tons

print(f"{average_per_ton:.2f}")
print(f"{((bus_tons / total_tons) * 100):.2f}%")
print(f"{((truck_tons / total_tons) * 100):.2f}%")
print(f"{((train_tons / total_tons) * 100):.2f}%")