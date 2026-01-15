num1 = int(input())
num2 = int(input())



for num in range(num1, num2 + 1):
    stringed_num = str(num)
    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(stringed_num):
        if digit == 0:
            continue

        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if even_sum == odd_sum:
        print(num, end=" ")

