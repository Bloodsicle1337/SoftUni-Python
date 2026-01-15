from math import ceil
from math import floor

MAGNOLIAS = 3.25
HYACINTHS = 4
ROSES = 3.50
CACTI = 8

# 5% of total sum should be deducted for TAX
number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
present_price = float(input())

total_profit = ((number_of_magnolias * MAGNOLIAS) +
             (number_of_hyacinths * HYACINTHS) +
             (number_of_roses * ROSES) +
             (number_of_cacti * CACTI))

tax = total_profit * 0.05
total_sum = total_profit - tax

if total_sum >= present_price:
    print(f"She is left with {floor(total_sum - present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - total_sum)} leva.")