budget_vacation = float(input())
season = input()

accommodation_type = ""
location = ""
vacation_price = 0
if budget_vacation <= 1000:
    accommodation_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        vacation_price = budget_vacation * 0.65
    elif season == "Winter":
        location = "Morocco"
        vacation_price = budget_vacation * 0.45
elif 1000 < budget_vacation <= 3000:
    accommodation_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        vacation_price = budget_vacation * 0.80
    elif season == "Winter":
        location = "Morocco"
        vacation_price = budget_vacation * 0.60

elif budget_vacation > 3000:
    accommodation_type = "Hotel"
    if season == "Summer":
        location = "Alaska"
        vacation_price = budget_vacation * 0.90
    elif season == "Winter":
        location = "Morocco"
        vacation_price = budget_vacation * 0.90

print(f"{location} - {accommodation_type} - {vacation_price:.2f}")