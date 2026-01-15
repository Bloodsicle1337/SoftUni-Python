budget = float(input())
price_per_kg_flour = float(input())
number_of_loaves_baked = 0
price_for_pack_eggs = price_per_kg_flour * 0.75
price_for_milk = price_per_kg_flour * 1.25
loaf_of_bread = price_per_kg_flour + price_for_pack_eggs + (price_for_milk * 0.25)

colored_eggs = 0

while budget >= loaf_of_bread:
    budget -= loaf_of_bread
    number_of_loaves_baked += 1
    colored_eggs += 3

    if number_of_loaves_baked % 3 == 0:
        colored_eggs -= (number_of_loaves_baked - 2)

print(f"You made {number_of_loaves_baked} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.02f}BGN left.")


