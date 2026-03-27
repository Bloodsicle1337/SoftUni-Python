players = {}

while True:
    command = input()

    if command == "Season end":
        break

    if " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {}

        if position not in players[player]:
            players[player][position] = skill
        else:
            if skill > players[player][position]:
                players[player][position] = skill

    elif " vs " in command:
        first_player, second_player = command.split(" vs ")

        if first_player in players and second_player in players:
            has_common_position = False

            for position in players[first_player]:
                if position in players[second_player]:
                    has_common_position = True
                    break

            if has_common_position:
                first_total_skill = 0
                second_total_skill = 0

                for skill in players[first_player].values():
                    first_total_skill += skill

                for skill in players[second_player].values():
                    second_total_skill += skill

                if first_total_skill > second_total_skill:
                    del players[second_player]
                elif second_total_skill > first_total_skill:
                    del players[first_player]

sorted_players = sorted(
    players.items(),
    key=lambda x: (-sum(x[1].values()), x[0])
)

for player, positions in sorted_players:
    total_skill = 0

    for skill in positions.values():
        total_skill += skill

    print(f"{player}: {total_skill} skill")

    sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))

    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")