words = input().split()
result = []

for word in words:
    ascii_number = ""
    for char in word:
        if char.isdigit():
            ascii_number += char
        else:
            break

    first_letter = chr(int(ascii_number))
    rest_of_word = word[len(ascii_number):]

    deciphered_word = first_letter + rest_of_word

    if len(deciphered_word) > 2:
        deciphered_word_as_list = list(deciphered_word)
        deciphered_word_as_list[1], deciphered_word_as_list[-1] = deciphered_word_as_list[-1], deciphered_word_as_list[1]
        deciphered_word = "".join(deciphered_word_as_list)

    result.append(deciphered_word)

print(" ".join(result))