food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

enough = True

for day in range(1, 31):
    food -= 300

    if food <= 0:
        enough = False
        break

    if day % 2 == 0:
        hay_needed = food * 0.05
        hay -= hay_needed
        if hay <= 0:
            enough = False
            break

    if day % 3 == 0:
        cover_needed = weight / 3
        cover -= cover_needed
        if cover <= 0:
            enough = False
            break

if enough:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")