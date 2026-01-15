text = input()
vow_sum = 0

for char in text:
    if char == "a":
        vow_sum += 1
    elif char == "e":
        vow_sum += 2
    elif char == "i":
        vow_sum += 3
    elif char == "o":
        vow_sum += 4
    elif char == "u":
        vow_sum += 5

print(vow_sum)