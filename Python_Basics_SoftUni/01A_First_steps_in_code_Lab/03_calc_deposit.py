deposit = float(input())
time_of_deposit = int(input())
year_interest = float(input()) / 100

total = deposit + time_of_deposit * ((deposit * year_interest) / 12)
print(total)