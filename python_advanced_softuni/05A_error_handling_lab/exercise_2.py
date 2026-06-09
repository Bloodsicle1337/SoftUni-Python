txt = input()
try:
    times = int(input())

except ValueError:
    print("Variable times must be an integer")

else:
    print(txt * times)