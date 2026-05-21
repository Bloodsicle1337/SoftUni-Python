from collections import deque

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    fuel, distance = [int(x) for x in input().split()]
    pumps.append({"fuel": fuel, "distance": distance})

start_idx = 0
stops = 0

while stops < pumps_num:
    current_fuel = 0
    for i in range(pumps_num):
        current_fuel += pumps[i]["fuel"]
        current_dist = pumps[i]["distance"]
        if current_fuel < current_dist:
            stops = 0
            start_idx += 1
            pumps.rotate(-1)
            break

        current_fuel -= current_dist
        stops += 1

print(start_idx)