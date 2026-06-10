class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


MINIMUM_AGE = 18

account_info = input().split(", ")

correct_pin = int(account_info[0])
balance = float(account_info[1])
age = int(account_info[2])

while True:
    command = input()

    if command == "End":
        break

    command_parts = command.split("#")
    action = command_parts[0]

    if action == "Send Money":
        money_to_send = float(command_parts[1])
        entered_pin = int(command_parts[2])

        if money_to_send > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if entered_pin != correct_pin:
            raise PINCodeError("Invalid PIN code")

        if age < MINIMUM_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money_to_send

        print(f"Successfully sent {money_to_send:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif action == "Receive Money":
        received_money = float(command_parts[1])

        if received_money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        money_for_account = received_money / 2
        balance += money_for_account

        print(f"{money_for_account:.2f} money went straight into the bank account")