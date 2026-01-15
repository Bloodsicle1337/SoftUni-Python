actor_name = input()
initial_points = float(input())
appraisers = int(input())
total_points = initial_points

for _ in range(appraisers):
    name_of_appraiser = input()
    points_given_by_appraiser = float(input())
    total_points += (len(name_of_appraiser) * points_given_by_appraiser) / 2

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")