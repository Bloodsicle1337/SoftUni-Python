text = input().lower()
keywords = ["sand", "water", "fish", "sun"]
count = 0

for word in keywords:
    count += text.count(word)

print(count)