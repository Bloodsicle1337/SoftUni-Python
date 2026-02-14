from math import ceil

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus = 0
best_attendance = 0

if students_count == 0 or lectures_count == 0:
    print(f"Max Bonus: {max_bonus}.")
    print(f"The student has attended {best_attendance} lectures.")
else:
    for _ in range(students_count):
        attendance = int(input())
        total_bonus = attendance / lectures_count * (5 + additional_bonus)

        if total_bonus > max_bonus:
            max_bonus = total_bonus
            best_attendance = attendance

    print(f"Max Bonus: {ceil(max_bonus)}.")
    print(f"The student has attended {best_attendance} lectures.")
