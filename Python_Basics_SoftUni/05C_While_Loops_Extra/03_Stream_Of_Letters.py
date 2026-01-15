secret = ""
secret1 = ""
c_once = 0
o_once = 0
n_once = 0

while True:
    char = input()

    if char == "End":
        break

    if ("a" <= char <= "z") or ("A" <= char <= "Z"):
        if char == "c" and c_once < 1:
            c_once += 1
        elif char == "o" and o_once < 1:
            o_once += 1
        elif char == "n" and n_once < 1:
            n_once += 1
        else:
            secret += char

        if c_once == 1 and o_once == 1 and n_once == 1:
            secret1 += secret + " "
            secret = ""
            c_once = 0
            o_once = 0
            n_once = 0

print(secret1)