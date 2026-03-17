banned_text = input().split(", ")
censored_text = input()

for word in banned_text:
    censored_text = censored_text.replace(word, len(word) * "*")

print(censored_text)