import re

all_matches = []
pattern = r"\b_([a-zA-Z0-9]+)\b"

line = input()

matches = re.findall(pattern, line,)
if matches:
    all_matches += matches

print(",".join(all_matches))
