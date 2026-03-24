text = input().split()

for word in text:
    for index in range(len(word)):
        if word[index] == ":":
            print(word[index] + word[index + 1])