number_of_rows = int(input())
student_grades = {}
grades_list = []
for rows in range(number_of_rows):
    name = input()
    grade = float(input())

    if name not in student_grades.keys():
        student_grades[name] = []
    student_grades[name].append(grade)

for name, grades in student_grades.items():
    average_score = sum(grades) / len(grades)

    if average_score >= 4.50:
        print(f"{name} -> {average_score:.02f}")