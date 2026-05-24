number_of_names = int(input())
odd_set = set()
even_set = set()


for row in range(1, number_of_names + 1):
    current_number = sum(ord(ch) for ch in input()) // row
    if current_number % 2 == 0:
        even_set.add(current_number)
    else:
        odd_set.add(current_number)

odd_set_sum, even_set_sum = sum(odd_set), sum(even_set)

if odd_set_sum == even_set_sum:
    print(*odd_set.union(even_set), sep=", ")

elif odd_set_sum > even_set_sum:
    print(*odd_set.difference(even_set), sep=", ")

else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")