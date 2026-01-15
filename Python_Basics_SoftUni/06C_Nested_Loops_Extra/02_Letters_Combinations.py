first_in_range_letter = input()
last_in_range_letter = input()
skipped_letter = input()
combinations = 0
result = ""

for first in range(ord(first_in_range_letter), ord(last_in_range_letter) + 1):
    for second in range(ord(first_in_range_letter), ord(last_in_range_letter) + 1):
        for third in range(ord(first_in_range_letter), ord(last_in_range_letter) + 1):
            combine = chr(first) + chr(second) + chr(third)

            if skipped_letter in combine:
                continue

            result += combine + " "
            combinations += 1

print(f"{result}{combinations}")