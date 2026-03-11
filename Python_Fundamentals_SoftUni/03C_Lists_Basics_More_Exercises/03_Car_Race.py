number_of_index = input().split()
finish_line = len(number_of_index) // 2
left_car_time = 0
right_car_time = 0

left_car = number_of_index[:finish_line]
right_car = number_of_index[:finish_line:-1]

for left_num in left_car:
    num1 = int(left_num)
    if num1 == 0:
        left_car_time *= 0.8

    left_car_time += num1

for right_num in right_car:
    num2 = int(right_num)
    if num2 == 0:
        right_car_time *= 0.8

    right_car_time += num2

if right_car_time < left_car_time:
    print(f"The winner is right with total time: {right_car_time:.01f}")

elif left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.01f}")

else:
    print(f"Its a tie")