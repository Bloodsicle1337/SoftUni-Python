reviewers = int(input())

number_of_reviews = 0
sum_of_scores = 0.0
result = ""
is_finished = False
while True:
    presentation_name = input()
    current_score = 0.0

    if presentation_name == "Finish":
        break

    for review in range(reviewers):
        score = input()

        if score == "Finish":
            break

        score = float(score)
        number_of_reviews += 1
        sum_of_scores += score
        current_score += score
    print(f"{presentation_name} - {current_score / reviewers:.2f}.")

print(f"Student's final assessment is {sum_of_scores / number_of_reviews:.2f}.")