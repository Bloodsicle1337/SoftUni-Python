start = int(input())
end = int(input())
magic_number = int(input())

count = 0
is_found = False

for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        count += 1

        if num1 + num2 == magic_number:
            is_found = True
            break

    if is_found:
        print(f"Combination N:{count} ({num1} + {num2} = {magic_number})")
        break
else:
    print(f"{count} combinations - neither equals {magic_number}")
