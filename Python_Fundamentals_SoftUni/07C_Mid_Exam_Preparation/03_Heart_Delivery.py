neighborhood = list(map(int, input().split("@")))

position = 0

while True:
    command = input()

    if command == "Love!":
        break

    parts = command.split()
    jump = int(parts[1])

    position += jump
    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

print(f"Cupid's last position was {position}.")

failed = 0
for house in neighborhood:
    if house != 0:
        failed += 1

if failed == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")