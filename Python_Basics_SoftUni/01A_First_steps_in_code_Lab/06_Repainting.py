NYLON = 1.50
PAINT = 14.50
THINNER = 5.00
BAGS = 0.40

needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hours_for_completion = int(input())

nylon_price = NYLON * (needed_nylon + 2)
paint_price = PAINT * needed_paint + (PAINT * needed_paint * 0.10)
thinner_price = THINNER * needed_thinner
material_price = paint_price + thinner_price + nylon_price + BAGS
hours_price = (material_price * 0.30) * hours_for_completion

full_price = hours_price + material_price
print(full_price)