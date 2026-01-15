VIP_TICKET = 499.99
NORMAL_TICKET = 249.99

budget = float(input())
type_of_ticket = input()
number_of_people = int(input())

transport = 0
bill = 0
if type_of_ticket == "VIP":
    bill = number_of_people * VIP_TICKET
    if 1 <= number_of_people <= 4:
        transport = budget * 0.75
    elif 5 <= number_of_people <= 9:
        transport = budget * 0.60
    elif 10 <= number_of_people <= 24:
        transport = budget * 0.50
    elif 25 <= number_of_people <= 49:
        transport = budget * 0.40
    elif number_of_people > 50:
        transport = budget * 0.25
elif type_of_ticket == "Normal":
    bill = number_of_people * NORMAL_TICKET
    if 1 <= number_of_people <= 4:
        transport = budget * 0.75
    elif 5 <= number_of_people <= 9:
        transport = budget * 0.60
    elif 10 <= number_of_people <= 24:
        transport = budget * 0.50
    elif 25 <= number_of_people <= 49:
        transport = budget * 0.40
    elif number_of_people > 50:
        transport = budget * 0.25

final_bill = bill + transport

if final_bill < budget:
    print(f"Yes! You have {budget - final_bill:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_bill - budget:.2f} leva.")