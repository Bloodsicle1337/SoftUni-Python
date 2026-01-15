num_start = int(input())
num_end = int(input())
result = ""
for num1 in range(num_start, num_end + 1):
    if num1 % 2 == 0:
        for num2 in range(num_start, num_end + 1):
            for num3 in range(num_start, num_end + 1):
                if (num2 + num3) % 2 == 0:
                    for num4 in range(num_start, num_end + 1):
                        if (num4 % 2 != 0) and (num1 > num4):
                            result += f"{num1}{num2}{num3}{num4} "
                        else:
                            continue
    else:
        for num2 in range(num_start, num_end + 1):
            for num3 in range(num_start, num_end + 1):
                if (num2 + num3) % 2 == 0:
                    for num4 in range(num_start, num_end + 1):
                        if (num4 % 2 == 0) and (num1 > num4):
                            result += f"{num1}{num2}{num3}{num4} "
                        else:
                            continue
print(result)