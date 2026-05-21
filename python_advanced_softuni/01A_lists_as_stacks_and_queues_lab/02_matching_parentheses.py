text = input()
my_stack = []

for i in range(len(text)):
    if text[i] == "(":
        my_stack.append(i)

    elif text[i] == ")":
        start_index = my_stack.pop()
        finish_index = i + 1
        print(text[start_index:finish_index])