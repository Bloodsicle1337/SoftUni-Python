number_of_messages = int(input())
message_sent = ""

for _ in range(number_of_messages):
    number = int(input())

    if number == 88:
        message_sent = "Hello"

    elif number == 86:
        message_sent = "How are you?"

    elif number < 88:
        message_sent = "GREAT!"

    else:
        message_sent = "Bye."

    print(message_sent)