class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


def is_password_too_common(password, special_symbols):
    contains_only_digits = password.isdigit()
    contains_only_letters = password.isalpha()
    contains_only_specials = all(symbol in special_symbols for symbol in password)

    return contains_only_digits or contains_only_letters or contains_only_specials


MIN_PASSWORD_LENGTH = 8
SPECIAL_SYMBOLS = ["@", "*", "&", "%"]

while True:
    password = input()

    if password == "Done":
        break

    if len(password) < MIN_PASSWORD_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    if is_password_too_common(password, SPECIAL_SYMBOLS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(symbol in SPECIAL_SYMBOLS for symbol in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    print("Password is valid")