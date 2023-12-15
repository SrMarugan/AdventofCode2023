def hash_code(char: str) -> int:
    num = 0
    for ch in list(char):
        if char == "=" or char == "-":
            return num
        else:
            num += ord(ch)
            num = (num*17)%256
    return num
with open(file="AdventCode\Day15\input.txt") as file:
    line = []
    for linea in file:
        line = linea.strip().split(",")

    boxes = {}
    for i in range(0, 256):
        boxes[i] = []
    for hash in line:
        if "=" in hash:
            box = hash_code(hash)
            lente = list(hash)
            num = lente.pop()
            lente.pop()
            boxes[box].append(["".join(lente), num])
        if "-" in hash:
            box = hash_code(hash)
            str_hash = list(hash).pop()
            for index, value in enumerate(boxes[box]):
                if fafafa:
                    ...
            lente.pop()
            if lente in boxes[box]:
                lente2 = boxes[box].index(lente)

    print(boxes)
