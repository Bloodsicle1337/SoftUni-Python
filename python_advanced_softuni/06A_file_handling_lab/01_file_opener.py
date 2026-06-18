import os.path
from constants import path_to_dir

path = os.path.join(path_to_dir, "06A_file_handling_lab", "text.txt")


try:
    file = open(path)
    print("file found")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("file not found")
