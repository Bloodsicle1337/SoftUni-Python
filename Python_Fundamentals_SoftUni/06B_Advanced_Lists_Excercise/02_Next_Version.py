version = input().split(".")

first_num = int(version[0])
second_num = int(version[1])
third_num = int(version[2])

third_num += 1

if third_num > 9:
    third_num = 0
    second_num += 1

if second_num > 9:
    second_num = 0
    first_num += 1

print(f"{first_num}.{second_num}.{third_num}")