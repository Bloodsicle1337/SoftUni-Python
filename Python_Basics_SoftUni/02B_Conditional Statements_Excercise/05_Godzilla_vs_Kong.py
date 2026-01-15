film_budget = float(input())
number_of_statists = int(input())
costume_price = float(input())

film_decor = film_budget * 0.10

if number_of_statists > 150:
    costume_price -= costume_price * 0.10

actual_price = number_of_statists * costume_price + film_decor
if actual_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(film_budget - actual_price):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(actual_price - film_budget):.2f} leva left.")