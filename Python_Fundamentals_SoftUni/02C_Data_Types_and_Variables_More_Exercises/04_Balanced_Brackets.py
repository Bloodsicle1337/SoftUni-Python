number_of_inputs = int(input())
list_of_brackets = []
is_balanced = True

for _ in range(number_of_inputs):
    string = input()
    if string == "(":
        if "(" in list_of_brackets:
            is_balanced = False

        list_of_brackets.append(string)

    if string == ")":
        if list_of_brackets:
            list_of_brackets.pop()
        else:
            is_balanced = False

if len(list_of_brackets) > 0:
    is_balanced = False

if is_balanced:
    print("BALANCED")

else:
    print("UNBALANCED")
