def is_length_valid(name:str) -> bool:
    if 3 <= len(name) <= 16:
        return True

    else:
        return False

def are_symbols_valid(name:str) -> bool:
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False

    return True


def are_symbols_redundant(name:str) -> bool:
    if "  " in name:
        return False

    else:
        return True

def is_input_valid(name:str) -> bool:
    if is_length_valid(name) and are_symbols_valid(name) and are_symbols_redundant(name):
        return True

    else:
        return False

text = input().split(", ")

for word in text:
    if is_input_valid(word):
        print(word)