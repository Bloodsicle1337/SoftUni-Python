def final_bill_price(product, quantity):
    final_bill = 0
    if product == "coffee":
        final_bill += 1.50 * quantity

    elif product == "water":
        final_bill += 1.00 * quantity

    elif product == "coke":
        final_bill += 1.40 * quantity

    elif product == "snacks":
        final_bill += 2.00 * quantity

    return final_bill

item_from_menu = input()
quantity_of_item = int(input())

print(f"{final_bill_price(item_from_menu, quantity_of_item):.02f}")