companies = {}

while True:
    company_register = input().split(" -> ")

    if len(company_register) == 1:
        break

    if company_register[0] not in companies.keys():
        companies[company_register[0]] = []

    if company_register[1] not in companies[company_register[0]]:
        companies[company_register[0]].append(company_register[1])

for company_name, employee_id in companies.items():
    print(company_name)
    for employee in employee_id:
        print(f"-- {employee}")