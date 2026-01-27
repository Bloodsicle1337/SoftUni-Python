deck_of_cards = input().split()
number_of_shuffles = int(input())
left_side = []
right_side = []

for shuffle in range(number_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_side = deck_of_cards[:middle_of_deck]
    right_side = deck_of_cards[middle_of_deck:]
    shuffled_deck = []
    for index in range(len(left_side)):
        shuffled_deck.append(left_side[index])
        shuffled_deck.append(right_side[index])

    deck_of_cards = shuffled_deck.copy()

print(deck_of_cards)