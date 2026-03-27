number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:
    command = input()

    if command == "End":
        break

    command_data = command.split()
    action = command_data[0]

    if action == "add":
        people = int(command_data[1])
        train[-1] += people

    elif action == "insert":
        index = int(command_data[1])
        people = int(command_data[2])
        train[index] += people

    elif action == "leave":
        index = int(command_data[1])
        people = int(command_data[2])
        train[index] -= people

print(train)