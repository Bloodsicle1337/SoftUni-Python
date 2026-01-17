key = int(input())
number_of_inputs = int(input())

for num in range(number_of_inputs):
    character = input()
    ascii_number = ord(character)
    decripted_chr = chr(ascii_number + key)
    print(decripted_chr, end="")