number = int(input())
key_word = input()

initial_list = []
filtered_list = []

for _ in range(number):
    strings = input()
    initial_list.append(strings)

    if key_word in strings:
        filtered_list.append(strings)
    else:
        continue

print(initial_list)
print(filtered_list)