DETERGENT_QUANTITY = 750
VOLUME_PER_DISH = 5
VOLUME_PER_POT = 15

detergent_bottles = int(input())
detergent_volume = detergent_bottles * DETERGENT_QUANTITY

total_volume = 0
cleaned_dishes = 0
cleaned_pots = 0
number_of_input = 0

while total_volume <= detergent_volume:
    dirty_silverware = input()
    number_of_input += 1

    if dirty_silverware == "End":
        break

    dirty_silverware = int(dirty_silverware)

    if number_of_input % 3 == 0:
        cleaned_pots += dirty_silverware
        total_volume += dirty_silverware * VOLUME_PER_POT

    else:
        cleaned_dishes += dirty_silverware
        total_volume += dirty_silverware * VOLUME_PER_DISH


if total_volume <= detergent_volume:
    leftover_detergent = detergent_volume - total_volume
    print(f"Detergent was enough!\n{cleaned_dishes} dishes and {cleaned_pots} pots were washed.\nLeftover detergent {leftover_detergent} ml.")

else:
    deficit = total_volume - detergent_volume
    print(f"Not enough detergent, {deficit} ml. more necessary!")