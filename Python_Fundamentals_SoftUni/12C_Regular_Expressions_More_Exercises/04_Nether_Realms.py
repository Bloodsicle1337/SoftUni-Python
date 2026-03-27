import re

demons = input().split(",")
demons = [d.strip() for d in demons]
demons.sort()

for demon in demons:
    health = 0
    damage = 0

    health_pattern = r"[^0-9+\-*/.]"
    damage_pattern = r"[-+]?\d+(?:\.\d+)?"

    health_matches = re.findall(health_pattern, demon)
    for ch in health_matches:
        health += ord(ch)

    damage_matches = re.findall(damage_pattern, demon)
    for num in damage_matches:
        damage += float(num)

    for ch in demon:
        if ch == "*":
            damage *= 2
        elif ch == "/":
            damage /= 2

    print(f"{demon} - {health} health, {damage:.2f} damage")