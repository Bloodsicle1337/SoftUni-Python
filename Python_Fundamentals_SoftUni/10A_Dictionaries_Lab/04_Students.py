students = {}

while True:
    line = input()

    if ":" not in line:
        course_to_find = line.replace("_", " ")
        break

    name, student_id, course = line.split(":")
    students[student_id] = {"name": name, "course": course}

for student_id, data in students.items():
    if data["course"] == course_to_find:
        print(f"{data['name']} - {student_id}")