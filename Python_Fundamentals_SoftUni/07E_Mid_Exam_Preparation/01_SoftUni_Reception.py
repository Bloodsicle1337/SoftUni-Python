employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students = int(input())

students_per_hour = employee1 + employee2 + employee3

hours = 0

while students > 0:
    hours += 1

    if hours % 4 == 0:
        continue

    students -= students_per_hour

print(f"Time needed: {hours}h.")