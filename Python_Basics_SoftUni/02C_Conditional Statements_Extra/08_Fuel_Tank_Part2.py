fuel_type = input()
liters = float(input())
own_card = input()

price_per_liter = 0
if fuel_type == "Gasoline":
    price_per_liter += 2.22
elif fuel_type == "Diesel":
    price_per_liter += 2.33
elif fuel_type == "Gas":
    price_per_liter += 0.93

if own_card == "Yes":
    if fuel_type == "Gasoline":
        price_per_liter -= 0.18
    elif fuel_type == "Diesel":
        price_per_liter -= 0.12
    elif fuel_type == "Gas":
        price_per_liter -= 0.08

total_price = liters * price_per_liter
if 20 <= liters <= 25:
    total_price *= 0.92
elif liters > 25:
    total_price *= 0.90

print(f"{total_price:.2f} lv.")
