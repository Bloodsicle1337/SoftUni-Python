from collections import deque

mechanical_parts = list(map(int, input().split()))
power_cells = deque(map(int, input().split()))

drones = {
    "Sentinel-X": 100,
    "Viper-MKII": 85,
    "Aegis-7": 75,
    "Striker-R": 65,
    "Titan-Core": 55
}

assembled_drones = []

while mechanical_parts and power_cells and len(assembled_drones) < 5:
    while power_cells and power_cells[0] <= 0:
        power_cells.popleft()

    if not power_cells:
        break

    current_part = mechanical_parts[-1]
    current_cell = power_cells.popleft()
    total_power = current_part + current_cell

    drone_to_build = None

    for drone, required_power in drones.items():
        if required_power == total_power and drone not in assembled_drones:
            drone_to_build = drone
            break

    if drone_to_build:
        mechanical_parts.pop()
        assembled_drones.append(drone_to_build)
        continue

    for drone, required_power in drones.items():
        if required_power < total_power and drone not in assembled_drones:
            drone_to_build = drone
            break

    if drone_to_build:
        mechanical_parts.pop()
        assembled_drones.append(drone_to_build)

        current_cell -= 30

        if current_cell > 0:
            power_cells.append(current_cell)

    else:
        mechanical_parts.pop()

        current_cell -= 1

        if current_cell > 0:
            power_cells.append(current_cell)

if len(assembled_drones) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")

else:
    print("Mission Failed! Some drones were not built.")

if assembled_drones:
    print(f"Assembled Drones: {', '.join(assembled_drones)}")

if mechanical_parts:
    print(f"Mechanical Parts: {', '.join(map(str, reversed(mechanical_parts)))}")

if power_cells:
    print(f"Power Cells: {', '.join(map(str, power_cells))}")