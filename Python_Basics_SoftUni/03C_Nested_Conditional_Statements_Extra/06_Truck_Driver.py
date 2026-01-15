truck_season = input()
km_per_month = float(input())
km_price = 0
salary = 0

if km_per_month <= 5000:
    if (truck_season == "Spring") or (truck_season == "Autumn"):
        km_price = 0.75
        salary = km_price * (km_per_month * 4)
    elif truck_season == "Summer":
        km_price = 0.90
        salary = km_price * (km_per_month * 4)
    elif truck_season == "Winter":
        km_price = 1.05
        salary = km_price * (km_per_month * 4)
elif 5000 < km_per_month <= 10000:
    if (truck_season == "Spring") or (truck_season == "Autumn"):
        km_price = 0.95
        salary = km_price * (km_per_month * 4)
    elif truck_season == "Summer":
        km_price = 1.10
        salary = km_price * (km_per_month * 4)
    elif truck_season == "Winter":
        km_price = 1.25
        salary = km_price * (km_per_month * 4)
elif 10000 < km_per_month <= 20000:
    if (truck_season == "Spring") or (truck_season == "Autumn") or (truck_season == "Summer") or (truck_season == "Winter"):
        km_price = 1.45
        salary = km_price * (km_per_month * 4)

salary -= salary * 0.10

print(f"{salary:.2f}")