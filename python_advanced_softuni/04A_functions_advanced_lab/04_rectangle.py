def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        area_result = length * width
        return f"Rectangle area: {area_result}\n"

    def perimeter():
        peri_result = 2 * (length + width)
        return f"Rectangle perimeter: {peri_result}"

    return area() + perimeter()

print(rectangle('2', 10))