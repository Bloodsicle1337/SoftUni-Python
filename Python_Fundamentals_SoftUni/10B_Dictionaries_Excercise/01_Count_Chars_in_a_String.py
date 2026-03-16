stringed_text = input()
occurrences = {}

for character in stringed_text:
    if character == " ":
        continue

    if character not in occurrences.keys():
        occurrences[character] = 0

    occurrences[character] += 1

for key, value in occurrences.items():
    print(f"{key} -> {value}")

