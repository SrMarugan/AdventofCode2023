with open(file="AdventCode\Day4\input.txt") as file:
    copies = []
    for linea in file:
        line = linea.strip()
        line = line.split(":")
        card = line[0].split(" ")[1]
        win_numbers = line[1].split("|")[0].split(" ")
        numbers = line[1].split("|")[1].split(" ")
        numbers_b = []
        for x in numbers:
            if x != "":
                numbers_b.append(int(x))

        win_numbers_2 = []
        for x in win_numbers:
            if x != "":
                win_numbers_2.append(int(x))

        prizes = 0
        at_least_one = False

        for win in win_numbers_2:
            if int(win) in numbers_b:
                at_least_one = True
                prizes += 1
        copies.append(prizes)
    copies_2 = [1]*len(copies)
    for index, num in enumerate(copies):
        for mult in range(1, num+1):
            if index+mult+1 < len(copies_2)+1:
                copies_2[index+mult] += copies_2[index]

    print(sum(copies_2))
