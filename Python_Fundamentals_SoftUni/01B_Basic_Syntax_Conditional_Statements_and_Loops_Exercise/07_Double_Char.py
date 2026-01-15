command = input()

while command != "End":

    if command != "SoftUni":
        word = ""

        for char in command:
            word += char * 2

        print(word)

    command = input()

