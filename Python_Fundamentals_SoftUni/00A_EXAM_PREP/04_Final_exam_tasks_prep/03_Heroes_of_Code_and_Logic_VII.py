n = int(input())

heroes = {}

for _ in range(n):
    name, hp, mp = input().split()
    heroes[name] = {"hp": int(hp), "mp": int(mp)}

command = input()

while command != "End":
    parts = command.split(" - ")
    action = parts[0]

    if action == "CastSpell":
        name, needed_mp, spell = parts[1], int(parts[2]), parts[3]

        if heroes[name]["mp"] >= needed_mp:
            heroes[name]["mp"] -= needed_mp
            print(f"{name} has successfully cast {spell} and now has {heroes[name]['mp']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif action == "TakeDamage":
        name, damage, attacker = parts[1], int(parts[2]), parts[3]
        heroes[name]["hp"] -= damage

        if heroes[name]["hp"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hp']} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")

    elif action == "Recharge":
        name, amount = parts[1], int(parts[2])

        current = heroes[name]["mp"]
        recovered = min(200 - current, amount)
        heroes[name]["mp"] += recovered

        print(f"{name} recharged for {recovered} MP!")

    elif action == "Heal":
        name, amount = parts[1], int(parts[2])

        current = heroes[name]["hp"]
        recovered = min(100 - current, amount)
        heroes[name]["hp"] += recovered

        print(f"{name} healed for {recovered} HP!")

    command = input()

for name, data in heroes.items():
    print(name)
    print(f"  HP: {data['hp']}")
    print(f"  MP: {data['mp']}")