from math import floor

def distance_to_center(x: float, y: float) -> float:
    return x ** 2 + y ** 2

def closer_point(x1: float, y1: float, x2: float, y2: float) -> str:
    first_distance = distance_to_center(x1, y1)
    second_distance = distance_to_center(x2, y2)

    if first_distance <= second_distance:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

result = closer_point(x1, y1, x2, y2)
print(result)