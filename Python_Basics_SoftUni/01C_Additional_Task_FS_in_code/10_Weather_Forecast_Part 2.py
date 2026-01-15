tell = float(input())

if tell >= 26.00 and tell <= 35.00:
    print("Hot")
elif tell >= 20.1 and tell <= 25.9:
    print("Warm")
elif tell >= 15.00 and tell <= 20.00:
    print("Mild")
elif tell >= 12.00 and tell <= 14.9:
    print("Cool")
elif tell >= 5.00 and tell <= 11.9:
    print("Cold")
else:
    print("unknown")