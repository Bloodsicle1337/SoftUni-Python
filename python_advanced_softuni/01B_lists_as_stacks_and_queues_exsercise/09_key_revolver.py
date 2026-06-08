from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())

intelligence_value = int(input())

shots_fired = 0
current_barrel = barrel_size

while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]

    shots_fired += 1
    current_barrel -= 1

    if bullet <= lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if current_barrel == 0 and bullets:
        print("Reloading!")
        current_barrel = barrel_size

if not locks:
    earned_money = intelligence_value - shots_fired * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")