n1 = int(input())
n2 = int(input())
operator = input()
result = ""

if operator == "+":
    result = (f"{n1} {operator} {n2} = {n1 + n2} "
                   f"{'- even' if (n1 + n2) % 2 == 0 else '- odd'}")
elif operator == "-":
    result = (f"{n1} {operator} {n2} = {n1 - n2} "
              f"{'- even' if (n1 - n2) % 2 == 0 else '- odd'}")
elif operator == "*":
    result = (f"{n1} {operator} {n2} = {n1 * n2} "
              f"{'- even' if (n1 * n2) % 2 == 0 else '- odd'}")
elif n2 == 0:
    result = f"Cannot divide {n1} by zero"
elif operator == "/":
    result = (f"{n1} {operator} {n2} = {n1 / n2:.2f}")
elif operator == "%":
    result = (f"{n1} {operator} {n2} = {n1 % n2}")

print(result)