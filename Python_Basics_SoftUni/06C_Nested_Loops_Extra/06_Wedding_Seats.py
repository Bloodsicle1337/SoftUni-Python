last_sector = input()
rows_in_first_sector = int(input())
number_of_seats_in_odd_rows = int(input())

total_seats =  0
number_of_seats_in_even = number_of_seats_in_odd_rows + 2
result = ""

for sector in range(ord('A'), ord(last_sector) + 1):
    num_rows = rows_in_first_sector + (sector - ord('A'))

    for row in range(1, num_rows + 1):
        if row % 2 != 0:
            for seat in range(1, number_of_seats_in_odd_rows + 1):
                total_seats += 1
                result += f"{chr(sector)}{row}{chr(96 + seat)}\n"

        else:
            for seat in range(1, number_of_seats_in_even + 1):
                total_seats += 1
                result += f"{chr(sector)}{row}{chr(96 + seat)}\n"

print(f"{result}{total_seats}")
