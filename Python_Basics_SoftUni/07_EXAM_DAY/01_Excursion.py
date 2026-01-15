NIGHT_PRICE = 20
TRANSPORT_PRICE = 1.60
MUSEUM_PRICE = 6

number_of_people = int(input())
number_of_nights = int(input())
number_of_transport_cards = int(input())
number_of_museum_tickets = int(input())

one_person_night_price = number_of_nights * NIGHT_PRICE
one_person_transport_price = number_of_transport_cards * TRANSPORT_PRICE
one_person_museum_price = number_of_museum_tickets * MUSEUM_PRICE
one_person_total_sum = one_person_night_price + one_person_transport_price + one_person_museum_price

total_sum = one_person_total_sum * number_of_people

total_sum += total_sum * 0.25

print(f"{total_sum:.2f}")


