import re

participants = input().split(", ")
racers = {}

pattern_name = r"[A-Za-z]"
pattern_distance = r"\d"

line = input()

while line != "end of race":
    name = "".join(re.findall(pattern_name, line))
    distance = sum(int(x) for x in re.findall(pattern_distance, line))

    if name in participants:
        if name not in racers:
            racers[name] = 0
        racers[name] += distance

    line = input()

sorted_racers = sorted(racers.items(), key=lambda x: -x[1])

print(f"1st place: {sorted_racers[0][0]}")
print(f"2nd place: {sorted_racers[1][0]}")
print(f"3rd place: {sorted_racers[2][0]}")