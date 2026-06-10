class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

def password_too_common(password, special_chars):
    only_digits = password.isdigit()
    only_specials = all(ch in special_chars for ch in password)
    only_letters = password.isalpha()
    return only_digits or only_letters or only_specials

PASSWORD_MIN_LEN = 8
SPECIAL_CHAR_LIST = ["@", "&", "*", "%"]

while True:
    password = input()

    if password == "Done":
        break

    if len(password) < PASSWORD_MIN_LEN:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(password, SPECIAL_CHAR_LIST):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in SPECIAL_CHAR_LIST for char in password):
        raise PasswordNoSpacialCharactersError("Password must contain at least 1 spacial character")

    if " " in password:
        raise PassswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")