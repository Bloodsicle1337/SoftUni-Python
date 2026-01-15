pool_volume = int(input())
pipe1_debit_per_hour = int(input())
pipe2_debit_per_hour = int(input())
hours = float(input())

both_pipes_rate = pipe1_debit_per_hour + pipe2_debit_per_hour

pipe1_percentage = (pipe1_debit_per_hour / both_pipes_rate) * 100
pipe2_percentage = (pipe2_debit_per_hour / both_pipes_rate) * 100

total_water_added = both_pipes_rate * hours
percent_filled = (total_water_added / pool_volume) * 100

if percent_filled <= 100:
    print(f"The pool is {percent_filled:.2f}% full. Pipe 1: {pipe1_percentage:.2f}%. Pipe 2: {pipe2_percentage:.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {total_water_added - pool_volume:.2f} liters.")