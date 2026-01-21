animal_megazord = []

for _ in range(3):
    animal_part = input()
    animal_megazord.append(animal_part)

animal_megazord[0], animal_megazord[2] = animal_megazord[2], animal_megazord[0]
print(animal_megazord)
