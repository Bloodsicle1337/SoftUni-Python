number_of_rooms = int(input())

free_chairs = 0
everything_is_ok = True

for room_number in range(1, number_of_rooms + 1):
    room_data = input().split()
    chairs = room_data[0]
    visitors = int(room_data[1])

    chairs_count = len(chairs)

    if chairs_count < visitors:
        needed_chairs = visitors - chairs_count
        print(f"{needed_chairs} more chairs needed in room {room_number}")
        everything_is_ok = False
    else:
        free_chairs += chairs_count - visitors

if everything_is_ok:
    print(f"Game On, {free_chairs} free chairs left")