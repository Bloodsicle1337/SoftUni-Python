number_of_words = int(input())
synonyms = {}

for _ in range(number_of_words):
    word_input = input()
    synonym_input = input()

    if word_input not in synonyms:
        synonyms[word_input] = []

    synonyms[word_input].append(synonym_input)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")