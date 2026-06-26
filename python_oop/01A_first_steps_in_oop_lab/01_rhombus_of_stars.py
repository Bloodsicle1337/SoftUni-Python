def print_lines(size, row):
    print(" " * (size - row) + "* " * row)

def print_lines_up(size):
    for row in range(1, size):
        print_lines(size, row)

def print_lines_down(size):
    for row in range(size, 0, -1):
        print_lines(size, row)

def print_rhombus(size:int):
    print_lines_up(size)
    print_lines_down(size)

num = int(input())
print_rhombus(num)