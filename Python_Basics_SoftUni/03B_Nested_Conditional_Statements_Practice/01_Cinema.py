type_of_ticket = input()
number_of_rows = int(input())
number_of_columns = int(input())
ticket_price = 0

if type_of_ticket == "Premiere":
    ticket_price = 12.00
elif type_of_ticket == "Normal":
    ticket_price = 7.50
elif type_of_ticket == "Discount":
    ticket_price = 5.00

seats = number_of_columns * number_of_rows
total_income = seats * ticket_price

print(f"{total_income:.2f}")
