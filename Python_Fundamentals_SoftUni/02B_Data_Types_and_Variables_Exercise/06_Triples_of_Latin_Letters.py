number = int(input())

for num1 in range(97, 97 + number):
    for num2 in range(97, 97 + number):
        for num3 in range(97, 97 + number):
            print(f"{chr(num1)}{chr(num2)}{chr(num3)}")
