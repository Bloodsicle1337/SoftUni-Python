first_char = input()
second_char = input()
text = input()

start = ord(first_char)
end = ord(second_char)

total_sum = 0

for char in text:
    current_ascii = ord(char)

    if current_ascii > min(start, end) and current_ascii < max(start, end):
        total_sum += current_ascii

print(total_sum)