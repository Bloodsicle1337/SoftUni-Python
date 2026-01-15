king_number = int(input())
numbers = 1

while True:
    if numbers > king_number:
        break

    print(numbers)
    numbers = (numbers * 2) + 1
