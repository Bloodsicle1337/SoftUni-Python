days_of_plunder = int(input())
daily_plunder = int(input())
plunder_goal = float(input())
total_gathered_plunder = 0

for current_day in range(1, days_of_plunder + 1):
    total_gathered_plunder += daily_plunder

    if current_day % 3 == 0:
        total_gathered_plunder += daily_plunder * 0.50

    if current_day % 5 == 0:
        total_gathered_plunder -= total_gathered_plunder * 0.30

if total_gathered_plunder >= plunder_goal:
    print(f"Ahoy! {total_gathered_plunder:.02f} plunder gained.")

else:
    print(f"Collected only {(total_gathered_plunder / plunder_goal) * 100:.02f}% of the plunder.")