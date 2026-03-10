total_quantity = 0
stocked_products = {}

while True:
    command = input()

    if command == "statistics":
        break

    products = command.split(": ")

    for index in range(0, len(products), 2):
        product = products[index]
        value = int(products[index + 1])

        if product in stocked_products:
            stocked_products[product] += value
            total_quantity += value
        else:
            stocked_products[product] = value
            total_quantity += value

print("Products in stock:")
for displayed, values in stocked_products.items():
    print(f"- {displayed}: {values}")
print(f"Total Products: {len(stocked_products.keys())}")
print(f"Total Quantity: {total_quantity}")