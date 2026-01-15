MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
hours = int(input())
minutes = int(input()) + 15

if minutes >= MINUTES_IN_HOUR:
    minutes -= MINUTES_IN_HOUR
    hours += 1

if hours >= HOURS_IN_DAY:
    hours -= HOURS_IN_DAY

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")