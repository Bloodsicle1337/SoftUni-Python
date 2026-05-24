from collections import deque

robot_data = input().split(";")
robots = []

for r in robot_data:
    r_name, r_time = r.split("-")
    robots.append({"name": r_name, "process_time": int(r_time), "busy_until": 0})

h, m, s = [int(x) for x in input().split(":")]
start_time_in_sec = h * 3600 + m * 60 + s

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    curr_product = products.popleft()
    start_time_in_sec += 1

    for r in robots:
        if r["busy_until"] <= start_time_in_sec:
            r["busy_until"] = start_time_in_sec + r["process_time"]
            hours = start_time_in_sec // 3600
            minutes = (start_time_in_sec % 3600) // 60
            seconds = (start_time_in_sec % 3600) % 60

            hours %= 24
            print(f"{r['name']} - {curr_product} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
            break
    else:
        products.append(curr_product)