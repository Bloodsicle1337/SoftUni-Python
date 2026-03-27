n = int(input())

pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {
        "composer": composer,
        "key": key
    }

command = input()

while command != "Stop":
    parts = command.split("|")
    action = parts[0]

    if action == "Add":
        piece = parts[1]
        composer = parts[2]
        key = parts[3]

        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {
                "composer": composer,
                "key": key
            }
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = parts[1]

        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = parts[1]
        new_key = parts[2]

        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")