FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

tabs_open = int(input())
salary = int(input())

for tab in range(tabs_open):
    site = input()
    if site == "Facebook":
        salary -= FACEBOOK_FINE
    elif site == "Instagram":
        salary -= INSTAGRAM_FINE
    elif site == "Reddit":
        salary -= REDDIT_FINE

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)