number_of_snowballs = int(input())
best_score = 0
best_time = 0
best_weight = 0
best_quality = 0


for ball in range(1, number_of_snowballs + 1):
    weight_of_snowball = int(input())
    time_to_make = int(input())
    quality_of_ball = int(input())

    score = (weight_of_snowball // time_to_make) ** quality_of_ball
    if score > best_score:
        best_score = score
        best_weight = weight_of_snowball
        best_time = time_to_make
        best_quality = quality_of_ball

    else:
        continue

print(f"{best_weight} : {best_time} = {best_score} ({best_quality})")