# Day 1 Part 1
# The input data is in the file
file = open(file="AdventCode\Day1\input.txt")
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

lineas = file.readlines()
sumatory = 0

for linea in lineas:
    first = True
    dec = 0
    numb = 0

    for ch in list(linea):
        if ch in numbers and first:
            dec = (numbers.index(ch)+1)*10
            numb = numbers.index(ch)+1
            first = False
        elif ch in numbers:
            numb = numbers.index(ch)+1
    sumatory += dec+numb
print(sumatory)
