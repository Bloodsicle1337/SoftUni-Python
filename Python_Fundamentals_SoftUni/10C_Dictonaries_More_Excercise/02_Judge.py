contests = {}
users = {}

while True:
    command = input()

    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest]:
        contests[contest][username] = points
    else:
        if points > contests[contest][username]:
            contests[contest][username] = points

for contest in contests:
    for username in contests[contest]:
        if username not in users:
            users[username] = 0

        users[username] += contests[contest][username]

print_result_order = list(contests.keys())

for contest in print_result_order:
    print(f"{contest}: {len(contests[contest])} participants")

    sorted_users = sorted(contests[contest].items(), key=lambda x: (-x[1], x[0]))

    place = 1
    for username, points in sorted_users:
        print(f"{place}. {username} <::> {points}")
        place += 1

print("Individual standings:")

sorted_users = sorted(users.items(), key=lambda x: (-x[1], x[0]))

place = 1
for username, points in sorted_users:
    print(f"{place}. {username} -> {points}")
    place += 1