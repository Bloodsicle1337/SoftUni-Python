string_of_animals = input()
list_of_animals = string_of_animals.split(", ")
wolf_index = list_of_animals.index("wolf")

if wolf_index == len(list_of_animals) - 1:
    print("Please go away and stop eating my sheep")

else:
    sheep_number = len(list_of_animals) - wolf_index - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
