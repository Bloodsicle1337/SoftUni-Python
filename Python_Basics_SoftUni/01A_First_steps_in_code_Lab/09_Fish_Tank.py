length = int(input())
width = int(input())
height = int(input())
occupied_space_percentage = float(input())

tank_volume = length * width * height
volume_in_liters = tank_volume * 0.001
reduced_volume = occupied_space_percentage / 100

needed_water = volume_in_liters * (1 - reduced_volume)
print(needed_water)
