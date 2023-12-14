def a_moverse_norte(line, line2):
    bool_me_he_movido = False
    for index in range(len(line)-1):
        for index2, char in enumerate(line2[len(line)-1-index]):
            if char == "O" and (line2[len(line)-(index+2)][index2] == "."):
                bool_me_he_movido = True
                line2[len(line)-(index+2)][index2] = "O"
                line2[len(line)-index-1][index2] = "."
    return bool_me_he_movido


def a_moverse_oeste(line, line2):
    bool_me_he_movido = False
    for index in range(len(line)):
        for index2, char in enumerate(line2[index]):
            if index2 != 0:
                if char == "O" and (line2[index][index2-1] == "."):
                    bool_me_he_movido = True
                    line2[index][index2-1] = "O"
                    line2[index][index2] = "."
    return bool_me_he_movido


def a_moverse_sur(line, line2):
    bool_me_he_movido = False
    for index in range(len(line)-1):
        for index2, char in enumerate(line2[index]):
            if char == "O" and (line2[index+1][index2] == "."):
                bool_me_he_movido = True
                line2[index+1][index2] = "O"
                line2[index][index2] = "."
    return bool_me_he_movido


def a_moverse_este(line, line2):
    bool_me_he_movido = False
    for index in range(len(line)):
        for index2, char in enumerate(line2[index]):
            if index2 < len(line2[index])-1:
                if char == "O" and (line2[index][index2+1] == "."):
                    bool_me_he_movido = True
                    line2[index][index2+1] = "O"
                    line2[index][index2] = "."
    return bool_me_he_movido


with open(file="AdventCode\Day14\input.txt") as file:
    line = []
    line2 = []
    for linea in file:
        line.append(linea.strip())
        line2.append(list(linea.strip()))

resultados = []
resultados_2 = []
global_index = 0
while global_index < 400:
    bool_me_he_movido = True
    while bool_me_he_movido:
        bool_me_he_movido = a_moverse_norte(line, line2)

    bool_me_he_movido_2 = True
    while bool_me_he_movido_2:
        bool_me_he_movido_2 = a_moverse_oeste(line, line2)

    bool_me_he_movido_3 = True
    while bool_me_he_movido_3:
        bool_me_he_movido_3 = a_moverse_sur(line, line2)

    bool_me_he_movido_4 = True
    while bool_me_he_movido_4:
        bool_me_he_movido_4 = a_moverse_este(line, line2)

    index = 100
    result = 0
    for char in line2:
        num_O = 0
        for ch in char:
            if ch == "O":
                num_O += 1
        result += index*num_O
        index -= 1

    resultados.append(result)
    resultados_2.append(result)
    global_index += 1
    if (global_index%10) == 0:
        print(resultados)
        resultados = []
# Hay que ver cada cuanto se repite la cadena y calcular el resto, mi cadena repetida es: una_lista con longitud 77

una_lista = [86076, 86070, 86084, 86086, 86080, 86092, 86099, 86092, 86101, 86100, 86102, 86087, 86084, 86075, 86069, 86064, 86096, 86112,
86103, 86115, 86091, 86085, 86071, 86088, 86088, 86080, 86078, 86087,
86095, 86087, 86119, 86104, 86096, 86085, 86079, 86071, 86064, 86082,
86100, 86106, 86101, 86110, 86087, 86080, 86089, 86092, 86082, 86078,
86073, 86083, 86090, 86105, 86123, 86098, 86094, 86080, 86075, 86066,
86082, 86086, 86094, 86104, 86096, 86106, 86082, 86098, 86093, 86086,
86080, 86073, 86069, 86078, 86108, 86109, 86117, 86096, 86089]

# Anterior a esto hay 82 partes que no se repiten, por lo que 1000000000-82 / 77 -> Resto = 71 (al ser 0 una posicion más hay que encontrar la 70)

print(una_lista[70])

# file = open(file="AdventCode\Day14\\e.txt", mode="x")
# for linea in line2:
#     cadena = "".join(linea) + "\n"
#     file.write(cadena)

# with open(file="AdventCode\Day14\\0.txt") as file:
#     index = 100
#     result = 0
#     for linea in file:
#         num_O = 0
#         for char in linea.strip():
#             if char == "O":
#                 num_O += 1
#         result += index*num_O
#         index -= 1
# print(result)
