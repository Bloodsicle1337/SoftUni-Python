h = float(input()) * 100
w = float(input()) * 100

usable_w = w - 100
number_of_work_spaces_height = h // 120
number_of_work_spaces_width = usable_w // 70

work_spaces = (number_of_work_spaces_height * number_of_work_spaces_width) - 3
print(f"{int(work_spaces)}")