first_match_score = input()
second_match_score = input()
third_match_score = input()

wins = 0
loses = 0
draws = 0

first_part = first_match_score.split(":")
second_part = second_match_score.split(":")
third_part = third_match_score.split(":")

m1_team_1 = int(first_part[0])
m1_team_2 = int(first_part[1])

m2_team_1 = int(second_part[0])
m2_team_2 = int(second_part[1])

m3_team_1 = int(third_part[0])
m3_team_2 = int(third_part[1])

if m1_team_1 > m1_team_2:
    wins += 1
elif m1_team_1 == m1_team_2:
    draws += 1
elif m1_team_1 < m1_team_2:
    loses += 1

if m2_team_1 > m2_team_2:
    wins += 1
elif m2_team_1 == m2_team_2:
    draws += 1
elif m2_team_1 < m2_team_2:
    loses += 1

if m3_team_1 > m3_team_2:
    wins += 1
elif m3_team_1 == m3_team_2:
    draws += 1
elif m3_team_1 < m3_team_2:
    loses += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")
