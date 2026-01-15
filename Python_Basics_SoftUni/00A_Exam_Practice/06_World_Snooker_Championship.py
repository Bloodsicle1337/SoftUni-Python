QUARTER_FINAL_STANDARD = 55.50
QUARTER_FINAL_PREMIUM = 105.20
QUARTER_FINAL_VIP = 118.90

SEMI_FINAL_STANDARD = 75.88
SEMI_FINAL_PREMIUM = 125.22
SEMI_FINAL_VIP = 300.40

FINAL_STANDARD = 110.10
FINAL_PREMIUM = 160.66
FINAL_VIP = 400

tournament_stage = input()
type_of_ticket = input()
number_of_tickets = int(input())
trophy_picture = input()

total_bill = 0


if tournament_stage == "Quarter final":
    if type_of_ticket == "Standard":
        total_bill += number_of_tickets * QUARTER_FINAL_STANDARD
    elif type_of_ticket == "Premium":
        total_bill += number_of_tickets * QUARTER_FINAL_PREMIUM
    elif type_of_ticket == "VIP":
        total_bill += number_of_tickets * QUARTER_FINAL_VIP
elif tournament_stage == "Semi final":
    if type_of_ticket == "Standard":
        total_bill += number_of_tickets * SEMI_FINAL_STANDARD
    elif type_of_ticket == "Premium":
        total_bill += number_of_tickets * SEMI_FINAL_PREMIUM
    elif type_of_ticket == "VIP":
        total_bill += number_of_tickets * SEMI_FINAL_VIP
elif tournament_stage == "Final":
    if type_of_ticket == "Standard":
        total_bill += number_of_tickets * FINAL_STANDARD
    elif type_of_ticket == "Premium":
        total_bill += number_of_tickets * FINAL_PREMIUM
    elif type_of_ticket == "VIP":
        total_bill += number_of_tickets * FINAL_VIP

if trophy_picture == "Y":
    if 2500 < total_bill <= 4000:
        total_bill -= total_bill * 0.10
        total_bill += number_of_tickets * 40

    elif total_bill > 4000:
        total_bill -= total_bill * 0.25
    elif total_bill < 2500:
        total_bill += number_of_tickets * 40
else:
    if 2500< total_bill <= 4000:
        total_bill -= total_bill * 0.10
    elif total_bill > 4000:
        total_bill -= total_bill * 0.25
print(f"{total_bill:.2f}")
