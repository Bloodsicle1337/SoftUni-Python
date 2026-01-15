health_check_days = int(input())
number_of_docs = 7
untreated = 0
treated = 0
for day in range(1, health_check_days + 1):
    patients = int(input())
    if day % 3 == 0:
        if untreated > treated:
            number_of_docs += 1

    if patients > number_of_docs:
        untreated += (patients - number_of_docs)
        treated += number_of_docs
    elif 0 < patients <= number_of_docs:
        treated += patients


print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")