number = int(input())
is_prime = True

if number < 2:
    print(False)

else:
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break

    print(is_prime)