text = input().split()
final_number = 0

for word in text:
    number = int(word[1:-1])
    start_letter_position = ord(word[0].upper()) - ord("A") + 1
    last_letter_position = ord(word[-1].upper()) - ord("A") + 1
    if word[0].isupper():
        final_number += number / start_letter_position

    else:
        final_number += number * start_letter_position

    if word[-1].isupper():
        final_number -= last_letter_position

    else:
        final_number += last_letter_position

print(f"{final_number:.2f}")
