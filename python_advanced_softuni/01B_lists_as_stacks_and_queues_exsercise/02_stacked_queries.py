num = int(input())
stack = []

for _ in range(num):
    queries = input().split()
    command = int(queries[0])
    if len(queries) == 2:
        value = int(queries[1])

    if command == 1:
        stack.append(value)
    if stack:
        if command == 2:
            stack.pop()

        elif command == 3:
            print(f"{max(stack)}")

        elif command == 4:
            print(f"{min(stack)}")

print(", ".join(str(x) for x in reversed(stack)))

