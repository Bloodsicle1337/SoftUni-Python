text = input()

numbers = ""
letters = ""
special_characters = ""

for character in text:
    if character.isdigit():
        numbers += character

    elif character.isalpha():
        letters += character

    else:
        special_characters += character

print(numbers)
print(letters)
print(special_characters)