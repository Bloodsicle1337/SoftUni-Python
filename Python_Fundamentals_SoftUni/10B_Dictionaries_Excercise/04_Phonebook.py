phonebook = {}

while True:
    entry = input()

    if "-" not in entry:
        break

    name, number = entry.split("-")
    phonebook[name] = number

number_of_search_times = int(entry)

for search in range(number_of_search_times):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")

    else:
        print(f"Contact {searched_name} does not exist.")


