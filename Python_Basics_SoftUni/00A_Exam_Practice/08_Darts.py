STARTING_SCORE = 301


successful_count = 0
unsuccessful_count = 0
current_score = 0
scored_points = 0
name = input()

while True:
    throw_multiplier = input()

    if throw_multiplier == "Retire":
        print(f"{name} retired after {unsuccessful_count} unsuccessful shots.")
        break

    points = input()
    if points == "Retire":
        print(f"{name} retired after {unsuccessful_count} unsuccessful shots.")
        break

    points = int(points)

    if throw_multiplier == "Single":
        scored_points = points
    elif throw_multiplier == "Double":
        scored_points = points * 2
    elif throw_multiplier == "Triple":
        scored_points = points * 3

    if current_score + scored_points > STARTING_SCORE:
        unsuccessful_count += 1
        continue
    else:
        current_score += scored_points
        successful_count += 1

        if current_score == STARTING_SCORE:
            print(f"{name} won the leg with {successful_count} shots.")
            break
