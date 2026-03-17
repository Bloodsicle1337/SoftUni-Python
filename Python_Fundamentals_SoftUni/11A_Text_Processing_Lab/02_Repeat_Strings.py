text = input().split()
formated_text = ""
for word in text:
    formated_text += word * len(word)

print(formated_text)