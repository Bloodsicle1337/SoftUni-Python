numbers = input().split()
text = list(input())

message = []

for num in numbers:
    digit_sum = 0

    for ch in num:
        digit_sum += (int(ch))

    index = digit_sum % len(text)

    message.append(text[index])

    text.pop(index)

print ("".join(message))