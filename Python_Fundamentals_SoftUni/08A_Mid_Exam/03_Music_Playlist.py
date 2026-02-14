list_of_songs = input().split()
number_of_commands = int(input())

for current_command in range(number_of_commands):
    command = input()

    if "Add" in command:
        new_command = command.split(" * ")
        song = new_command[1]
        if song not in list_of_songs:
            list_of_songs.append(song)
            print(f"{song} successfully added")

    elif "Delete" in command:
        new_command = command.split(" * ")
        number_of_songs_to_remove = int(new_command[1])

        if number_of_songs_to_remove <= len(list_of_songs):
            deleted_songs = list_of_songs[:number_of_songs_to_remove]
            print(f"{', '.join(deleted_songs)} deleted")
            del list_of_songs[0:number_of_songs_to_remove]

    elif "Shuffle" in command:
        new_command = command.split(" * ")
        first_index, second_index = int(new_command[1]), int(new_command[2])

        if 0 <= first_index < len(list_of_songs) and 0 <= second_index < len(list_of_songs):
            list_of_songs[first_index], list_of_songs[second_index] = list_of_songs[second_index], list_of_songs[first_index]
            print(f"{list_of_songs[first_index]} is swapped with {list_of_songs[second_index]}")

    elif "Insert" in command:
        new_command = command.split(" * ")
        song, index = new_command[1], int(new_command[2])

        if 0 <= index < len(list_of_songs):
            if song not in list_of_songs:
                list_of_songs.insert(index, song)
                print(f"{song} successfully inserted")

            else:
                print("Song is already in the playlist")

        else:
            print("Index out of range")

    elif command == "Sort":
        list_of_songs.sort(reverse=True)

    elif command == "Play":
        print("Songs to Play:")
        [print(song) for song in list_of_songs]