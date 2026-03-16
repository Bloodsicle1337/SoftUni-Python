products_quantity = {}
products_price = {}

while True:
    product_inputs = input().split()

    if len(product_inputs) == 1:
        break

    if product_inputs[0] not in products_quantity.keys():
        products_quantity[product_inputs[0]] = 0

    if product_inputs[0] not in products_price.keys():
        products_price[product_inputs[0]] = 0

    products_quantity[product_inputs[0]] += int(product_inputs[2])

    if products_price[product_inputs[0]] != float(product_inputs[1]):
        products_price[product_inputs[0]] = float(product_inputs[1])

for product, quantity in products_quantity.items():
    print(f"{product} -> {quantity * products_price[product]:.02f}")