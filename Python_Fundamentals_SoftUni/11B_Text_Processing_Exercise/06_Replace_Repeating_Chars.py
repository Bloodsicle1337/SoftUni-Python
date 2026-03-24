text_input = input()
final_text = ""

for char in text_input:
    if not final_text or char != final_text[-1]:
        final_text += char

print(final_text)