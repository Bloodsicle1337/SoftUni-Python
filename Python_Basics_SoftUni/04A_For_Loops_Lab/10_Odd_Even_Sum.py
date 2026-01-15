number = int(input())
sum_odd = 0
sum_even = 0

for n in range(number):
    num = int(input())
    if n % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

if sum_odd == sum_even:
    print(f"Yes\nSum = {sum_odd}")
else:
    print(f"No\nDiff = {abs(sum_odd - sum_even)}")