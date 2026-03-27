import re

total_income = 0
pattern = r"%([A-Z][a-z]+)%[^|$%\.]*<([^<>]+)>[^|$%\.]*\|(\d+)\|[^|$%\.]*?(\d+\.?\d*)\$"

line = input()

while line != "end of shift":
    matches = re.search(pattern, line)

    if matches:
        customer, product, count, price = matches.groups()
        current_total = int(count) * float(price)
        total_income += current_total
        print(f"{customer}: {product} - {current_total:.2f}")

    line = input()

print(f"Total income: {total_income:.2f}")