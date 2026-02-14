total_without_taxes = 0

while True:
    command = input()

    if command == "special" or command == "regular":
        customer_type = command
        break

    price = float(command)

    if price <= 0:
        print("Invalid price!")
        continue

    total_without_taxes += price

if total_without_taxes == 0:
    print("Invalid order!")
else:
    taxes = total_without_taxes * 0.20
    total_price = total_without_taxes + taxes

    if customer_type == "special":
        total_price *= 0.90

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")