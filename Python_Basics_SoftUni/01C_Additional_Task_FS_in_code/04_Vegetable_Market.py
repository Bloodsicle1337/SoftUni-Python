veg_price_per_kilo = float(input())
fruit_price_per_kilo = float(input())
kg_vegetable = int(input())
kg_fruits = int(input())

euro_price = (veg_price_per_kilo * kg_vegetable + fruit_price_per_kilo * kg_fruits) / 1.94
print(f"{euro_price:.2f}")