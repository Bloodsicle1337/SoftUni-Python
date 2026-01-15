string1 = input()
string2 = input()
transformer_word = ""

for char_index in range(len(string1)):

    left_side = string2[:char_index + 1]
    right_side = string1[char_index + 1:]

    transformer_word = left_side + right_side

    if string1[char_index] != string2[char_index]:
        print(transformer_word)