num1_max = int(input())
num2_max = int(input())
num3_max = int(input())

for num1 in range(1, num1_max + 1):
    if num1 % 2 != 0:
        continue

    for num2 in range(2, num2_max + 1):
        is_prime = True
        for number in range(2, num2):
            if num2 % number == 0:
                is_prime = False
                break

        if not is_prime:
            continue

        for num3 in range(1, num3_max + 1):
            if num3 % 2 != 0:
                continue

            print(f"{num1} {num2} {num3}")



