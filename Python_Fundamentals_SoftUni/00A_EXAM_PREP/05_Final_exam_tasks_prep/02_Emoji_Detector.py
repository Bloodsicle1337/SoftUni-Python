import re

text = input()

digits = re.findall(r"\d", text)
threshold = 1

for d in digits:
    threshold *= int(d)

pattern = r"(\*\*|::)([A-Z][a-z]{2,})\1"
matches = re.findall(pattern, text)

print(f"Cool threshold: {threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for symbol, word in matches:
    coolness = sum(ord(ch) for ch in word)

    if coolness > threshold:
        print(f"{symbol}{word}{symbol}")