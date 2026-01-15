ivancho_age = 18

inherited_money = float(input())
year_of_death = int(input())
yearly_spendings = 0

for year in range(1800, year_of_death + 1):
    if year % 2 == 0:
        yearly_spendings += 12000
        ivancho_age += 1
    else:
        yearly_spendings += 12000 + (50 * ivancho_age)
        ivancho_age += 1


if inherited_money >= yearly_spendings:
    print(f"Yes! He will live a carefree life and will have {inherited_money - yearly_spendings:.2f} dollars left.")
else:
    print(f"He will need {(yearly_spendings - inherited_money):.2f} dollars to survive.")