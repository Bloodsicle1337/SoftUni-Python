text = input()
my_list = []

for char in text:
    my_list.append(char)

while len(my_list) > 0:
    print(my_list.pop(), end='')