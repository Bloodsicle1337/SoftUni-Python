number_of_allowed_tries = int(input())
is_enough = False

number_of_bad_grades = 0
score_sum = 0
number_of_tasks = 0
last_task = ""

while number_of_allowed_tries > number_of_bad_grades:
    name_of_task = input()

    if name_of_task == "Enough":
        is_enough = True
        break

    grade_of_task = int(input())

    if grade_of_task <= 4:
        number_of_bad_grades += 1


    last_task = name_of_task
    number_of_tasks += 1
    grade_of_task = int(grade_of_task)
    score_sum += grade_of_task

if is_enough:
    average_score = score_sum / number_of_tasks
    print(f"Average score: {average_score:.2f}\nNumber of problems: {number_of_tasks}\nLast problem: {last_task}")

else:
    print(f"You need a break, {number_of_bad_grades} poor grades.")