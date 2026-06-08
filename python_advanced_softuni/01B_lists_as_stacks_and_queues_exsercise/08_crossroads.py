from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0

while True:
    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{passed_cars} total cars passed the crossroads.")
        break

    if command == "green":
        current_green = green_light

        while cars and current_green > 0:
            car = cars.popleft()

            if len(car) <= current_green:
                current_green -= len(car)
                passed_cars += 1

            else:
                remaining_time = current_green + free_window

                if len(car) <= remaining_time:
                    passed_cars += 1
                    current_green = 0

                else:
                    hit_index = remaining_time
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    exit()

    else:
        cars.append(command)