def palindrome(text_list: list) -> list:
    return_list = []
    for text in text_list:
        if text[::] == text[::-1]:
            return_list.append(True)

        else:
            return_list.append(False)

    return return_list

initial_list = input().split(", ")

result = palindrome(initial_list)

for res in result:
    print(res)