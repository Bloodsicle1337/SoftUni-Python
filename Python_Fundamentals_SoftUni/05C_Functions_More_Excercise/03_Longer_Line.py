from math import floor

def distance_to_center(x: float, y: float) -> float:
    return x ** 2 + y ** 2

def line_length(x1: float, y1: float, x2: float, y2: float) -> float:
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def line_coordinates(x1: float, y1: float, x2: float, y2: float) -> str:
    first_point_distance = distance_to_center(x1, y1)
    second_point_distance = distance_to_center(x2, y2)

    if first_point_distance <= second_point_distance:
        return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"

    else:
        return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

first_line_length = line_length(x1, y1, x2, y2)
second_line_length = line_length(x3, y3, x4, y4)

if first_line_length >= second_line_length:
    print(line_coordinates(x1, y1, x2, y2))
else:
    print(line_coordinates(x3, y3, x4, y4))