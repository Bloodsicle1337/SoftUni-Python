age = float(input())
gender = input()
result = ""

if gender == "m":
    if age >= 16:
        result = "Mr."
    elif age < 16:
        result = "Master"
else:
    if age >= 16:
        result = "Ms."
    elif age < 16:
        result = "Miss"

print(result)