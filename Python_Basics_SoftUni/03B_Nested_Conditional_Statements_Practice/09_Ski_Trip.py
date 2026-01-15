ROOM_FOR_ONE = 18.00
APART = 25.00
PRESIDENT_APART = 35.00

days = int(input()) - 1
room_type = input()
feedback = input()

total_price = (days * ROOM_FOR_ONE)

if days < 10:
    if room_type == "apartment":
        total_price = (days * APART) - ((days * APART) * 0.30)
    elif room_type == "president apartment":
        total_price = (days * PRESIDENT_APART) - ((days * PRESIDENT_APART) * 0.10)
elif 10 <= days <= 15:
    if room_type == "apartment":
        total_price = (days * APART) - ((days * APART) * 0.35)
    elif room_type == "president apartment":
        total_price = (days * PRESIDENT_APART) - ((days * PRESIDENT_APART) * 0.15)
elif days > 20:
    if room_type == "apartment":
        total_price = (days * APART) - ((days * APART) * 0.50)
    elif room_type == "president apartment":
        total_price = (days * PRESIDENT_APART) - ((days * PRESIDENT_APART) * 0.20)

if feedback == "positive":
    total_price += total_price * 0.25
elif feedback == "negative":
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")