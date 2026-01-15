JUNIORS_TRAIL = 5.50
JUNIORS_CROSS = 8
JUNIORS_DOWN = 12.25
JUNIORS_ROAD = 20

SENIORS_TRAIL = 7
SENIORS_CROSS = 9.50
SENIORS_DOWN = 13.75
SENIORS_ROAD = 21.50

number_of_juniors = int(input())
number_of_seniors = int(input())
type_of_race = input()

total_participants = number_of_juniors + number_of_seniors

total_donation = 0

if type_of_race == "trail":
    total_donation = (number_of_juniors * JUNIORS_TRAIL) + (number_of_seniors * SENIORS_TRAIL)
elif type_of_race == "cross-country":
    total_donation = (number_of_juniors * JUNIORS_CROSS) + (number_of_seniors * SENIORS_CROSS)
    if total_participants >= 50:
        total_donation -= total_donation * 0.25
elif type_of_race == "downhill":
    total_donation = (number_of_juniors * JUNIORS_DOWN) + (number_of_seniors * SENIORS_DOWN)
elif type_of_race == "road":
    total_donation = (number_of_juniors * JUNIORS_ROAD) + (number_of_seniors * SENIORS_ROAD)

final_bill = total_donation - (total_donation * 0.05)

print(f"{final_bill:.2f}")