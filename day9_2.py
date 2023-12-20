def dif_lista(lista):
    if all(x == 0 for x in lista):
        return 0

    deltas = [y - x for x, y in zip(lista, lista[1:])]
    diff = dif_lista(deltas)
    return lista[0] - diff
        

with open(file="adventcalendar\Day9\input.txt") as read_file:
    lines = read_file.readlines()
    resultado = 0
    for line in lines:
        nums = list(map(int, line.split()))
        resultado += dif_lista(nums)

print(resultado)
