number_of_inputs = int(input())

for _ in range(number_of_inputs):
    number = int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        break

else:
    print(f"All numbers are even.")