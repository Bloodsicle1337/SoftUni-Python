PACKAGES_PENS = 5.80
PACKAGES_MARKERS = 7.20
DETEREGENT_PER_LITER = 1.20

pen_packages = int(input())
marker_packages = int(input())
liters_deteregent = int(input())
discount = int(input()) /100

pen_price = pen_packages * PACKAGES_PENS
marker_price = marker_packages * PACKAGES_MARKERS
deteregent_price = liters_deteregent * DETEREGENT_PER_LITER

full_price = pen_price + marker_price + deteregent_price
discount_price = full_price - (full_price * discount)
print(discount_price)