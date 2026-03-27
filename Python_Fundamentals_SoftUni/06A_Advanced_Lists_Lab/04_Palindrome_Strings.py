words = input().split()
searched_word = input()

palindromes = []

for word in words:
    reversed_word = ""

    for index in range(len(word) - 1, -1, -1):
        reversed_word += word[index]

    if word == reversed_word:
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_word)} times")