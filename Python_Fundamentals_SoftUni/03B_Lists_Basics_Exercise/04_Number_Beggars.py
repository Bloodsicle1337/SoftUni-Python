money_for_grab = input().split(", ")
number_of_beggars = int(input())
sum_for_current_beggar = 0
each_beggar_share =[]
beggar_starting_money = 0
index = 0

for beggar in range(number_of_beggars):
    sum_for_current_beggar = 0

    for money in range(index, len(money_for_grab), number_of_beggars):
        sum_for_current_beggar += int(money_for_grab[money])

    each_beggar_share.append(sum_for_current_beggar)
    index += 1

print(each_beggar_share)