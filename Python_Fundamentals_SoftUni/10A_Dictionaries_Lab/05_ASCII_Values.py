char_list = input().split(", ")

char_dict = {char: ord(char) for char in char_list}
print(char_dict)