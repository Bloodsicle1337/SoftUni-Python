text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

result = ''.join([char for char in text if char not in vowels])
print(result)