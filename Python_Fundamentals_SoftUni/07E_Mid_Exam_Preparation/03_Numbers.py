numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)

greater_numbers = []

for num in numbers:
    if num > average:
        greater_numbers.append(num)

greater_numbers.sort(reverse=True)

if len(greater_numbers) == 0:
    print("No")
else:
    top_five = greater_numbers[:5]
    print(" ".join(map(str, top_five)))