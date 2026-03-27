key = input().split()
key_numbers = []

for number in key:
    key_numbers.append(int(number))

while True:
    text = input()

    if text == "find":
        break

    decrypted_message = ""

    key_index = 0

    for char in text:
        decrypted_char = chr(ord(char) - key_numbers[key_index])
        decrypted_message += decrypted_char

        key_index += 1

        if key_index == len(key_numbers):
            key_index = 0

    start_type_index = decrypted_message.index("&") + 1
    end_type_index = decrypted_message.index("&", start_type_index)
    treasure_type = decrypted_message[start_type_index:end_type_index]

    start_coordinates_index = decrypted_message.index("<") + 1
    end_coordinates_index = decrypted_message.index(">")
    coordinates = decrypted_message[start_coordinates_index:end_coordinates_index]

    print(f"Found {treasure_type} at {coordinates}")