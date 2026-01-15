number_of_tournaments = int(input())
starting_points = int(input())
wins_at_tournaments = 0
average_points = 0
for _ in range(number_of_tournaments):
    tournament_stage_reached = input()

    if tournament_stage_reached == "W":
        starting_points += 2000
        wins_at_tournaments += 1
        average_points += 2000
    elif tournament_stage_reached == "F":
        starting_points += 1200
        average_points += 1200
    elif tournament_stage_reached == "SF":
        starting_points += 720
        average_points += 720

print(f"Final points: {starting_points}")
print(f"Average points: {(average_points // number_of_tournaments)}")
print(f"{(wins_at_tournaments / number_of_tournaments * 100):.2f}%")
