student_name = input()
grade = 1
average_grade = 0
max_tries = 0

while True:
    score = float(input())

    if score < 4.00:
        max_tries += 1
        if max_tries == 2:
            print(f"{student_name} has been excluded at {grade} grade")
            break
        continue

    average_grade += score
    grade += 1

    if grade > 12:
        average_grade /= 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break
