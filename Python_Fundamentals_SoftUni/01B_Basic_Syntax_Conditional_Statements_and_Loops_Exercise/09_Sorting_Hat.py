while True:
    name = input()
    result = ""
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(name) < 5:
        result = f"{name} goes to Gryffindor."

    elif len(name) == 5:
        result = f"{name} goes to Slytherin."

    elif len(name) == 6:
        result = f"{name} goes to Ravenclaw."

    elif len(name) > 6:
        result = f"{name} goes to Hufflepuff."

    print(result)