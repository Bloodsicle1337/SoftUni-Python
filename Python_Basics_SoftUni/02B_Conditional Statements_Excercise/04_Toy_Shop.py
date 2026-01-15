PUZZLE = 2.60
TALKING_DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

trip_price = float(input())
puzzles_purchased = int(input())
talking_dolls_purchased = int(input())
teddy_bears_purchased = int(input())
minions_purchased = int(input())
trucks_purchased = int(input())
discount = 0


toys_price = ((puzzles_purchased * PUZZLE) +
              (talking_dolls_purchased * TALKING_DOLL) +
              (teddy_bears_purchased * TEDDY_BEAR) +
              (minions_purchased * MINION) +
              (trucks_purchased * TRUCK))

sum_toys = puzzles_purchased + talking_dolls_purchased + teddy_bears_purchased + minions_purchased + trucks_purchased

if sum_toys >= 50:
    discount += toys_price * 0.25

final_price = toys_price - discount

shop_rent = final_price * 0.10
amount_left = final_price - shop_rent

if amount_left >= trip_price:
    print(f"Yes! {amount_left - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - amount_left:.2f} lv needed.")