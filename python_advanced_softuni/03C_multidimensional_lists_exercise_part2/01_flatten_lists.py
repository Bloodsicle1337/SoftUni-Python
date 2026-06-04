data = input()
temp = []
matrices = data.split("|")

for matrix in reversed(matrices):
    if matrix:
        numbers = matrix.split()
        temp.extend(numbers)

result = " ".join(temp)
print(result)