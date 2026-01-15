number = float(input())
special_number = ""

if number == 0:
    special_number = "zero"

elif number > 0:
    if number < 1:
        special_number = "small positive"
    elif number > 1_000_000:
        special_number = "large positive"

    else:
        special_number = "positive"

else:
    if abs(number) < 1:
        special_number = "small negative"

    elif abs(number) > 1_000_000:
        special_number = "large negative"

    else:
        special_number = "negative"

print(special_number)