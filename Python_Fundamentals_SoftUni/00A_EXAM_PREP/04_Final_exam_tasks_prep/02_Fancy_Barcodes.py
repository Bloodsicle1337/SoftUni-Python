import re

n = int(input())

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for _ in range(n):
    barcode = input()
    match = re.fullmatch(pattern, barcode)

    if not match:
        print("Invalid barcode")
        continue

    valid = match.group(1)
    digits = "".join(ch for ch in valid if ch.isdigit())

    print(f"Product group: {digits if digits else '00'}")