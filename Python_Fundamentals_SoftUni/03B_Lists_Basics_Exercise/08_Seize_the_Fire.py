fire_cells = input().split("#")
total_water = int(input())
total_fire = 0
effort = 0
print("Cells:")
for cell in fire_cells:
    cells_splited = cell.split(" = ")
    fire_type, fire_value = cells_splited[0], int(cells_splited[1])
    if fire_type == "High":
        if 81 <= fire_value <= 125:
            if total_water >= fire_value:
                total_water -= fire_value
                effort += fire_value * 0.25
                total_fire += fire_value
                print(f"- {fire_value}")
            else:
                continue

        else:
            continue

    elif fire_type == "Medium":
        if 51 <= fire_value <= 80:
            if total_water >= fire_value:
                total_water -= fire_value
                effort += fire_value * 0.25
                total_fire += fire_value
                print(f"- {fire_value}")
            else:
                continue

        else:
            continue

    elif fire_type == "Low":
        if 1 <= fire_value <= 50:
            if total_water >= fire_value:
                total_water -= fire_value
                effort += fire_value * 0.25
                total_fire += fire_value
                print(f"- {fire_value}")
            else:
                continue

        else:
            continue

print(f"Effort: {effort:.02f}")
print(f"Total Fire: {total_fire}")