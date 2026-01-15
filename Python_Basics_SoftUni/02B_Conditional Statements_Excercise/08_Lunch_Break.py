from math import ceil
series = input()
episode = int(input())
launch_break = int(input())

eating_time = launch_break * 0.125
leisure_time = launch_break * 0.25

time_left = launch_break - (eating_time + leisure_time)

if time_left >= episode:
    print(f"You have enough time to watch {series} and left with {ceil(time_left - episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(episode - time_left)} more minutes.")