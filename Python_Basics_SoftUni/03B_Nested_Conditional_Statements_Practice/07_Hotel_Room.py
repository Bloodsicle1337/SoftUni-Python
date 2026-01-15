STUDIO_MAY_OCTOBER_PRICE = 50
STUDIO_JUNE_SEPTEMBER_PRICE = 75.20
STUDIO_JULY_AUGUST_PRICE = 76

APARTMENT_MAY_OCTOBER_PRICE = 65
APARTMENT_JUNE_SEPTEMBER_PRICE = 68.70
APARTMENT_JULY_AUGUST_PRICE = 77

month = input()
nights = int(input())

apartment_price = 0
studio_price = 0

if (month == "May") or (month == "October"):
    apartment_price = nights * APARTMENT_MAY_OCTOBER_PRICE
    studio_price = nights * STUDIO_MAY_OCTOBER_PRICE
    if nights > 14:
        studio_price -= studio_price * 0.30
    elif nights > 7:
        studio_price -= studio_price * 0.05
elif (month == "June") or (month == "September"):
    apartment_price = nights * APARTMENT_JUNE_SEPTEMBER_PRICE
    studio_price = nights * STUDIO_JUNE_SEPTEMBER_PRICE
    if nights > 14:
        studio_price -= studio_price * 0.20
elif (month == "July") or (month == "August"):
    apartment_price = nights * APARTMENT_JULY_AUGUST_PRICE
    studio_price = nights * STUDIO_JULY_AUGUST_PRICE

if nights > 14:
    apartment_price -= apartment_price * 0.10

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")