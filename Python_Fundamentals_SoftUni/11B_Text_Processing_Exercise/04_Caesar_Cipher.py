cypher_message = input()
encrypt_message = ""
new_message = ""
for index in range(len(cypher_message)):
    encrypt_message += chr(ord(cypher_message[index]) + 3)

print(encrypt_message)
