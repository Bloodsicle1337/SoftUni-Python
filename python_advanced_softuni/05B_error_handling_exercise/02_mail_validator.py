class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(NameTooShortError):
    pass

class InvalidDomainError(NameTooShortError):
    pass

EMAIL_MIN_NAME_LENGHT = 5
VALID_DOMAINS = ["com", "net", "bg", "org"]

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < EMAIL_MIN_NAME_LENGHT:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email.split(".")[-1]

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be onf of the following: .com, .bg, .org, .net")

    print("Email is valid")
