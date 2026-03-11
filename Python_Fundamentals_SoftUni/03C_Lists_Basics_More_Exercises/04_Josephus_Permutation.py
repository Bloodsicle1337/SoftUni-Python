soldier_line = input().split()
unlucky_number = int(input())

result = []
index = 0

while len(soldier_line) > 0:
    index = (index + unlucky_number - 1) % len(soldier_line)
    removed = soldier_line.pop(index)
    result.append(removed)

print("[" + ",".join(result) + "]")