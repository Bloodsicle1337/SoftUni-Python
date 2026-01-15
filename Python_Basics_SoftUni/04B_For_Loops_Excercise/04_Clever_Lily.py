lili_years = int(input())
washing_machine = float(input())
toy_price = int(input())
toy_years = 0
birthday_sum = 0
money_years = 0
current_money = 10
brother_cut = 0
for x in range(1, lili_years + 1):
    if x % 2 == 0:
        birthday_sum += current_money
        brother_cut += 1
        current_money += 10
    else:
        toy_years += 1
toy_sum = toy_years * toy_price
total_sum_saved = (birthday_sum + toy_sum) - brother_cut

if total_sum_saved >= washing_machine:
    print(f"Yes! {total_sum_saved - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - total_sum_saved:.2f}")