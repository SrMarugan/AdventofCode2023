# with open(file="AdventCode\Day18\input.txt") as file:
#     lines = file.readlines()
#     direction = []
#     steps = []
#     actual_pos = [0, 0]
#     maxim_pos = [0, 0]
#     minim_pos = [0, 0]
#     for line in lines:
#         line = line.split(" ")

#         match line[0]:
#             case "R":
#                 actual_pos[0] = actual_pos[0] + int(line[1])
#                 if actual_pos[0] > maxim_pos[0]:
#                     maxim_pos[0] = actual_pos[0]
#             case "L":
#                 actual_pos[0] = actual_pos[0] - int(line[1])
#                 if actual_pos[0] < minim_pos[0]:
#                     minim_pos[0] = actual_pos[0]
#             case "U":
#                 actual_pos[1] = actual_pos[1] + int(line[1])
#                 if actual_pos[1] > maxim_pos[1]:
#                     maxim_pos[1] = actual_pos[1]
#             case "D":
#                 actual_pos[1] = actual_pos[1] - int(line[1])
#                 if actual_pos[1] < minim_pos[1]:
#                     minim_pos[1] = actual_pos[1]

#     max_x = maxim_pos[0]-minim_pos[0]+1
#     max_y = maxim_pos[1]-minim_pos[1]+1

#     mapa = [["."]*(max_x)]*(max_y)

# with open(file="AdventCode\Day18\mapa3.txt", mode="x") as write_file:
#     for value in mapa:
#         line = "".join(value)
#         write_file.write(line+"\n")

# with open(file="AdventCode\Day18\mapa3.txt") as read_file:
#     lines_2 = read_file.readlines()
#     mapa = []
#     for line_2 in lines_2:
#         aux = list(line_2)
#         aux.pop()
#         mapa.append(aux)

# with open(file="AdventCode\Day18\input.txt") as file:
#     lines = file.readlines()
#     actual_pos = [-int(minim_pos[0]), -int(minim_pos[1])]
#     print(actual_pos)
#     for line in lines:
#         line = line.split(" ")
#         match line[0]:
#             case "R":
#                 for _ in range(int(line[1])):
#                     varaux = mapa[actual_pos[1]]
#                     print(varaux, actual_pos)
#                     if varaux[actual_pos[0]] == ".":
#                         varaux[actual_pos[0]] = "#"
#                     actual_pos[0] = actual_pos[0] + 1
#             case "L":
#                 for _ in range(int(line[1])):
#                     varaux = mapa[actual_pos[1]]
#                     print(varaux, actual_pos)
#                     if varaux[actual_pos[0]] == ".":
#                         varaux[actual_pos[0]] = "#"
#                     actual_pos[0] = actual_pos[0] - 1
#             case "U":
#                 for _ in range(int(line[1])):
#                     varaux = mapa[actual_pos[1]]
#                     print(varaux, actual_pos)
#                     if varaux[actual_pos[0]] == ".":
#                         varaux[actual_pos[0]] = "#"
#                     actual_pos[1] = actual_pos[1] + 1
#             case "D":
#                 for _ in range(int(line[1])):
#                     varaux = mapa[actual_pos[1]]
#                     print(varaux, actual_pos)
#                     if varaux[actual_pos[0]] == ".":
#                         varaux[actual_pos[0]] = "#"
#                     actual_pos[1] = actual_pos[1] - 1

# with open(file="AdventCode\Day18\mapa4.txt", mode="x") as write_file:
#     for value in mapa:
#         line = "".join(value)
#         write_file.write(line+"\n")

with open(file="AdventCode\Day18\mapa4.txt") as read_file:
    lines_3 = read_file.readlines()
    mapa = []
    for line_3 in lines_3:
        aux = list(line_3)
        aux.pop()
        mapa.append(aux)

    for line_map in mapa:
        draw = False
        for index, ch in enumerate(line_map):
            if index < len(line_map)-1:
                siguiente = line_map[index+1]
            else:
                siguiente = "E"

            if ch == "#" and siguiente == ".":
                if draw:
                    draw = False
                else:
                    draw = True
            if ch == "." and draw:
                line_map[index] = "#"

with open(file="AdventCode\Day18\mapa5.txt", mode="x") as write_file:
    for value in mapa:
        line = "".join(value)
        write_file.write(line+"\n")

    # for i in range(maxim_pos[0]-minim_pos[0]):
    #     for j in range(maxim_pos[1]-minim_pos[1]):
    #         mapa[i][j] = "."
    # print(maxim_pos, minim_pos)
