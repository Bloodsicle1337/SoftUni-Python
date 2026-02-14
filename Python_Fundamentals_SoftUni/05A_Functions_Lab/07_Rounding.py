def string_floater_rounder(floaters):
    floaterers = floaters.split()
    rounded_integers = []

    for floater in floaterers:
        rounded_integers.append(round(float(floater)))

    return rounded_integers

stringed_input = input()

print(string_floater_rounder(stringed_input))