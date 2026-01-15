budget = int(input())
money_spent = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    price = int(command)

    if money_spent + price > budget:
        print("You went in overdraft!")
        break

    money_spent += price


# budget = int(input())
# command = input()
# money_spent = 0
#
# while command != "End":
#     price_of_product = int(command)
#
#     money_spent += price_of_product
#
#     if money_spent > budget:
#         print("You went in overdraft!")
#         break
#
#     command = input()
#
# else:
#     print("You bought everything needed.")


