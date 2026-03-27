import re

bought_furniture = []
total_cost = 0
pattern = r">>([a-z]+)<<(\d+\.?\d*)!(\d+)"

line = input()

while line != "Purchase":
    matches = re.search(pattern, line, re.IGNORECASE)
    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)

    line = input()

print("Bought furniture:")
for furni in bought_furniture:
    print(furni)
print(f"Total money spend: {total_cost:.2f}")