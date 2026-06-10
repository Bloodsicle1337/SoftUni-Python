class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_NAME_LENGTH = 5
ALLOWED_DOMAINS = ["com", "bg", "org", "net"]

while True:
    email_address = input()

    if email_address == "End":
        break

    if "@" not in email_address:
        raise MustContainAtSymbolError("Email must contain @")

    username = email_address.split("@")[0]

    if len(username) < MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email_address.split(".")[-1]

    if domain not in ALLOWED_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")