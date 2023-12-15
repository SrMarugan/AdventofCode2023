with open(file="AdventCode\Day15\input.txt") as file:
    line = []
    for linea in file:
        line = linea.strip().split(",")

    print(len(line), line)
    total = 0
    for hash in line:
        num = 0
        for ch in list(hash):
            num += ord(ch)
            num = (num*17)%256
        total += num
    print(total)
