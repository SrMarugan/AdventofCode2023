# Day 8 part 2
from math import lcm
file = open(file="AdventCode\Day8\input.txt")

lineas = file.readlines()

camino = []
inicio = []
lefts = []
rights = []
diccionario = {}
linea1 = lineas.pop(0)
for char in linea1:
    if char == "L":
        camino.append(0)
    elif char == "R":
        camino.append(1)

camino_max = len(camino)
lineas.pop(0)

for linea in lineas:
    linea = linea.split(" ")
    inicio.append(linea.pop(0))
    linea.pop(0)
    aux_str = []
    for index, char in enumerate(linea[0]):
        if index == 1 or index == 2 or index == 3:
            aux_str.append(char)
    lefts.append("".join(aux_str))

    aux_str = []
    for index, char in enumerate(linea[1]):
        if index == 0 or index == 1 or index == 2:
            aux_str.append(char)
    rights.append("".join(aux_str))

for index, var_aux in enumerate(inicio):
    diccionario[var_aux] = [lefts[index], rights[index]]

resultado = 0
camino_loop = 0
num_z = 0
new_camino = ["AAA", "FJA", "XPA", "DVA", "MPA", "TDA"]
multiplos = []
not_index = []
no_encontrado = True

while no_encontrado:
    if camino_loop >= camino_max:
        camino_loop = 0

    resultado += 1

    for index, camino_new in enumerate(new_camino):
        go_to = diccionario[camino_new]
        new_camino[index] = go_to[camino[camino_loop]]
        if "Z" in new_camino[index]:
            if index in not_index:
                ...
            else:
                multiplos.append(resultado)
                not_index.append(index)
                print(multiplos)
    camino_loop += 1
    if len(not_index) == len(new_camino):
        no_encontrado = False

print(lcm(*multiplos))

