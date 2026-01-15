num = int(input())
sum_average = 0
for _ in range(num):
    new_num = int(input())
    sum_average += new_num

print(f"{sum_average / num:.2f}")