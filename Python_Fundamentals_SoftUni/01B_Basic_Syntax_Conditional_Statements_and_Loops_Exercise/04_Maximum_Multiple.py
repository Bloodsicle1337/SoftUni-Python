divisor = int(input())
boundary = int(input())

for number in range(boundary, 1, -1):
    if (number <= boundary) and (number % divisor == 0) and (number > 0):
        print(number)
        break

