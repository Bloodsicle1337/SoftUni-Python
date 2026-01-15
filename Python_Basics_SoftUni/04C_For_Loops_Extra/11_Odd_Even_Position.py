import sys

number_of_numbers = int(input())
OddSum = 0
OddMin = sys.maxsize
OddMax = -sys.maxsize

EvenSum = 0
EvenMin = sys.maxsize
EvenMax = -sys.maxsize

if number_of_numbers == 0:
    print(f"OddSum=0.00,")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum=0.00,")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

else:
    for num in range(1, number_of_numbers + 1):
        number = float(input())

        if num % 2 == 0:
            EvenSum += number

            if number < EvenMin:
                EvenMin = number

            if number > EvenMax:
                EvenMax = number

        else:
            OddSum += number

            if number < OddMin:
                OddMin = number

            if number > OddMax:
                OddMax = number

    if EvenMin == sys.maxsize and EvenMax == -sys.maxsize:
        print(f"OddSum={OddSum:.2f},")
        print(f"OddMin={OddMin:.2f},")
        print(f"OddMax={OddMax:.2f},")
        print(f"EvenSum={EvenSum:.2f},")
        print(f"EvenMin=No,")
        print(f"EvenMax=No")

    else:
        print(f"OddSum={OddSum:.2f},")
        print(f"OddMin={OddMin:.2f},")
        print(f"OddMax={OddMax:.2f},")
        print(f"EvenSum={EvenSum:.2f},")
        print(f"EvenMin={EvenMin:.2f},")
        print(f"EvenMax={EvenMax:.2f}")
