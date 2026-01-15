player1 = input()
player2 = input()

player1_points = 0
player2_points = 0

while True:
    card1 = input()

    if card1 == "End of game":
        print(f"{player1} has {player1_points} points")
        print(f"{player2} has {player2_points} points")
        break

    card2 = input()
    if card2 == "End of game":
        print(f"{player1} has {player1_points} points")
        print(f"{player2} has {player2_points} points")
        break

    card1 = int(card1)
    card2 = int(card2)

    if card1 > card2:
        player1_points += card1 - card2

    elif card2 > card1:
        player2_points += card2 - card1

    else:
        print("Number wars!")

        while True:
            war_card1 = int(input())
            war_card2 = int(input())

            if war_card1 != war_card2:
                if war_card1 > war_card2:
                    print(f"{player1} is winner with {player1_points} points")
                else:
                    print(f"{player2} is winner with {player2_points} points")
                break

        break
