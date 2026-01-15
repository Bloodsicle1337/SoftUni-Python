CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGI_MENU = 8.15
TIP = 2.50

chicken_wants = int(input())
fish_wants = int(input())
vegi_wants = int(input())

main_course_price = (chicken_wants * CHICKEN_MENU) + (fish_wants * FISH_MENU) + (vegi_wants * VEGI_MENU)
desert_price = main_course_price * 0.20

full_price = round(main_course_price + desert_price + TIP, 2)
print(full_price)