course_number_of_participants = {}
course_student_names = {}

while True:
    student_inputs = input().split(" : ")

    if len(student_inputs) == 1:
        break

    course = student_inputs[0]
    student = student_inputs[1]

    if course not in course_number_of_participants:
        course_number_of_participants[course] = 0

    course_number_of_participants[course] += 1

    if course not in course_student_names:
        course_student_names[course] = []

    course_student_names[course].append(student)


for course, count in course_number_of_participants.items():
    print(f"{course}: {count}")
    for student in course_student_names[course]:
        print(f"-- {student}")