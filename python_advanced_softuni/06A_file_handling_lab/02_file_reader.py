import os.path
from constants import path_to_dir

path = os.path.join(path_to_dir, "numbers.txt")

file = open(path)
numbers = [int(el) for el in file.read().split("\n") if el]

print(sum(numbers))