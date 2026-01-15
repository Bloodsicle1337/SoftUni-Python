year = int(input())

while True:
    year += 1
    year_str = str(year)
    set_year = set(year_str)

    if len(set_year) == len(year_str):
        print(year)
        break

    else:
        continue
