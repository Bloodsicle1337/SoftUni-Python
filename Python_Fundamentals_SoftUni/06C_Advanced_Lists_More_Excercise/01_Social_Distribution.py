population_as_string = input().split(", ")
minimum_wealth = int(input())

population = []

for person in population_as_string:
    population.append(int(person))

for index in range(len(population)):
    if population[index] < minimum_wealth:
        needed_wealth = minimum_wealth - population[index]

        richest_person = max(population)
        richest_index = population.index(richest_person)

        population[richest_index] -= needed_wealth
        population[index] += needed_wealth

if min(population) >= minimum_wealth:
    print(population)
else:
    print("No equal distribution possible")