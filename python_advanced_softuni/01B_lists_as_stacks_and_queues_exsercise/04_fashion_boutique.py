clothes = list(map(int, input().split()))
rack_capacity = int(input())
racks = 0

while clothes:
    used_rack_capacity = rack_capacity
    racks += 1

    while clothes and used_rack_capacity >= clothes[-1]:
        used_rack_capacity -= clothes.pop()

print(racks)

