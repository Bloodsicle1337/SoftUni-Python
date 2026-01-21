number = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(number):
    num = int(input())

    if num >= 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)

print(positive_numbers)
print(negative_numbers)

print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
