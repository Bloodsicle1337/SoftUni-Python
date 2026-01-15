square_meters = float(input())
not_discounted_price = square_meters * 7.61
discount = not_discounted_price * 0.18

discounted_price = not_discounted_price - discount

print(f"The final price is: {discounted_price} lv.")
print(f"The discount is: {discount} lv.")