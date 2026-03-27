import re

n = int(input())

attacked_planets = []
destroyed_planets = []

pattern = r"@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)"

for _ in range(n):
    encrypted_message = input()

    key = len(re.findall(r"[starSTAR]", encrypted_message))
    decrypted_message = ""

    for ch in encrypted_message:
        decrypted_message += chr(ord(ch) - key)

    match = re.search(pattern, decrypted_message)

    if match:
        planet, population, attack_type, soldiers = match.groups()

        if attack_type == "A":
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

attacked_planets.sort()
destroyed_planets.sort()

print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")