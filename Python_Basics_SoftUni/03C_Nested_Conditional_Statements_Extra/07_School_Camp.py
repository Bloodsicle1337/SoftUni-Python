season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())

hotel_price = 0
sport = ""

if season == "Winter":
    if type_of_group == "boys":
        hotel_price = number_of_students * (number_of_nights * 9.60)
        sport = "Judo"
    elif type_of_group == "girls":
        hotel_price = number_of_students * (number_of_nights * 9.60)
        sport = "Gymnastics"
    elif type_of_group == "mixed":
        hotel_price = number_of_students * (number_of_nights * 10)
        sport = "Ski"
elif season == "Spring":
    if type_of_group == "boys":
        hotel_price = number_of_students * (number_of_nights * 7.20)
        sport = "Tennis"
    elif type_of_group == "girls":
        hotel_price = number_of_students * (number_of_nights * 7.20)
        sport = "Athletics"
    elif type_of_group == "mixed":
        hotel_price = number_of_students * (number_of_nights * 9.50)
        sport = "Cycling"
elif season == "Summer":
    if type_of_group == "boys":
        hotel_price = number_of_students * (number_of_nights * 15)
        sport = "Football"
    elif type_of_group == "girls":
        hotel_price = number_of_students * (number_of_nights * 15)
        sport = "Volleyball"
    elif type_of_group == "mixed":
        hotel_price = number_of_students * (number_of_nights * 20)
        sport = "Swimming"

if number_of_students >= 50:
    hotel_price -= hotel_price * 0.50
elif 20 <= number_of_students < 50:
    hotel_price -= hotel_price * 0.15
elif 10 <= number_of_students < 20:
    hotel_price -= hotel_price * 0.05

print(f"{sport} {hotel_price:.2f} lv.")