import re

text = input()

pattern = r"([|#])([A-Za-z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d{1,5})\1"
matches = re.findall(pattern, text)

total_calories = 0
foods = []

for match in matches:
    item_name = match[1]
    expiration_date = match[2]
    calories = int(match[3])

    total_calories += calories
    foods.append((item_name, expiration_date, calories))

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for food in foods:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")