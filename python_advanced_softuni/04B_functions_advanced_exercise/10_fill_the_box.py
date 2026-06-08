def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    cubes_left = 0

    for index, value in enumerate(args):
        if value == "Finish":
            break

        box_size -= value

        if box_size < 0:
            cubes_left = abs(box_size)

            for cubes in args[index + 1:]:
                if cubes == "Finish":
                    break

                cubes_left += cubes

            return f"No more free space! You have {cubes_left} more cubes."

    return f"There is free space in the box. You could put {box_size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))