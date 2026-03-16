languages = {}
exam_points = {}

while True:
    command = input().split("-")

    if len(command) == 1:
        break

    elif len(command) == 3:
        name, language, score = command[0], command[1], command[2]

        if name not in exam_points.keys():
            exam_points[name] = 0

        if exam_points[name] < int(score):
            exam_points[name] = int(score)

        if language not in languages.keys():
            languages[language] = 0

        languages[language] += 1

    elif len(command) == 2:
        if command[0] in exam_points.keys():
            del exam_points[command[0]]

print("Results:")
for name, score in exam_points.items():
    print(f"{name} | {score}")

print("Submissions:")
for lang, submissions in languages.items():
    print(f"{lang} - {submissions}")
