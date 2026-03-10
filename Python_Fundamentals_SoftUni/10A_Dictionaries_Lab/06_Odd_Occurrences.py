words_input = input().split()
words_dict = {}

for word in words_input:
    word_lowercase = word.lower()

    if word_lowercase not in words_dict:
        words_dict[word_lowercase] = 0

    words_dict[word_lowercase] += 1

for key, value in words_dict.items():
    if value % 2 != 0:
        print(key, end=" ")