is_finished = False

while True:
    travel_destination = input()

    if travel_destination == "End":
        break

    budget_target = float(input())
    sum_gathered = 0.00

    while sum_gathered < budget_target:
        money = input()

        if money == "End":
            is_finished = True
            break

        money = float(money)
        sum_gathered += money

    print(f"Going to {travel_destination}!")