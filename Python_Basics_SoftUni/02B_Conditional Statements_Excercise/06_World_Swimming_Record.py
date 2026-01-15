from math import floor

world_record = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

swim_time = distance_in_meters * seconds_per_meter

delay = floor(distance_in_meters / 15) * 12.5

total_time = swim_time + delay

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - world_record:.2f} seconds slower.")