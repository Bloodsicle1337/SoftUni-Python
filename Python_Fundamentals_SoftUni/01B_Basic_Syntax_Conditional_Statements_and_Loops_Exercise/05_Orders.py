number_of_orders = int(input())
total_price = 0

for order in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    total_day_price = 0

    if 0.01 <= price_per_capsule <= 100_000 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        total_day_price = (price_per_capsule * capsules_needed_per_day) * days
        print(f"The price for the coffee is: ${total_day_price:.02f}")
        total_price += total_day_price
    else:
        continue

print(f"Total: ${total_price:.02f}")