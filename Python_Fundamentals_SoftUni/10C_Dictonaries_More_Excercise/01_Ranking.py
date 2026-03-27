contests = {}
users = {}

while True:
    command = input()

    if command == "end of contests":
        break

    contest, password = command.split(":")
    contests[contest] = password

while True:
    command = input()

    if command == "end of submissions":
        break

    contest, password, username, points = command.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}

        if contest not in users[username]:
            users[username][contest] = points
        else:
            if points > users[username][contest]:
                users[username][contest] = points

best_user = ""
best_points = 0

for username in users:
    current_points = 0

    for contest in users[username]:
        current_points += users[username][contest]

    if current_points > best_points:
        best_points = current_points
        best_user = username

print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")

for username in sorted(users.keys()):
    print(username)

    sorted_contests = sorted(users[username].items(), key=lambda x: -x[1])

    for contest, points in sorted_contests:
        print(f"#  {contest} -> {points}")