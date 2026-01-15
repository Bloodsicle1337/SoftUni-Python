num1 = int(input())
num2 = int(input())
num3 = int(input())
number = 0

if num1 > num2 and num1 > num3:
    number = num1

elif num2 > num1 and num2 > num3:
    number = num2

else:
    number = num3

print(number)