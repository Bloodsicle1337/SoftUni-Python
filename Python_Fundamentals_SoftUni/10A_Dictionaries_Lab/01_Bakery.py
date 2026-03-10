bakery_products = input().split()
bakery_stock = {}

for index in range(0, len(bakery_products), 2):
    product = bakery_products[index]
    product_value = int(bakery_products[index + 1])

    bakery_stock[product] = product_value

print(bakery_stock)