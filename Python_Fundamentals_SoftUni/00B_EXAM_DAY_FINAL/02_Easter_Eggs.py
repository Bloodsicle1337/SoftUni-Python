import re

text = input()
pattern = r"[@#]+([a-z]{3,})[@#]+[^a-zA-Z0-9]*\/+(\d+)\/+"

matches = re.findall(pattern, text)

for egg_colour, amount in matches:
    print(f"You found {amount} {egg_colour} eggs!")