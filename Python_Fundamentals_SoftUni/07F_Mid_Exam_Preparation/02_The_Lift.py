people = int(input())
wagons = list(map(int, input().split()))

for i in range(len(wagons)):
    while wagons[i] < 4 and people > 0:
        wagons[i] += 1
        people -= 1

if people == 0 and any(wagon < 4 for wagon in wagons):
    print("The lift has empty spots!")
    print(" ".join(map(str, wagons)))
elif people > 0 and all(wagon == 4 for wagon in wagons):
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(map(str, wagons)))
else:
    print(" ".join(map(str, wagons)))