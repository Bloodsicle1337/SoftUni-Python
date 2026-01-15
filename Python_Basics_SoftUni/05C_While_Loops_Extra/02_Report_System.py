charity_goal = int(input())
item_number = 0
cash_people = 0
card_people = 0
sum_accumulated = 0
cash_accumulated = 0
card_accumulated = 0

while sum_accumulated < charity_goal:
    item = input()

    if item == "End":
        break

    item = int(item)

    if item_number % 2 == 0:
        if item <= 100:
            cash_people += 1
            cash_accumulated += item
            item_number += 1
            print("Product sold!")
            sum_accumulated += item
        else:
            print("Error in transaction!")
            item_number += 1

    else:
        if item >= 10:
            card_people += 1
            print("Product sold!")
            card_accumulated += item
            sum_accumulated += item
            item_number += 1
        else:
            print("Error in transaction!")
            item_number += 1

if sum_accumulated < charity_goal:
    print("Failed to collect required money for charity.")
else:
    print(f"Average CS: {cash_accumulated / cash_people:.2f}")
    print(f"Average CC: {card_accumulated / card_people:.2f}")
