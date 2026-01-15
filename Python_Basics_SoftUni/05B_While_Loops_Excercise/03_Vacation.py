needed_money_for_vacation = float(input())
budget = float(input())

is_enough = False
days_spending_count = 0
money_for_that_day = 0
days_count = 0

while days_spending_count < 5:
    type_of_action = input()
    money_for_that_day = float(input())
    days_count += 1

    if type_of_action == "spend":
        days_spending_count += 1
        if budget >= money_for_that_day:
            budget -= money_for_that_day
        else:
            budget = 0

    elif type_of_action == "save":
        days_spending_count = 0
        budget += money_for_that_day
        if budget >= needed_money_for_vacation:
            is_enough = True
            break

if is_enough:
    print(f"You saved the money for {days_count} days.")

else:
    print(f"You can't save the money.\n{days_count}")