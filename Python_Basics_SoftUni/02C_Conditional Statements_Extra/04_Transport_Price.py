TAXI_DAY_PRICE_KM = 0.79
TAXI_NIGHT_PRICE_KM = 0.90
TAXI_CALL_PRICE = 0.70
BUS_PRICE_PER_KM = 0.09
BUS_MIN_DISTANCE = 20
TRAIN_PRICE_PER_KM = 0.06
TRAIN_MIN_DISTANCE = 100

travel_distance = int(input())
time_of_day = input()
travel_sum = 0
time_price = ""

if time_of_day == "day":
    time_price = TAXI_DAY_PRICE_KM
elif time_of_day == "night":
    time_price = TAXI_NIGHT_PRICE_KM

if travel_distance < BUS_MIN_DISTANCE:
    travel_sum += TAXI_CALL_PRICE + time_price * travel_distance
elif travel_distance >= BUS_MIN_DISTANCE and travel_distance < TRAIN_MIN_DISTANCE:
    travel_sum += BUS_PRICE_PER_KM * travel_distance
elif travel_distance >= TRAIN_MIN_DISTANCE:
    travel_sum += TRAIN_PRICE_PER_KM * travel_distance

print(f"{travel_sum:.2f}")