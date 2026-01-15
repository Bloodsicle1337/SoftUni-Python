student_totally_sold_tickets = 0
standard_totally_sold_tickets = 0
kid_totally_sold_tickets = 0
total_seats_sold = 0


while True:
    name_of_movie = input()

    if name_of_movie == "Finish":
        break

    total_seats_available = int(input())
    current_tickets_sold = 0

    while current_tickets_sold < total_seats_available:
        type_of_ticket = input()

        if type_of_ticket == "End":
            break

        if type_of_ticket == "standard":
            current_tickets_sold += 1
            total_seats_sold += 1
            standard_totally_sold_tickets += 1

        elif type_of_ticket == "student":
            current_tickets_sold += 1
            total_seats_sold += 1
            student_totally_sold_tickets += 1

        elif type_of_ticket == "kid":
            current_tickets_sold += 1
            total_seats_sold += 1
            kid_totally_sold_tickets += 1

    print(f"{name_of_movie} - {current_tickets_sold / total_seats_available * 100:.2f}% full.")

print(f"Total tickets: {total_seats_sold}")
print(f"{student_totally_sold_tickets / total_seats_sold * 100:.2f}% student tickets.")
print(f"{standard_totally_sold_tickets / total_seats_sold * 100:.2f}% standard tickets.")
print(f"{kid_totally_sold_tickets / total_seats_sold * 100:.2f}% kids tickets.")