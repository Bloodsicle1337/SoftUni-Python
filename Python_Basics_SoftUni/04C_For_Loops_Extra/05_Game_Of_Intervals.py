number_of_rounds = int(input())
final_score = 0
first_x = 0
second_x = 0
third_x = 0
fourth_x = 0
fifth_x = 0
invalid_x = 0


for _ in range(number_of_rounds):
    number = int(input())

    if 0 <= number <= 9:
        final_score += number * 0.20
        first_x += 1
    elif 10 <= number <= 19:
        final_score += number * 0.30
        second_x += 1
    elif 20 <= number <= 29:
        final_score += number * 0.40
        third_x += 1
    elif 30 <= number <= 39:
        final_score += 50
        fourth_x += 1
    elif 40 <= number <= 50:
        final_score += 100
        fifth_x += 1
    else:
        final_score /= 2
        invalid_x += 1

p1 = first_x / number_of_rounds * 100
p2 = second_x / number_of_rounds * 100
p3 = third_x / number_of_rounds * 100
p4 = fourth_x / number_of_rounds * 100
p5 = fifth_x / number_of_rounds * 100
p6 = invalid_x / number_of_rounds * 100

print(f"{final_score:.2f}")
print(f"From 0 to 9: {p1:.2f}%")
print(f"From 10 to 19: {p2:.2f}%")
print(f"From 20 to 29: {p3:.2f}%")
print(f"From 30 to 39: {p4:.2f}%")
print(f"From 40 to 50: {p5:.2f}%")
print(f"Invalid numbers: {p6:.2f}%")
