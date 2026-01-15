number_of_students = int(input())
top_students = 0
good_students = 0
average_students = 0
failed_students = 0
average_grade = 0.0

for student in range(number_of_students):
    grade = float(input())

    if grade >= 5.00:
        top_students += 1
        average_grade += grade
    elif 4.00 <= grade <= 4.99:
        good_students += 1
        average_grade += grade
    elif 3.00 <= grade <= 3.99:
        average_students += 1
        average_grade += grade
    elif grade < 3.00:
        failed_students += 1
        average_grade += grade

p1 = top_students / number_of_students * 100
p2 = good_students / number_of_students * 100
p3 = average_students / number_of_students * 100
p4 = failed_students / number_of_students * 100
p5 = average_grade / number_of_students

print(f"Top students: {p1:.2f}%")
print(f"Between 4.00 and 4.99: {p2:.2f}%")
print(f"Between 3.00 and 3.99: {p3:.2f}%")
print(f"Fail: {p4:.2f}%")
print(f"Average: {p5:.2f}")