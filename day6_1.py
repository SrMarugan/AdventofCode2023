# Day 6 Part 1
# I insert directly the input
tiempos = [48, 93, 84, 66]
distancia = [261, 1192, 1019, 1063]
numbers = []

for jindex in range(0, 4):
    num = 0
    for index in range(1, tiempos[jindex]+1):
        if index*(tiempos[jindex]-index) >= distancia[jindex]:
            num += 1
    numbers.append(num)

result = 1
for vals in numbers:
    result = result*vals

print(result)
