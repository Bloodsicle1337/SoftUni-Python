YEARLY_GOAL_PLAYTIME = 30000
WORK_DAY_PLAYTIME = 63
OFF_DAY_PLAYTIME = 127

number_of_off_days = int(input())

sum_playtime = ((365 - number_of_off_days) * WORK_DAY_PLAYTIME) + (number_of_off_days * OFF_DAY_PLAYTIME)
difference = 0
hours = 0
minutes = 0

if sum_playtime > YEARLY_GOAL_PLAYTIME:
    difference += sum_playtime - YEARLY_GOAL_PLAYTIME
    hours += difference // 60
    minutes += difference % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    difference += YEARLY_GOAL_PLAYTIME - sum_playtime
    hours += difference // 60
    minutes += difference % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")