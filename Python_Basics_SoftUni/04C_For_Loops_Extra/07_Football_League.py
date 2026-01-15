stadium_capacity = int(input())
total_number_of_fans = int(input())

team_1 = 0
team_2 = 0
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0


for _ in range(total_number_of_fans):
    fan_sector = input()

    if fan_sector == "A":
        team_1 += 1
        sector_a += 1
    elif fan_sector == "B":
        team_1 += 1
        sector_b += 1
    elif fan_sector == "V":
        team_2 += 1
        sector_v += 1
    elif fan_sector == "G":
        team_2 += 1
        sector_g += 1

a_sector_percentage = sector_a / total_number_of_fans * 100
b_sector_percentage = sector_b / total_number_of_fans * 100
v_sector_percentage = sector_v / total_number_of_fans * 100
g_sector_percentage = sector_g / total_number_of_fans * 100

capacity_percentage = total_number_of_fans / stadium_capacity * 100

print(f"{a_sector_percentage:.2f}%")
print(f"{b_sector_percentage:.2f}%")
print(f"{v_sector_percentage:.2f}%")
print(f"{g_sector_percentage:.2f}%")
print(f"{capacity_percentage:.2f}%")