# Day 4 Part 1
# The input data is in the file
file = open(file="AdventCode\Day4\input.txt")
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lineas = file.readlines()
sumatory = 0
results_list = []
results_list2 = []
for linea in lineas:
    matches = 0
    start = False
    next_bool = True
    continue_bool = False
    number1 = []
    card = 0
    for ch in linea:
        if start:
            if ch in numbers:
                if next_bool:
                    numberx = (numbers.index(ch))
                else:
                    numberx = numberx*10 + (numbers.index(ch))
                next_bool = False
            elif ch == " ":
                if next_bool is not True:
                    next_bool = True
                    number1.append(str(numberx))
        elif ch == ":":
            start = True
        if continue_bool:
            if ch in numbers:
                if next_bool:
                    numbery = (numbers.index(ch))
                else:
                    numbery = numbery*10 + (numbers.index(ch))
                next_bool = False
            if ch == " " or ch == "\n":
                if next_bool is not True:
                    next_bool = True
                    if str(numbery) in number1:
                        #print(f"Match: {numbery} in {number1}")
                        matches += 1
                        if card == 0:
                            card = 1
                        else:
                            card = card*2
        if ch == "|":
            start = False
            continue_bool = True
            next_bool = True
    sumatory += card

print(sumatory)
