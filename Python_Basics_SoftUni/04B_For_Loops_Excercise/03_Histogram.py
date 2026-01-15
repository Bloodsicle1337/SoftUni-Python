p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
num = int(input())
for x in range(num):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    elif number >= 800:
        p5 += 1
percentage1 = p1 / num * 100
percentage2 = p2 / num * 100
percentage3 = p3 / num * 100
percentage4 = p4 / num * 100
percentage5 = p5 / num * 100

print(f"{percentage1:.2f}%\n{percentage2:.2f}%\n{percentage3:.2f}%\n{percentage4:.2f}%\n{percentage5:.2f}%")