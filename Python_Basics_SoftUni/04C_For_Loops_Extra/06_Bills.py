WATER_PER_MONTH = 20
INTERNET_PER_MONTH = 15

billed_months = int(input())
electricity = 0
water = 0
internet = 0
other_bill = 0
average_bill = 0
electricity_bill = 0

for _ in range(billed_months):
    electricity_per_month = float(input())
    water += 1
    internet += 1
    electricity += 1
    electricity_bill += electricity_per_month
    other_bill += ((electricity_per_month + WATER_PER_MONTH + INTERNET_PER_MONTH) +
                   ((electricity_per_month + WATER_PER_MONTH + INTERNET_PER_MONTH) * 0.20))

water_bill = water * WATER_PER_MONTH
internet_bill = internet * INTERNET_PER_MONTH
average_bill = electricity_bill + water_bill + internet_bill + other_bill

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {(average_bill / billed_months):.2f} lv")