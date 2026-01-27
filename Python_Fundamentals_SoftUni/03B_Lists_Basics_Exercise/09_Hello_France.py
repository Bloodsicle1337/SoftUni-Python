TRAIN_TICKET = 150

collection_of_items = input().split("|")
budget = int(input())

profit = 0
sum_of_all_items = 0

for item in collection_of_items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if item_type == "Clothes":
        if item_price <= 50.00 and budget >= item_price:
            budget -= item_price
            selling_price = item_price * 1.40
            profit += selling_price - item_price
            sum_of_all_items += selling_price
            print(f"{selling_price:.2f}", end=" ")

    elif item_type == "Shoes":
        if item_price <= 35.00 and budget >= item_price:
            budget -= item_price
            selling_price = item_price * 1.40
            profit += selling_price - item_price
            sum_of_all_items += selling_price
            print(f"{selling_price:.2f}", end=" ")

    elif item_type == "Accessories":
        if item_price <= 20.50 and budget >= item_price:
            budget -= item_price
            selling_price = item_price * 1.40
            profit += selling_price - item_price
            sum_of_all_items += selling_price
            print(f"{selling_price:.2f}", end=" ")

print(f"\nProfit: {profit:.2f}")

if budget + sum_of_all_items >= TRAIN_TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
