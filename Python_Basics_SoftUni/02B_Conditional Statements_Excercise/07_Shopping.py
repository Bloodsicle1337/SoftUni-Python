GPU_PRICE = 250

budget = float(input())
gpu_number = int(input())
cpu_number = int(input())
ram_number = int(input())

gpu_price = gpu_number * GPU_PRICE
cpu_price = (gpu_price * 0.35) * cpu_number
ram_price = (gpu_price * 0.10) * ram_number
discount = 0

total_price = gpu_price + ram_price + cpu_price

if gpu_number > cpu_number:
    discount += total_price * 0.15

final_price = total_price - discount

if budget >= final_price:
    print(f"You have {budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva more!")