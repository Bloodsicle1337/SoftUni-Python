text = input()
result = ""
explosion_power = 0

for index in range(len(text)):
    if explosion_power > 0 and text[index] != ">":
        explosion_power -= 1

    elif text[index] == ">":
        result += ">"
        explosion_power += int(text[index + 1])

    else:
        result += text[index]

print(result)
