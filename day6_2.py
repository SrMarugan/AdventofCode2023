# Day 6 Part 2
# I insert directly the input
tiempos = 48938466
distancia = 261119210191063

num = 0
for index in range(1, tiempos+1):
    if index*(tiempos-index) >= distancia:
        num += 1

print(num)
