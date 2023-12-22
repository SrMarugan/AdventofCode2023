def detect_coord(lines):
    for index_y, line in enumerate(lines):
        for index_x, ch in enumerate(line):
            if ch == "S":
                cord = (index_y, index_x)
                return cord


def create_border(lines):
    border = []
    bord_x = ["#"]*(len(list(lines[0]))+1)
    border.append("".join(bord_x))
    for line in lines:
        bord_y = ["#"]
        line_list = list(line)
        line_list.pop()
        bord_y.append("".join(line_list))
        bord_y.append("#")
        border.append("".join(bord_y))
    border.append("".join(bord_x))
    return border


with open(file="AdventCode\Day21\input.txt") as file:
    lines = file.readlines()
    print(len(lines), len(list(lines[1])))
    border = create_border(lines)
    print(border)
    cord = []
    cord.append(detect_coord(lines))

    for _ in range(64):
        new_cord = []
        for c in cord:
            if border[c[0]+1][c[1]] == ".":
                border[c[0]+1][c[1]] = "O"
                new_cord.append((c[0]+1, c[1]))
            if border[c[0]][c[1]+1] == ".":
                border[c[0]][c[1]+1] = "O"
                new_cord.append((c[0], c[1]+1))
            if border[c[0]-1][c[1]] == ".":
                border[c[0]-1][c[1]] = "O"
                new_cord.append((c[0]-1, c[1]))
            if border[c[0]][c[1]-1] == ".":
                border[c[0]][c[1]-1] = "O"
                new_cord.append((c[0], c[1]-1))

        for __ in _:
            ...
            
