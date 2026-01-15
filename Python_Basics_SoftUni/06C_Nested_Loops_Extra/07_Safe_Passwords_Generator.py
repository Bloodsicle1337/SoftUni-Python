a = int(input())
b = int(input())
max_number_of_passwords = int(input())

A = 35
B = 64
counter = 0
has_ended = False

for simbol in range(1, a + 1):
    for simbol2 in range(1, b + 1):
        print(f"{chr(A)}{chr(B)}{simbol}{simbol2}{chr(B)}{chr(A)}|", end="")
        counter += 1

        if counter == max_number_of_passwords:
            has_ended = True
            break

        A += 1
        B += 1

        if A > 55:
            A = 35

        if B > 96:
            B = 64
    if has_ended:
        break