import re


patter = r"(www\.([a-zA-Z0-9\-]+)(\.[a-z]+)+)"

line = input()

while line:
    matches = re.search(patter, line, re.IGNORECASE)
    if matches:
        output = matches.group(1)
        print(output)
    line = input()
