budget = float(input())
season = input()
type_of_vacation = ""
destination = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_vacation = "Camp"
        money_spent = budget * 0.30
    elif season == "winter":
        type_of_vacation = "Hotel"
        money_spent = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_vacation = "Camp"
        money_spent = budget * 0.40
    elif season == "winter":
        type_of_vacation = "Hotel"
        money_spent = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    type_of_vacation = "Hotel"
    money_spent = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {money_spent:.2f}")