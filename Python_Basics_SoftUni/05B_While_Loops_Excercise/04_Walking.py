GOAL_STEPS_PER_DAY = 10_000

steps_sum = 0

while steps_sum < GOAL_STEPS_PER_DAY:
    steps = input()

    if steps == "Going home":
        final_steps = int(input())
        steps_sum += final_steps
        break

    steps = int(steps)
    steps_sum += steps

if steps_sum >= GOAL_STEPS_PER_DAY:
    print(f"Goal reached! Good job!\n{steps_sum - GOAL_STEPS_PER_DAY} steps over the goal!")

else:
    print(f"{GOAL_STEPS_PER_DAY - steps_sum} more steps to reach goal.")


