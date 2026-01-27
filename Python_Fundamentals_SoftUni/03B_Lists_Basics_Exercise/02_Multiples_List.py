factor = int(input())
count = int(input())
multiples_list = []

for index_multiplier in range(1, count + 1):
    multiples_list.append(factor * index_multiplier)

print(multiples_list)