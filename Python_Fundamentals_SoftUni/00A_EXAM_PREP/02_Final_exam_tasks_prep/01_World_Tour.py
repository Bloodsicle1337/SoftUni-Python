stops = input()

command = input()

while command != "Travel":
    parts = command.split(":")
    action = parts[0]

    if action == "Add Stop":
        index, string = int(parts[1]), parts[2]

        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]

    elif action == "Remove Stop":
        start, end = int(parts[1]), int(parts[2])

        if 0 <= start <= end < len(stops):
            stops = stops[:start] + stops[end + 1:]

    elif action == "Switch":
        old, new = parts[1], parts[2]

        if old in stops:
            stops = stops.replace(old, new)

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")