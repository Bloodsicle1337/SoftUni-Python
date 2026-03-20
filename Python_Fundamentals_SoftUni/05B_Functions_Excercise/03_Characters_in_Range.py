def string_chars(start: str, finish: str) -> list:
    characters = []
    for char in range(ord(start) + 1, ord(finish)):
        characters.append(chr(char))
    return characters

start_char = input()
end_char = input()

result = string_chars(start_char, end_char)
print(" ".join(result))
