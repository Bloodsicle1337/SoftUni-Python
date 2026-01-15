target_climb = ""
number_of_groups = int(input())
total_number_of_hikers = 0
group_m = 0
group_b = 0
group_k = 0
group_k2 = 0
group_e = 0
for _ in range(number_of_groups):
    number_of_hikers = int(input())
    total_number_of_hikers += number_of_hikers
    if number_of_hikers <= 5:
        target_climb = "Musala"
        group_m += number_of_hikers
    elif 5 < number_of_hikers <= 12:
        taget_climb = "Mont Blan"
        group_b += number_of_hikers
    elif 12 < number_of_hikers <= 25:
        taget_climb = "Kilimanjaro"
        group_k += number_of_hikers
    elif 25 < number_of_hikers <= 40:
        taget_climb = "K2"
        group_k2 += number_of_hikers
    elif number_of_hikers > 40:
        taget_climb = "Everest"
        group_e += number_of_hikers

p1 = group_m / total_number_of_hikers * 100
p2 = group_b / total_number_of_hikers * 100
p3 = group_k / total_number_of_hikers * 100
p4 = group_k2 / total_number_of_hikers * 100
p5 = group_e / total_number_of_hikers * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")