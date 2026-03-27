notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    command_data = command.split("-")
    importance = int(command_data[0]) - 1
    note = command_data[1]

    notes.pop(importance)
    notes.insert(importance, note)

result = [element for element in notes if element != 0]
print(result)