animal = input()
type_of_animal = ""

if animal == "dog":
    type_of_animal = "mammal"
elif (animal == "crocodile") or (animal == "tortoise") or (animal == "snake"):
    type_of_animal = "reptile"
else:
    type_of_animal = "unknown"
print(type_of_animal)