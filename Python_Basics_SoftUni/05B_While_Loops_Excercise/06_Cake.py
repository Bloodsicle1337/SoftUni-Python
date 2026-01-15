cake_total_size = int(input()) * int(input())

cake_slices_number = 0

is_finished = False

while cake_slices_number < cake_total_size:
    cake_slices_input = input()

    if cake_slices_input == "STOP":
        is_finished = True
        break

    cake_slices_input = int(cake_slices_input)
    cake_slices_number += cake_slices_input

if is_finished:
    print(f"{cake_total_size - cake_slices_number} pieces are left.")

else:
    print(f"No more cake left! You need {abs(cake_slices_number - cake_total_size)} pieces more.")