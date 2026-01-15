tshirt_price = float(input())
target_for_football = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.20
boots_price = (tshirt_price + shorts_price) * 2

total_sum = tshirt_price + shorts_price + socks_price + boots_price

total_sum -= total_sum * 0.15


if total_sum >= target_for_football:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")

else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {target_for_football - total_sum:.2f} lv. more.")