from collections import deque

people_que = deque(input().split())
n = int(input())

while len(people_que) > 1:
    people_que.rotate(-(n-1))
    print(f"Removed {people_que.popleft()}")

print(f"Last is {people_que.popleft()}")