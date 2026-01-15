n = int(input())

found = False

for a in range(1, 10):
    if found:
        break
    for b in range(9, a - 1, -1):
        if found:
            break
        for c in range(0, 10):
            if found:
                break
            for d in range(9, c - 1, -1):

                summed = a + b + c + d
                multiplied = a * b * c * d

                if (summed == multiplied) and (n % 10 == 5):
                    print(f"{a}{b}{c}{d}")
                    found = True
                    break

                if (multiplied // summed == 3) and (n % 3 == 0):
                    print(f"{d}{c}{b}{a}")
                    found = True
                    break

if not found:
    print("Nothing found")