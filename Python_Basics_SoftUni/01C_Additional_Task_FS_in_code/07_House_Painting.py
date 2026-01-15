x = float(input())
y = float(input())
h = float(input())

#Walls
side_wall = x * y
window = 1.5 * 1.5
two_side_walls = 2 * side_wall - 2 * window
back_wall = x * x
door = 1.2 * 2
front_back_walls = back_wall * 2 - door
total_walls = two_side_walls + front_back_walls
green_paint = total_walls / 3.4

#Roof

roof_sides = 2 * (x * y)
roof_front_back = 2 * (x * h / 2)
total_roof = roof_sides + roof_front_back
red_paint = total_roof / 4.3

print(f"{green_paint:.2f}\n{red_paint:.2f}")