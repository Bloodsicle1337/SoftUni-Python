stock = input().split()
wanted_products = input().split()
stocked_products = {}

for index in range(0, len(stock), 2):
    product = stock[index]
    product_value = int(stock[index + 1])

    stocked_products[product] = product_value

for specific_product in wanted_products:
    if specific_product in stocked_products:
        print(f"We have {int(stocked_products[specific_product])} of {specific_product} left")

    else:
        print(f"Sorry, we don't have {specific_product}")