def a_moverse(line, line2):
    bool_me_he_movido = False
    for index in range(len(line)-1):
        if index == len(line):
            print(index)
        for index2, char in enumerate(line2[len(line)-1-index]):
            if char == "O" and (line2[len(line)-(index+2)][index2] == "."):
                bool_me_he_movido = True
                line2[len(line)-(index+2)][index2] = "O"
                line2[len(line)-index-1][index2] = "."
    return bool_me_he_movido


with open(file="AdventCode\Day14\input.txt") as file:
    line = []
    line2 = []
    for linea in file:
        line.append(linea.strip())
        line2.append(list(linea.strip()))

    bool_me_he_movido = True
    while bool_me_he_movido:
        bool_me_he_movido = a_moverse(line, line2)

file = open(file="AdventCode\Day14\\21.txt", mode="x")
for linea in line2:
    cadena = "".join(linea) + "\n"
    file.write(cadena)

with open(file="AdventCode\Day14\\21.txt") as file:
    index = 100
    result = 0
    for linea in file:
        num_O = 0
        for char in linea.strip():
            if char == "O":
                num_O += 1
        result += index*num_O
        index -= 1
print(result)
