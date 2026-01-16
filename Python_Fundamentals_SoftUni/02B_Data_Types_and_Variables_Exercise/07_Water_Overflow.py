number_of_inputs = int(input())
tank_capacity = 255

for number in range(number_of_inputs):
    liters_of_water = int(input())

    if liters_of_water > tank_capacity:
        print("Insufficient capacity!")

    else:
        tank_capacity -= liters_of_water

print(255 - tank_capacity)