electrons = int(input())

shells = []
position = 1

while electrons > 0:
    max_electrons = 2 * position ** 2

    if electrons >= max_electrons:
        shells.append(max_electrons)
        electrons -= max_electrons
    else:
        shells.append(electrons)
        electrons = 0

    position += 1

print(shells)