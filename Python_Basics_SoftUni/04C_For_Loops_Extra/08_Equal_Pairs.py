number_of_pairs = int(input())

a = int(input())
b = int(input())
first_value = a + b
previous_value = first_value
current_value = 0
max_diff = 0

for _ in range(1, number_of_pairs):
    a = int(input())
    b = int(input())
    current_value = a + b

    diff = current_value - previous_value
    if diff < 0:
        diff = -diff

    if diff > max_diff:
        max_diff = diff

    previous_value = current_value

if max_diff == 0:
    print(f"Yes, value={first_value}")
else:
    print(f"No, maxdiff={max_diff}")
