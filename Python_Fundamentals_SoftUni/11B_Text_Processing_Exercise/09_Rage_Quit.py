text = input()
result = ""
final_result = ""
rage_message = ""
unique_symbols = []
for index in range(len(text)):
    if not text[index].isdigit():
        result += text[index].upper()
    else:
        repeat = text[index]
        if index + 1 < len(text):
            if text[index + 1].isdigit():
                repeat += text[index + 1]
        rage_message += result * int(repeat)
        result = ""
        repeat = ""
print(f"Unique symbols used: {len(set(rage_message))}\n{rage_message}")