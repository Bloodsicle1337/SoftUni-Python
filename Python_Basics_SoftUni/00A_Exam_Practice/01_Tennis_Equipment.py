from math import floor
from math import ceil

price_for_racket = float(input())
number_of_rackets = int(input())
number_of_shoes = int(input())

racket_total_bill = price_for_racket * number_of_rackets
price_for_shoes = price_for_racket/ 6
shoes_total_bill = price_for_shoes * number_of_shoes
other_equipment_bill = (racket_total_bill + shoes_total_bill) * 0.20

total_price = shoes_total_bill + other_equipment_bill + racket_total_bill

print(f"Price to be paid by Djokovic {floor(total_price * 0.125)}")
print(f"Price to be paid by sponsors {ceil(total_price * 0.875)}")