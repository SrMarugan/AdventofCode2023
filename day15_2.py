def hash_code(char: str) -> int:
    num = 0
    for ch in list(char):
        if ch == "=" or ch == "-":
            return num
        else:
            num += ord(ch)
            num = (num*17)%256
    return num

with open(file="input15.txt") as file:
    line = file.readline().strip().split(",")
    boxes = {}
    for i in range(0, 256):
        boxes[i] = []
    for hash in line:
        if "=" in hash:
            box = hash_code(hash)
            lente = list(hash)
            num = lente.pop()
            lente.pop()
            str_lente = "".join(lente)
            bool_remplace = True
            for index, value in enumerate(boxes[box]):
                if str_lente == value[0]:
                    bool_remplace = False
                    boxes[box].pop(index)
                    boxes[box].insert(index, [str_lente, num])
            if bool_remplace:
                boxes[box].append([str_lente, num])
        if "-" in hash:
            box = hash_code(hash)
            str_hash = list(hash)
            str_hash.pop()
            str_hash = "".join(str_hash)
            for index, value in enumerate(boxes[box]):
                if str_hash == value[0]:
                    boxes[box].pop(index)
    result = 0
    for i in range(0, 256):
        for index, value in enumerate(boxes[i]):
            #print(f"Box {i}: {(i+1)} Slot: {index+1} Focal Length: {int(value[1])} Total: {(i+1)*int(value[1])*(index+1)}")
            result += (i+1)*int(value[1])*(index+1)
            #print(result)
    # for i in range(0, 256):
    #     print(i, boxes[i])
    print(result)
