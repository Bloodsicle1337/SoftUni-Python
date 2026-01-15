hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_minutes = (hour_of_exam * 60) + minute_of_exam
arrival_hour = (hour_of_arrival * 60) + minute_of_arrival

time_difference = exam_minutes - arrival_hour
time_print = ""

if time_difference > 30:
    time_print = "Early"
elif time_difference < 0:
    time_print = "Late"
else:
    time_print = "On time"

hours = abs(time_difference) // 60
minutes = abs(time_difference) % 60
result = ""

if hours > 0:
    result = f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result = f"{minutes} minutes"

if time_difference > 0:
    result += " before the start"
elif time_difference < 0:
    result += " after the start"

print(time_print)
print(result)