def is_pass_valid(password: str) -> str:
    is_length_valid = False
    is_alnum_valid = False
    is_digit_count_valid = False
    return_result = ""
    digits = 0

    if 6 <= len(password) <= 10:
        is_length_valid = True

    else:
        return_result += "Password must be between 6 and 10 characters\n"

    if password.isalnum():
        is_alnum_valid = True

    else:
        return_result += "Password must consist only of letters and digits\n"

    for char in password:
        if char.isdigit():
            digits += 1

    if digits >= 2:
        is_digit_count_valid = True

    else:
        return_result += "Password must have at least 2 digits"

    if is_length_valid and is_alnum_valid and is_digit_count_valid:
        return "Password is valid"

    else:
        return return_result

user_password = input()
final_result = is_pass_valid(user_password)
print(final_result)